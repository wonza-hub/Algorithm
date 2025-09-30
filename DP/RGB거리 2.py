# 생성형 AI 풀이
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = INF
for start in range(3):  # 0=R, 1=G, 2=B
    dp = [[INF]*3 for _ in range(n)]
    dp[0][start] = arr[0][start]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    for end in range(3):
        if end != start:  # 마지막 집 색이 시작 집 색과 달라야 함
            ans = min(ans, dp[n-1][end])

print(ans)