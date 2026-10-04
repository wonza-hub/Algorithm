                                # 삼성 26상 오전 1번
#
# 안식처 N-1, N-1 위치
# 시뮬레이션 최대 100턴
# [1] 바다거북 이동
# [2] 화산 압력 증가
# [3] 화산 분출 및 연쇄 반응
# 1. 열기 전파
# 2. 연쇄 반응
# 3. 화석화
# [4] 환경 초기화
#
import sys
input=sys.stdin.readline
from collections import deque

# [수정] 상·좌·하·우 → 우·하·좌·상 순서. 이 배열 순서가 곧 최단경로 우선순위
dx=[0,1,0,-1]
dy=[1,0,-1,0]


def print2d(arr):
    for a in arr:
        print(*(f"{v:>4}" for v in a))
    print()


def 안식처로부터_거북이탐색(tx,ty,N,sea):
    # [수정] "거북이에 처음 닿은 방향"을 쓰지 않고, 거리 배열을 만든 뒤
    #        거북이 이웃을 우·하·좌·상 순서로 보며 dist가 1 작은 첫 칸을 고른다
    dist=[[-1]*N for _ in range(N)]        # [수정] ch(방문배열) → dist(거리배열)
    dist[N-1][N-1]=0
    q=deque([(N-1,N-1)])                   # [수정] 시작점 하나만, 방향 정보 불필요

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 범위밖
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 방문
            if dist[nx][ny]!=-1:
                continue
            # 산호초
            if sea[nx][ny] == 1:
                continue
            # 찾으려는 거북이 아닌 살아있는 거북
            if (nx!=tx or ny!=ty) and sea[nx][ny] == 2:
                continue
            # 화석
            if sea[nx][ny] == 3:
                continue
            dist[nx][ny]=dist[x][y]+1
            q.append((nx,ny))

    # [추가] 경로 없음
    if dist[tx][ty]==-1:
        return None
    # [추가] 우·하·좌·상 순서로 dist가 정확히 1 작은 이웃 선택
    for i in range(4):
        nx=tx+dx[i]
        ny=ty+dy[i]
        if 0<=nx<N and 0<=ny<N and dist[nx][ny]==dist[tx][ty]-1:
            return [nx,ny]
    return None


def 화산분출(화산,화산번호,열기,sea,N):
    x,y,P,h=화산[화산번호]
    열기[x][y]+=P

    for i in range(4):
        sh=P                                # [수정] 압력(h)이 아니라 임계치 P 부터 절반씩
        k=1
        while True:
            nx=x+dx[i]*k
            ny=y+dy[i]*k
            # 범위밖
            if nx<0 or nx>=N or ny<0 or ny>=N:
                break
            # 산호초
            if sea[nx][ny]==1:
                break
            sh//=2
            # 열기 0
            if sh<=0:
                break
            열기[nx][ny]+=sh
            k+=1

def main():
    N,M,K=map(int,input().split())
    ans=[-1]*M
    sea=[list(map(int,input().split())) for _ in range(N)]
    거북=[list(map(int,input().split())) for _ in range(M)]
    화산=[list(map(int,input().split()))+[0] for _ in range(K)]
    alive=[True]*M                          # [추가] 살아있고 아직 도착하지 않은 거북

    for tx,ty in 거북:
        sea[tx][ty]=2

    # 최대 100턴
    for turn in range(1,101):               # [수정] 턴 번호 1부터 (출력이 1-based)
        # [1] 바다거북 이동
        for tidx,t in enumerate(거북):
            # [수정] sea[tx][ty]==3 검사 대신 alive 플래그 (화석 + 도착 모두 제외)
            if not alive[tidx]:
                continue
            tx,ty=t
            res=안식처로부터_거북이탐색(tx,ty,N,sea)
            if res==None:
                continue
            nx,ny=res
            # [삭제] print(nx,ny) / print2d(sea)  디버그 출력 제거
            sea[tx][ty] = 0
            거북[tidx]=[nx,ny]              # [추가] 거북 위치 갱신 (원래 코드에 없었음)
            # 다음위치가 안식처
            # 정답에 기록
            if nx==N-1 and ny==N-1:
                ans[tidx]=turn
                alive[tidx]=False           # [추가] 지도에서 즉시 제외
            else:                           # [수정] 안식처가 아닐 때만 sea에 표시
                sea[nx][ny] = 2

        # [2] 화산 압력 증가
        for idx,vol in enumerate(화산):
            화산[idx][3]+=10                 # [수정] min(p+10,P) 클램프 제거 (결과엔 영향 없지만 문제 그대로)

        열기 = [[0] * N for _ in range(N)]
        폭발여부=[0]*K

        # [3] 화산 분출 및 연쇄 반응
        vq=[idx for idx,[_, _, P, p] in enumerate(화산) if P<=p]

        for i in vq:
            폭발여부[i]=1
        while vq:
            # 1. 열기 전파
            for 화산번호 in vq:
                화산분출(화산,화산번호,열기, sea, N)
            vq=[]
            # 2. 연쇄 반응 (화산 추가)
            for i in range(K):
                # [수정] 비교 연산자 누락 → >= 화산[i][2](P) 추가
                if not 폭발여부[i] and 화산[i][3]+열기[화산[i][0]][화산[i][1]] >= 화산[i][2]:
                    폭발여부[i]=1
                    vq.append(i)
        # 3. 화석화
        for tidx,(tx,ty) in enumerate(거북):   # [수정] 살아있는 거북만 검사
            if alive[tidx] and 열기[tx][ty]>=20:
                sea[tx][ty]=3
                alive[tidx]=False           # [추가]

        # [4] 환경 초기화
        for idx, vol in enumerate(화산):
            if 폭발여부[idx]==1:
                화산[idx][3]=0

        # [추가] 모두 도착/화석이면 조기 종료 (선택 사항)
        if not any(alive):
            break

    # [수정] print(ans) → 한 줄에 하나씩
    for a in ans:
        print(a)

if __name__=='__main__':
    main()