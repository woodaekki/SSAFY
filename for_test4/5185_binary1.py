import sys
sys.stdin = open("tree.txt", "r")

def binary(n, new_arr):
    dicts = {"A":'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
    lst = []
    for key, val in dicts.items():
        for i in range(n):
            if new_arr[i] == key:
                new_arr[i] = val
    
    for j in range(n):
        remained = ""
        value = int(new_arr[j])
        len_part = len(new_arr[j])
        while value > 0:
            remain = value % 2
            remained = str(remain) + remained
            value = value // 2
        remained = remained.zfill(4)
        lst.append(remained)
    return "".join(lst)
            
T = int(input())
for t in range(1, T+1):
    n, arr = list(map(str, input().split()))
    n = int(n)
    new_arr = list(arr)
    result = binary(n, new_arr)
    print(f'#{t} {result}')