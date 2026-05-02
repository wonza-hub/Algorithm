from collections import deque

dx = [-1, 0, 0, 1]  # 상, 좌, 우, 하
dy = [0, -1, 1, 0]

def p2d(arr):
    for a in arr:
        print(*a)
    print()

def 가장가까운캠프찾기(idx, target_x, target_y):
    """목표 편의점에서 가장 가까운 베이스캠프 찾기"""
    global 베이스캠프, ch
    
    # 목표 편의점에서 역BFS
    q = deque()
    q.append((target_x, target_y))
    vi = [[0] * (n + 2) for _ in range(n + 2)]
    vi[target_x][target_y] = 1
    dist = [[float('inf')] * (n + 2) for _ in range(n + 2)]
    dist[target_x][target_y] = 0
    
    camps = []  # (거리, 행, 열) 저장
    
    while q:
        x, y = q.popleft()
        
        # 베이스캠프 발견
        if graph[x][y] == 1 and ch[x][y] == 0:
            camps.append((dist[x][y], x, y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 바깥 영역
            if graph[nx][ny] == -1:
                continue
            # 이미 막힌 곳
            if ch[nx][ny] == 1:
                continue
            # 이미 방문
            if vi[nx][ny] == 1:
                continue
            
            q.append((nx, ny))
            vi[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1
    
    # 가장 가까운 베이스캠프 선택 (거리, 행, 열 순으로 정렬)
    camps.sort()
    if camps:
        _, camp_x, camp_y = camps[0]
        베이스캠프[idx][0], 베이스캠프[idx][1] = camp_x, camp_y
        return camp_x, camp_y
    
    return -1, -1


def get_next_position(person_num, cur_x, cur_y):
    """현재 위치에서 편의점까지 최단거리로 가는 다음 1칸 선택"""
    target_x = 편의점[person_num][0]
    target_y = 편의점[person_num][1]
    
    # 이미 도착했으면 그대로
    if cur_x == target_x and cur_y == target_y:
        return cur_x, cur_y
    
    # 목표 편의점에서 역BFS로 모든 칸까지의 거리 계산
    dist = [[float('inf')] * (n + 2) for _ in range(n + 2)]
    q = deque([(target_x, target_y)])
    dist[target_x][target_y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 바깥 영역
            if graph[nx][ny] == -1:
                continue
            # 막힌 곳
            if ch[nx][ny] == 1:
                continue
            # 이미 방문
            if dist[nx][ny] != float('inf'):
                continue
            
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    
    # 현재 위치에서 우선순위대로 다음 칸 선택
    # 우선순위: 상(0), 좌(1), 우(2), 하(3)
    best_dir = -1
    min_dist = float('inf')
    
    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        
        # 바깥 영역
        if graph[nx][ny] == -1:
            continue
        # 막힌 곳
        if ch[nx][ny] == 1:
            continue
        
        # 더 가까운 방향 선택 (같으면 우선순위가 앞선 것 선택)
        if dist[nx][ny] < min_dist:
            min_dist = dist[nx][ny]
            best_dir = i
    
    if best_dir != -1:
        return cur_x + dx[best_dir], cur_y + dy[best_dir]
    
    return cur_x, cur_y  # 이동 불가


# 입력
n, m = map(int, input().split())
graph = [[-1] * (n + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)] + [[-1] * (n + 2)]
ch = [[0] * (n + 2) for _ in range(n + 2)]
편의점 = [[0, 0] for _ in range(m + 1)]
베이스캠프 = [[0, 0] for _ in range(m + 1)]
도착여부 = [0] * (m + 1)
사람위치 = [[0, 0] for _ in range(m + 1)]  # 각 사람의 현재 위치 (1개만)

for i in range(1, m + 1):
    x, y = map(int, input().split())
    편의점[i][0], 편의점[i][1] = x, y

time = 0

while True:
    time += 1
    
    # 1단계: 격자에 있는 사람들 모두 1칸 이동
    for num in range(1, m + 1):
        # 아직 출발 안 한 사람
        if num > time:
            continue
        # 이미 도착한 사람
        if 도착여부[num]:
            continue
        
        # 현재 위치
        cur_x, cur_y = 사람위치[num]
        
        # 다음 위치 계산 (정확히 1칸만!)
        next_x, next_y = get_next_position(num, cur_x, cur_y)
        
        # 위치 업데이트
        사람위치[num] = [next_x, next_y]
        
        # 편의점 도착 확인
        if next_x == 편의점[num][0] and next_y == 편의점[num][1]:
            도착여부[num] = 1
    
    # 2단계: 도착한 편의점 칸 막기
    for num in range(1, m + 1):
        if 도착여부[num]:
            ch[편의점[num][0]][편의점[num][1]] = 1
    
    # 3단계: 새 사람 베이스캠프 입장 (t ≤ m일 때)
    if time <= m:
        sx, sy = 가장가까운캠프찾기(time, 편의점[time][0], 편의점[time][1])
        사람위치[time] = [sx, sy]
        ch[sx][sy] = 1  # 베이스캠프 막기
    
    # 종료 조건: 모든 사람이 도착
    if sum(도착여부[1:m + 1]) == m:
        break

print(time)

# 오답 풀이 (99번 케이스 불통과)
from collections import deque

dx=[-1,0,0,1]
dy=[0,-1,1,0]

def p2d(arr):
    for a in arr:
        print(*a)
    print()

def 가장가까운캠프찾기(idx,a,b):
    global 베이스캠프,ch
    q=deque()
    q.append((a,b))
    vi = [[0] * (n + 2) for _ in range(n + 2)]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 빨간 곳
            if ch[nx][ny]==1:
                continue
            # bfs 방문한 영역
            if vi[nx][ny]==1:
                continue
            # 바깥 영역
            if graph[nx][ny]==-1:
                continue
            # 베이스캠프
            if graph[nx][ny]==1:
                베이스캠프[idx][0],베이스캠프[idx][1]=nx,ny
                ch[nx][ny]=1
                return nx,ny
            q.append((nx,ny))
            vi[nx][ny]=1


n,m=map(int,input().split())
graph=[[-1]*(n+2)]+[[-1]+list(map(int,input().split()))+[-1] for _ in range(n)]+[[-1]*(n+2)]
ch = [[0] * (n + 2) for _ in range(n + 2)]
편의점=[[0,0] for _ in range(m+1)]
베이스캠프=[[0,0] for _ in range(m+1)]
도착여부=[0]*(m+1)
v=[[[0]*(n+2) for _ in range(n+2)] for _ in range(m+1)]
사람q=[deque([]) for _ in range(m+1)]

for i in range(1,m+1):
    x,y=map(int,input().split())
    편의점[i][0],편의점[i][1]=x,y

time=0
while True:
    time+=1
    if sum(도착여부[1:m+1])==m:
        break

    if time<=m:
        번호=time
        sx, sy = 가장가까운캠프찾기(time, 편의점[번호][0], 편의점[번호][1])
        사람q[번호].append([sx, sy, 번호, time])
        v[번호][sx][sy]=1

    for num in range(1,m+1):
        if num>time:
            continue
        new_q=deque()
        while 사람q[num]:
            x,y,사람번호,t=사람q[num].popleft()
            if 도착여부[사람번호]:
                continue
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                # 바깥 영역
                if graph[nx][ny]==-1:
                    continue
                # 빨간 영역
                if ch[nx][ny]==1:
                    continue
                # 해당 사람이 방문한 영역
                if v[사람번호][nx][ny]==1:
                    continue
                # 해당 사람이 방문해야 할 편의점
                if nx==편의점[사람번호][0] and ny==편의점[사람번호][1]:
                    도착여부[사람번호]=1
                new_q.append([nx,ny,사람번호,t+1])
                v[사람번호][nx][ny]=1
        사람q[num]=new_q

    for no in range(1,m+1):
        if 도착여부[no]:
            ch[편의점[no][0]][편의점[no][1]]=1
        ch[베이스캠프[no][0]][베이스캠프[no][1]] = 1

print(time)