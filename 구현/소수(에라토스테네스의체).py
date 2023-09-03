import math

n = int(input())
arr = [True for i in range(n + 1)]
ans = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(2, n + 1):
    if arr[i]:
        ans += 1

print(ans)

# 강의 풀이
n = int(input())
ch = [True for i in range(n + 1)]
ans = 0

for i in range(2, n + 1):
    if ch[i] == True:
        ans += 1
        for j in range(i, n + 1, i):
            ch[j] = False

print(ans)
    
    