import sys
input=sys.stdin.readline

n=int(input().rstrip())
graph=list(list(input().rstrip().split()) for _ in range(n))
flag=False
t=[]

for x in range(n):
    for y in range(n):
        if graph[x][y]=='T':
            t.append((x,y))

def dfs(cnt):
    global flag
    if cnt==3:
        res=bfs()
        if res==True:
            flag=True
            return
    else: # 이 부분에서 else가 없으면, 위 조건에서 res가 False인 경우 무한루프 빠짐에 유의
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    dfs(cnt + 1)
                    graph[i][j] = 'X'
dx=[-1,0,1,0]
dy=[0,-1,0,1]
def bfs():
    for x,y in t:
        for i in range(4):
            nx,ny=x,y # 각 선생님에 따라 시선 시작을 초기화해줘야 하는 것에 유의
            while 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]=='O':
                    break
                if graph[nx][ny]=='S':
                    return False
                nx+=dx[i]
                ny+=dy[i]
    return True

dfs(0)
if flag:
    print('YES')
else:
    print('NO')


