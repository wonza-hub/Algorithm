seriesNum = input()
seriesCnt = 0
ans = 666

while True:
    for i in range(len(str(ans)) - 2):
        if str(ans)[i: i+3] == '666':
            seriesCnt += 1
            break
    if seriesCnt == int(seriesNum):
        break
    else:
        ans += 1

print(ans)

# 복습시 풀이
n = int(input())
series = 0
title = 666

while True:
    if '666' in str(title):
        series += 1
    if series == n:
        break
    title += 1

print(title)    
            
