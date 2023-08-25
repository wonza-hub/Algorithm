n = int(input())
mnt = [list(map(int ,input().split())) for _ in range(n)]
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mnt.insert(0, [0] * n)
mnt.append([0] * n)
for x in mnt:
    x.insert(0, 0)
    x.append(0)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        tmp = 0
        for k in range(4):
            nx = i + dx[k] 
            ny = j + dy[k]
            if mnt[i][j] > mnt[nx][ny]:
                tmp += 1
            else:
                break
        if tmp == 4:
            ans += 1
print(ans)

# 함수 all()를 활용한 간결한 풀이
n = int(input())
mnt = [list(map(int ,input().split())) for _ in range(n)]
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mnt.insert(0, [0] * n)
mnt.append([0] * n)

for x in mnt:
    x.insert(0, 0)
    x.append(0)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(mnt[i][j] > mnt[i + dx[k]][j + dy[k]] for k in range(4)):
            ans += 1
print(ans)