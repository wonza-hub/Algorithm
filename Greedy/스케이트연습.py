import sys
input = sys.stdin.readline

n = int(input())
mid = list(map(int, input().split()))
v = [0] * (n + 1)
ans = 0
for i in range(n - 1, -1, -1):
    if mid[i] <= v[i + 1]:
        v[i] = mid[i]
    else:
        v[i] += v[i + 1] + 1
    ans += v[i]
    
print(ans)