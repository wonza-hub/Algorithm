k, n = map(int, input().split())
ans = 0
lans = []
for _ in range(k):
    lan = int(input())
    lans.append(lan)

l, r = 1, max(lans) # l을 0으로 설정하면 아래의 코드에서 mid로 나누는 부분에서 ZeroDivisionError 발생

while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for lan in lans:
        tmp = lan // mid 
        cnt += tmp
        
    if cnt >= n:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
    
# 강의 풀이
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
        
            