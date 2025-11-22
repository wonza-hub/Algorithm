import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
arr=list(map(int,input().split()))
rank=[]
for t in range(len(arr)):
    for i in range(len(rank)):
        if arr[t]==rank[i][2]:
            rank[i][0]+=1
            break
    # 사진틀 꽉 찬 경우
    else:
        if len(rank)==n:
            rank.pop()
        rank.append([1,t,arr[t]])
    rank.sort(key=lambda x:[-x[0],-x[1]])

rank.sort(key=lambda x:x[2])
for _,_,c in rank:
    print(c,end=" ")

