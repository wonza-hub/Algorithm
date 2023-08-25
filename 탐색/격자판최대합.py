# n = int(input())
# arr = []
# ans = 0
# for _ in range(n):
#     a = list(map(int, input().split()))
#     # 행의 합 중 최댓값을 정답으로 초기화
#     ans = max(ans, sum(a)) 
#     arr.append(a)

# # 두 대각선 합
# sum_accl = 0
# sum_accr = 0

# for j in range(n):
#     sum_col = 0
#     for i in range(n):
#         if i == j:
#             sum_accl += arr[i][j]
#         if i + j == n - 1:
#             sum_accr += arr[i][j]
#         sum_col += arr[i][j]
#     # 열의 합 중 최댓값을 정답으로 초기화
#     ans = max(ans, sum_col)
# # 대각선의 합 중 최댓값을 정답으로 초기화
# ans = max(ans, sum_accl, sum_accr)

# print(ans)

# 간결한 풀이
n = int(input())
ans = -10e9
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    sum1 = sum2 = sum3 = sum4 = 0
    for j in range(n):
        if i == j:
            sum3 += arr[i][j]
        if j == n - i - 1:
            sum4 += arr[i][j]
        # 행 고정(한 열 합산)
        sum1 += arr[i][j]
        # 열 고정(한 행 합산)
        sum2 += arr[j][i]
    ans = max(ans, sum1, sum2)
ans = max(ans, sum3, sum4)

print(ans)
    
    