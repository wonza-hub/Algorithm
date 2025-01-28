def solution(arr):
    ans=0
    ms=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if ms<=arr[i]:
            ms=arr[i]
            continue
        if ms>arr[i]:
            ans+=ms-arr[i]

    return ans



for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=solution(arr)
    print(ans)
