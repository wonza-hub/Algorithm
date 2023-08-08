k, n = map(int, input().split())
lans = []
ans = 0

for _ in range(k):
    lan = int(input())
    lans.append(lan)

start = 1
end = max(lans)

def Count(len):
    cnt = 0
    for lan in lans:
        cnt += lan // len
    return cnt

while start <= end:
    mid = (start + end) // 2
    if Count(mid) >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1    
        
print(ans)
        
            