import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "6e4b4ddadafecc802ff1d8fc2535c255"
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    # 응답을 json 형태로 변환 
    response = requests.get(url, params=params).json()
    return response['result']
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()

    base_list = result.get('baseList', [])  
    option_list = result.get('optionList', [])  

    final_products = []

    for base in base_list:
        product_code = base['fin_prdt_cd']  

        product_info = {
            '금융상품명': base['fin_prdt_nm'],
            '금융회사명': base['kor_co_nm'],
            '금리정보': []
        }

        for option in option_list:
            if option["fin_prdt_cd"] == product_code: # 금융상품코드가 같을 경우우
                new_dict = {}
                new_dict['저축 금리'] = option["intr_rate"]
                new_dict['저축 기간'] = option['save_trm']
                new_dict['저축 금리유형'] = option['intr_rate_type']
                new_dict['저축 금리유형명'] = option['intr_rate_type_nm']
                new_dict['최고 우대금리'] = option['intr_rate2']
                product_info['금리정보'].append(new_dict)  
        
        final_products.append(product_info)

    pprint.pprint(final_products)
