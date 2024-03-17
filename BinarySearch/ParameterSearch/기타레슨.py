n, m = map(int, input().split())
lectures = list(map(int, input().split()))
ans = int(1e9)

start = max(lectures)
end = sum(lectures)

def Count(max_volume):
    blue_lay_cnt = 1
    sum = 0
    for item in lectures:
        if (sum + item) > max_volume:
            blue_lay_cnt += 1
            sum = item
            continue
        sum += item    
        
    return blue_lay_cnt
    
while start <= end:
    mid = (start + end) // 2
    if Count(mid) <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)