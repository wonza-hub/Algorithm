import sys
input=sys.stdin.readline
from collections import defaultdict

T=int(input().rstrip())
for _ in range(T):
    n,k,t,m=map(int,input().rstrip().split())
    cnt_dic=defaultdict(int)
    arr=[[0]*(k+2) for _ in range(n+1)]
    # 배열 요소 마지막에 팀 번호 기록
    for i in range(1,n+1):
        arr[i][k+1]=i
    for time in range(m):
        i,j,s=map(int,input().rstrip().split())
        # 배열 요소 처음에 시간 기록
        arr[i][0]=time
        # 제출 횟수 추가
        cnt_dic[i]+=1
        # 풀이한 문제에 대한 점수 초기화
        arr[i][j]=max(arr[i][j],s)

    res=arr[1:]
    res.sort(key=lambda x:[sum(x[1:k+1]),-cnt_dic[x[k+1]],-x[0]],reverse=True)

    for i in range(len(res)):
        if res[i][k+1]==t:
            print(i+1)