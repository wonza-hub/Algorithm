# DFS+누적합 (시간 초과)
import sys
sys.setrecursionlimit=10**8
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
p=[0]+list(map(int,input().rstrip().split()))
graph=[[] for _ in range(n+1)]
reward=[0]*(n+1)

for i in range(2,len(p)):
    graph[p[i]].append(i)

for _ in range(m):
    i,w=map(int,input().rstrip().split())
    reward[i]+=w

def dfs(u,r):
    for v in graph[u]:
        dfs(v,r+reward[v])
        reward[v]+=r

dfs(1,0)

print(*reward[1:])

# DP
import sys
input = sys.stdin.readline

n,m=map(int,input().rstrip().split())
p=[0]+list(map(int,input().rstrip().split()))

arr=[0]*(n+1)

for _ in range(m):
    i,w=map(int,input().split())
    arr[i]+=w

for i in range(2, n + 1):
    # 상사의 칭찬 수치를 부하직원에게 추가
    arr[i]+=arr[p[i]]

print(*arr[1:])