# 리스트를 생성하는 3가지 방법(기본 loop, list comprehension, map) 비교

"""
1. 기본 loop

특징
- 직관적으로 이해하기 쉽고, 복잡한 로직을 담기에도 용이
- 반복문 내부에서 여러 변수를 업데이트하거나, 특정 조건에 따라 continue/break가 필요한 경우 유리
"""
result1 = []
for i in range(10):
    result1.append(i)


"""
# 2. list comprehension
특징
- 파이썬스러운(Pythonic) 방식으로 간결한 코드 작성 가능
- 조건문을 넣거나, 중첩 for 문을 사용하는 등 다양한 패턴을 구현하기에도 용이
- 가독성을 해치지 않을 선에서 사용하는 것이 중요
"""
result2 = [i for i in range(10)]
# result2 = list(i for i in range(10))


"""
3. map
특징
- 함수형 프로그래밍 스타일을 선호하거나, 이미 정의된 함수를 적용해야 할 때 유용
- 이미 존재하는 함수에 여러 값을 한꺼번에 적용할 때 가독성이 좋아짐
- 복잡한 로직은 map 내부에서 처리하기가 난해하므로, 코드가 오히려 읽기 어려워질 수 있음
"""
result3 = list(map(lambda i: i, range(10)))


"""
성능 비교

1. list comprehension
    - 대부분의 경우 가장 빠른 속도를 보임
2. map
    - 특정 상황(예: 기존 함수를 사용할 때, 매우 간단한 변환)의 경우
      list comprehension과 비슷하거나 약간 더 빠른 성능을 보일 수도 있음 (파이썬 버전 및 구현 세부사항에 따라 다름)
3. loop
    - 일반적으로는 list comprehension이나 map에 비해 조금 더 느린 경향을 보였지만
      python 버전이 올라가면서 다른 방식과 비슷하거나 때로는 더 나은 결과를 보이기도 함

결론
- 성능 차이는 대부분의 경우 미미하므로, 
  미세한 차이가 아니라면, 가독성과 유지보수성이 성능보다 더 중요
"""
