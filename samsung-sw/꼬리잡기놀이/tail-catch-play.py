# 삼성 22상 오후 1번
# nXn
# 머리사람
# 꼬리사람
# 팀: 3명 이상
#
# 한 라운드 규칙
# [1] 모든 팀: 머리사람 따라 한 칸 이동
# [2] 공 던짐: 좌->우, 하->상, 우->좌, 상->하
# [3] 공 얻음: 최초 얻는 사람 => k번째인 경우, k**2
# [4] 공 획득 팀: 머리사람<->꼬리사람 (방향 전환)
#
# 출력: 각 팀이 획득한 점수의 총합
from collections import defaultdict, deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def print2d(arr):
    for a in arr:
        print(*(f'{v:>4}' for v in a))
    print()


def 팀체크(sx, sy, 팀번호):
    global n, m, k, graph, 팀
    q = [(sx, sy)]
    팀[팀번호].append((sx, sy))
    graph[sx][sy] = 팀번호

    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 2인 경우 탐색
            if graph[nx][ny] == 2:
                팀[팀번호].append((nx, ny))
                graph[nx][ny] = 팀번호
                q.append((nx, ny))
            # 현재 좌표가 머리가 아니고 3인 경우 탐색 후 종료
            if ((x, y) != (sx, sy)) and graph[nx][ny] == 3:
                팀[팀번호].append((nx, ny))
                graph[nx][ny] = 팀번호
                return


# m: 팀개수 / k: 라운드 수
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
팀 = defaultdict(deque)


def main():
    global n, m, k, graph, 팀
    ans = 0

    # 팀 저장
    num = 5
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 1:
                continue
            if graph[i][j] == 1:
                팀체크(i, j, num)
                ch[i][j] = 1
                num += 1
    # k 라운드 반복
    for round in range(k):

        # [1] 모든 팀: 머리사람 따라 한 칸 이동
        for 팀번호, 팀원들 in 팀.items():
            # 꼬리사람 pop
            tx, ty = 팀원들.pop()
            graph[tx][ty] = 4
            # 머리사람이 다음 이동 선 찾기
            hx, hy = 팀원들[0]
            for i in range(4):
                nx = hx + dx[i]
                ny = hy + dy[i]
                # 범위 밖
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                # 이동 선
                if graph[nx][ny] == 4:
                    팀원들.appendleft((nx, ny))
                    graph[nx][ny] = 팀번호
                    break

        # [2] 공 던짐: 좌->우, 하->상, 우->좌, 상->하
        dr = (round // n) % 4
        offset = round % n
        if dr == 0:
            ci, cj = offset, 0
        elif dr == 1:
            ci, cj = n - 1, offset
        elif dr == 2:
            ci, cj = n - offset - 1, n - 1
        else:
            ci, cj = 0, n - offset - 1

        # [3] 공 얻음: 최초 얻는 사람 => s번째인 경우, s**2
        for _ in range(n):
            # 특정 팀의 팀원인 경우
            if 0 <= ci < n and 0 <= cj < n and graph[ci][cj] > 4:
                팀번호 = graph[ci][cj]
                ans += (팀[팀번호].index((ci, cj)) + 1) ** 2
                # [4] 공 획득 팀: 머리사람<->꼬리사람 (방향 전환)
                팀[팀번호].reverse()
                break
            ci, cj = ci + dx[dr], cj + dy[dr]

    print(ans)


if __name__ == '__main__':
    main()
