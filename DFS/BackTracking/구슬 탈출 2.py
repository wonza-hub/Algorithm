import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().rstrip().split())
arr=[list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]=='R':
            rx,ry=i,j
        if arr[i][j]=='B':
            bx,by=i,j

def move(x,y,dr):
    back=-1
    for cnt in range(1,10): # 최대로 뻗어가서 벽을 만날 때까지 고려
        nx,ny=x+dx[dr]*cnt,y+dy[dr]*cnt
        if arr[nx][ny]=='#':
            return cnt+back
        if arr[nx][ny]=='O':
            return cnt
        if arr[nx][ny]=='B' or arr[nx][ny]=='R':
            back-=1

def dfs(n,rx,ry,bx,by):
    global ans
    # 가지 치기
    if (n,rx,ry,bx,by) in v_set:
        return
    v_set.add((n,rx,ry,bx,by))

    # 종료조건
    if n>10:
        return
    # 하부호출
    for dr in range(4):
        # 이동칸수 계산
        r_cnt=move(rx,ry,dr)
        b_cnt=move(bx,by,dr)
        if r_cnt==0 and b_cnt==0:
            continue
        # 실제 이동 수행
        rnx,rny=rx+dx[dr]*r_cnt,ry+dy[dr]*r_cnt
        bnx,bny=bx+dx[dr]*b_cnt,by+dy[dr]*b_cnt

        # 이동완료한 위치가 홀인 경우 처리 (성공 or 실패)
        if arr[bnx][bny]=='O':
            continue
        else:
            if arr[rnx][rny]=='O':
                ans=min(ans,n)
                return

        # 둘 다 홀이 아닌 경우
        arr[rx][ry],arr[bx][by]='.','.'
        arr[rnx][rny],arr[bnx][bny]='R','B'
        dfs(n+1,rnx,rny,bnx,bny)
        arr[rnx][rny],arr[bnx][bny]='.','.'
        arr[rx][ry],arr[bx][by]='R','B'


ans=11
v_set=set()
dfs(1,rx,ry,bx,by)
if ans==11:
    ans=-1

print(ans)