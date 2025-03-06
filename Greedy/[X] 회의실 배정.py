n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))
meetings.sort(key = lambda x : (x[1], x[0]))

end = -1
cnt = 0
for s, e in meetings:
    if s >= end:
        end = e
        cnt += 1

print(cnt)

# 복습 풀이
import sys
input=sys.stdin.readline

a=[list(map(int,input().rstrip().split())) for _ in range(int(input().rstrip()))]
a.sort(key=lambda x:(x[1],x[0]))

t,ans=0,0
for s,e in a:
    if s>=t:
        t=e
        ans+=1
print(ans)