import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(input())
ch=[0]*len(arr)
ans=0

def find(i):
    global ans
    s,e=i-k,i+k+1
    if i-k<0:
        s=0
    if i+k+1>len(arr):
        e=len(arr)
    # 로봇 기준으로 좌측에서는 가장 먼 부품을 선택 / 좌측에 없을 때는 우측에서 가장 가까운 부품을 선택
    for j in range(s,e):
        if arr[j]=='H':
            arr[j]='X'
            ans+=1
            ch[i]=1
            break
                
for i in range(len(arr)):
    if not ch[i] and arr[i]=='P':
        find(i)
            
print(ans)
        