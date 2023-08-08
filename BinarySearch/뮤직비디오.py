n, m = map(int, input().split())
musics = list(map(int, input().split()))
ans = 0

start = max(musics)
end = sum(musics)

def Count(cap):
    cnt = 1
    sum = 0
    for music in musics:
        if sum + music > cap:
            cnt += 1
            sum = music
        else:
            sum += music
    return cnt
    
while start <= end:
    mid = (start + end) // 2
    if Count(mid) <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)
        
            