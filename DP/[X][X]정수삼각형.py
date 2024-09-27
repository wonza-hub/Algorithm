# 다른 사람 풀이 참고
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))

# 복습 풀이
import sys
input = sys.stdin.readline

d = []

n = int(input())
for _ in range(n):
    d.append(list(map(int, input().split())))    

for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            left, right = -1, d[i - 1][j]
        elif j == i:
            left, right = d[i - 1][j - 1], -1
        else:
            left, right = d[i - 1][j - 1], d[i - 1][j]
        d[i][j] = d[i][j] + max(left, right)
        
print(max(d[n - 1]))

# 복습 풀이(2)
#거쳐간 숫자의 합이 가장 큰 경우
#대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            a, b = 0, 0
            if j != 0:
                a = triangle[i - 1][j - 1]
            if i != j:
                b = triangle[i - 1][j]
                
            triangle[i][j] = max(a, b) + triangle[i][j]
    
    return max(triangle[len(triangle) - 1])