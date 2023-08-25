n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    row, dir, num = map(int, input().split())
    if dir == 0:
        for _ in range(num):
            data[row - 1].append(data[row - 1].pop(0))
    else:
        for _ in range(num):
            data[row - 1].insert(0, data[row - 1].pop())
    
s = 0
e = n
ans = 0
for i in range(n):
    for j in range(s, e):
        ans += data[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
        
print(ans)