# 삼성 22상 오후 2번
# [1] 성장
# 1. 성장: 인접 네 칸 나무 칸 수만큼 성장. 모든 나무 동시
# 2. 번식: 해당 칸 그루 수//인접 네 칸 중 번식 가능 칸. 모든 나무 동시
# [2] 박멸
# 제초제 범위: k, 대각선, 벽 제외
#
# 출력: m년 동안 3개 과정 진행 시 총 박멸 그루 수

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]


def print2d(arr):
    for a in arr:
        print(*(f"{v:>4}" for v in a))
    print()


def copy2d(arr):
    return [x[:] for x in arr]


def 인접나무칸수(x, y, arr):
    나무칸수 = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 밖
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 나무가 있는 경우
        if arr[nx][ny] > 0:
            나무칸수 += 1
    return 나무칸수


def 인접나무칸수배열(graph):
    tmp = [[0] * n for _ in range(n)]
    # 기존 나무에 대해 인접 나무 칸 수 세기
    for i in range(n):
        for j in range(n):
            # 나무가 있는 경우
            if graph[i][j] > 0:
                tmp[i][j] = 인접나무칸수(i, j, graph)
    return tmp


# 해당 칸 그루 수//인접 네 칸 중 번식 가능 칸. 모든 나무 동시
def 번식(arr):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= 0:
                continue
            # 나무인 경우
            # 번식가능칸수 세서 가능 칸들에 나무 심기
            번식가능칸수 = 0
            번식가능칸 = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 범위 밖
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                # 벽: -1
                if arr[nx][ny] == -1:
                    continue
                # 다른 나무: 0<
                if arr[nx][ny] > 0:
                    continue
                # 제초제
                if 제초제[nx][ny] > 0:
                    continue
                번식가능칸수 += 1
                번식가능칸.append((nx, ny))
            if 번식가능칸수 <= 0:
                continue
            심을나무수 = arr[i][j] // 번식가능칸수
            for a, b in 번식가능칸:
                tmp[a][b] += 심을나무수
    return tmp


def 제초제좌표반환(arr):
    tmp = [[0] * n for _ in range(n)]
    제초제좌표 = [[[] for _ in range(n)] for _ in range(n)]
    최대박멸수 = 0
    ax, ay = 0, 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= 0:
                continue
            tmp[i][j] = arr[i][j]
            # 대각선 확인하며 박멸수에 더함
            # 제초제 전파: 대각선으로 k, 벽 제외, 범위 밖 제외
            # - 전파 중: 벽:-1 / 나무x:0 => 그 칸까지만 제초제 뿌림
            for dr in range(4, 8):
                s = 1
                while True:
                    if s > k:
                        break
                    nx = i + dx[dr] * s
                    ny = j + dy[dr] * s
                    # 범위 밖
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        break
                    # 대각선 k
                    # 벽
                    if arr[nx][ny] == -1:
                        break
                    # 나무 0
                    if arr[nx][ny] == 0:
                        제초제좌표[i][j].append((nx, ny))
                        break
                    # 합산
                    tmp[i][j] += arr[nx][ny]
                    s += 1
                    제초제좌표[i][j].append((nx, ny))
            # 행/열 우선
            if 최대박멸수 < tmp[i][j]:
                최대박멸수 = tmp[i][j]
                ax, ay = i, j

    return (최대박멸수, [(ax, ay)] + 제초제좌표[ax][ay])


def 두배열합(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
제초제 = [[0] * n for _ in range(n)]


def main():
    global n, m, k, c, graph, 제초제
    ans = 0
    # m년 진행
    for _ in range(m):
        # [1] 성장
        # 1. 성장: 인접 네 칸 나무 칸 수만큼 성장. 모든 나무 동시
        tmp = 인접나무칸수배열(graph)
        arr2 = 두배열합(graph, tmp)
        # 2. 번식
        ntree = 번식(arr2)
        arr3 = 두배열합(arr2, ntree)
        # [2] 박멸
        (최대박멸수, 제초제좌표) = 제초제좌표반환(arr3)
        ans += 최대박멸수
        # 제초제 제거
        for i in range(n):
            for j in range(n):
                제초제[i][j] = max(제초제[i][j] - 1, 0)
        # 각 칸 중 나무 가장 많이 박멸되는 칸에 제초제 뿌림
        # 제초제가 제초제 위에 뿌려질 때 더해지는 것이 아니고 덮어쓰는 것에 유의!!
        # '제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.'
        for x, y in 제초제좌표:
            제초제[x][y] = c
            arr3[x][y] = 0
        graph = arr3


    # 정답 출력
    print(ans)


if __name__ == '__main__':
    main()
