import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input().rstrip())):
    arr.append(input().rstrip())

arr=list(set(arr))
arr.sort(key=lambda x:(len(x),x))
for a in arr:
    print(a)