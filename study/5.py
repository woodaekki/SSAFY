import sys
sys.stdin = open("1.txt", "r")

# 백준: 과일 탕후루
def solve():
    front = 0
    back = len(arr)-1
    # 앞에거 뺐을때
    arr.remove((arr[0:front]))
    if len(set(arr)) == 2:
        return len(arr)
    else:
        # 원복
        arr.append(arr[front])

    # 뒤에거 뺐을때
    i = 0
    arr.remove((arr[back:back-i:-1]))
    if len(set(arr)) == 2:
        return len(arr)
    else:
        # 원복
        arr.append(arr[back])

n = int(input())
arr = list(map(int, input().split()))
# print(solve())


