# 금융상품정보 API Server

### A. 정기예금 상품 및 옵션 목록 저장
```python
response = requests.get(url).json()
base_list = response.get("result", {}).get("baseList", [])
option_list = response.get("result", {}).get("optionList", [])

# 상품 저장
for pr in base_list:
    if not DepositProducts.objects.filter(fin_prdt_cd=pr['fin_prdt_cd']).exists():
        serializer = DepositProductSerializer(data=pr)
        if serializer.is_valid():
            serializer.save()

# 옵션 저장
for pr2 in option_list:
    pr2['intr_rate'] = pr2.get('intr_rate', -1) or -1
    pr2['intr_rate2'] = pr2.get('intr_rate2', -1) or -1
    serializer = DepositOptionSerializer(data=pr2)
    if serializer.is_valid():
        serializer.save()
```
- 외부 금융 API를 통해 정기예금 상품과 옵션 정보를 가져와 데이터베이스에 저장
- 금리가 누락된 경우 `-1`로 대체 저장
- 상품 중복 저장을 방지

<br>

B. 전체 정기예금 상품 목록 출력
```
if request.method == 'GET':
    deposit_products = DepositProducts.objects.all()
    serializer = DepositProductSerializer(deposit_products, many=True)
    return Response(serializer.data)
```
-데이터베이스에 저장된 모든 정기예금 상품을 JSON 형태로 반환

<br>

C. 사용자 입력을 통한 정기예금 상품 추가
```
elif request.method == 'POST':
    serializer = DepositProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
```
- 사용자로부터 받은 JSON 데이터를 통해 새로운 정기예금 상품을 등록
- Postman 등 API 테스트 도구를 통해 입력 

<br>

D. 특정 상품의 옵션 리스트 출력
```
option = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
serializer = DepositOptionSerializer(option, many=True)
return Response(serializer.data)
```
- 상품 코드(fin_prdt_cd)에 해당하는 옵션 리스트를 JSON으로 반환

<br>

E. 최고 금리 상품 조회
```
top_product = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
options = DepositOptions.objects.filter(intr_rate2=top_product['intr_rate2'])
products = [DepositProducts.objects.get(id=option.product_id) for option in options]
```
- 모든 옵션 중에서 가장 높은 우대금리(intr_rate2)를 기준으로 상품 및 옵션 상세 정보를 반환

<br>

## 관통 프로젝트에서 배운 점 및 느낀 점

오늘 진행한 관통 프로젝트는 개인적으로 가장 어려운 시간이었습니다.  
특히 첫 주차에 배웠던 API를 활용해 정보를 불러오는 부분이  잘 기억나지 않아 큰 어려움을 겪었습니다.

또한 데이터를 성공적으로 불러오더라도, 이를 화면에 어떻게 보여줄지.
그리고 그 과정에서 발생하는 에러를 디버깅하는 작업도 쉽지 않았습니다.  

오늘 REST API에 대한 개념과 활용법이 아직 부족하다는 점을 깨달았고,  
주말 동안 관련 개념을 복습하고, 더 많은 실습을 통해 보완해야겠다고 다짐했습니다.