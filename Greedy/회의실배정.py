n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))
meetings.sort(key = lambda x : (x[1]))

end = -1
cnt = 0
for s, e in meetings:
    if s >= end:
        end = e
        cnt += 1

print(cnt)