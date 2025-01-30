from bisect import bisect_left

n=int(input())
arr=list(map(int,input().split()))

# set는 정렬 순서를 무시하고 재배치하므로 set를 리스트로 변환 후, 정렬해야함에 유의
sarr=list(set(arr))
sarr.sort() 

for a in arr:
    print(bisect_left(sarr,a),end=" ")