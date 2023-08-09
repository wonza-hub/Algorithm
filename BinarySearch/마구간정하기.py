n, c = map(int, input().split())
line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()

def Count(len):
    cnt = 1
    ep = line[0]
    for i in range(1, n):
        if line[i] - ep >= len:
            cnt += 1
            ep = line[i]
    return cnt
    
start = 1
end = line[n - 1]
while start <= end:
    mid = (start + end) // 2
    if Count(mid) >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)