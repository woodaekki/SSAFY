from rest_framework.response import Response
from .models import DepositProducts, DepositOptions
from .serializer import DepositProductSerializer, DepositOptionSerializer

import requests
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Max

@api_view(['GET'])
def save_deposit_products(request):
    # requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금
    # 상품 목록과 옵션 목록을 DB에 저장 
    API_KEY = '8fa6827478b5917c06649630bc32306f'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth=8fa6827478b5917c06649630bc32306f&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    # 응답이 올바른지 확인
    if not response.get("result"):
        return Response({"message": "Invalid response from API"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 상품 목록 저장
    base_list = response.get("result", {}).get("baseList", [])
    for pr in base_list:
        fin_prdt_cd = pr.get('fin_prdt_cd')
        
        # 이미 존재하는 상품은 저장하지 않음
        if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            Data = {
                'fin_prdt_cd': fin_prdt_cd,
                'kor_co_nm': pr.get('kor_co_nm', ''),
                'fin_prdt_nm': pr.get('fin_prdt_nm', ''),
                'etc_note': pr.get('etc_note', ''),
                'join_deny': pr.get('join_deny', 0),
                'join_member': pr.get('join_member', ''),
                'join_way': pr.get('join_way', ''),
                'spcl_cnd': pr.get('spcl_cnd', ''),
            }
            serializer = DepositProductSerializer(data=Data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"상품 저장 오류: {serializer.errors}")

    # 옵션 목록 저장
    option_list = response.get("result", {}).get("optionList", [])
    for pr2 in option_list:
        try:
            product_instance = DepositProducts.objects.get(fin_prdt_cd=pr2.get('fin_prdt_cd'))
        except DepositProducts.DoesNotExist:
            print(f"상품 {pr2.get('fin_prdt_cd')} 존재하지 않음")
            continue  # 상품이 없으면 건너뜀

        # 금리가 비어있으면 -1로 처리
        intr_rate = pr2.get('intr_rate')
        if intr_rate in [None, '']:
            intr_rate = -1

        option_Data = {
            'product': product_instance.pk,
            'fin_prdt_cd': pr2.get('fin_prdt_cd', ''),
            'intr_rate_type_nm': pr2.get('intr_rate_type_nm', ''),
            'intr_rate': intr_rate,
            'intr_rate2': pr2.get('intr_rate2', -1),
            'save_trm': pr2.get('save_trm', 0),
        }

        serializer = DepositOptionSerializer(data=option_Data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(f"옵션 저장 오류: {serializer.errors}")

    return Response({'message': 'Data successfully saved'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductSerializer(deposit_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DepositProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    # print(fin_prdt_cd)
    option = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    # print(option)
    serializer = DepositOptionSerializer(option, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    top_product = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    options = DepositOptions.objects.filter(intr_rate2=top_product['intr_rate2'])
    if not options.exists():
        return Response({"message": "No options found"}, status=404)

    
    options_serializer = DepositOptionSerializer(options, many=True)
    products = [DepositProducts.objects.get(id=option.product_id) for option in options]
    product_serializer = DepositProductSerializer(products, many=True)

    response_data = {
        'top_product': product_serializer.data,
        'options': options_serializer.data
    }
    return Response(response_data)