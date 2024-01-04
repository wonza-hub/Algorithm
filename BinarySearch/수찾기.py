# 이진 탐색 풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
a.sort()

for num in arr:
    l, r = 0, n - 1
    isExist = False

    while l <= r:
        mid = (l + r) // 2
        if num == a[mid]:
            isExist = True
            print(1)
            break
        elif num > a[mid]:
            l = mid + 1
        else:
            r = mid - 1

    if not isExist:
        print(0)

# 딕셔너리 풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dict = {}
for a_item in a:
    dict[a_item] = 1
for b_item in b:
    if b_item in dict:
        print(1)
    else:
        print(0)    
