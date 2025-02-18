import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,d=map(int,input().rstrip().split())
    graph[u].append((v,d))
    graph[v].append((u,d))

def cal_dis(x,y):
    ans=0
    ch=[0]*(n+1)

    def dfs(v,td):
        nonlocal ans
        if v==y:
            ans=td
            return
        
        for i,d in graph[v]:
            if ch[i]:
                continue
            
            ch[i]=1
            dfs(i,td+d)
    ch[x]=1
    dfs(x,0)
    return ans

for _ in range(m):
    a,b=map(int,input().rstrip().split())
    ans=cal_dis(a,b)
    print(ans)

# 수행시간 개선 (정점 찾을 시, 상위 호출 스택 모두 종료)
import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,d=map(int,input().rstrip().split())
    graph[u].append((v,d))
    graph[v].append((u,d))

def cal_dis(x,y):
    ans=0
    ch=[0]*(n+1)

    def dfs(v,td):
        nonlocal ans
        if v==y:
            ans=td
            return True
        
        for i,d in graph[v]:
            if ch[i]:
                continue

            ch[i]=1

            if dfs(i,td+d):
                return True
    ch[x]=1
    dfs(x,0)

    return ans

for _ in range(m):
    a,b=map(int,input().rstrip().split())
    ans=cal_dis(a,b)
    print(ans)