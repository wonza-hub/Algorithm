# 비효율적인 풀이
# n = int(input())
# applicants = []
# for _ in range(n):
#     cm, kg = map(int, input().split())
#     applicants.append((cm, kg))
# applicants.sort(reverse=True)

# ans = len(applicants)
# check = [1] * ans
# for i in range(n - 1):
#     if check[i] == 0:
#         continue
#     for j in range(i + 1, n):
#         if check[j] == 0:
#             continue
#         if applicants[i][1] > applicants[j][1]:
#             check[j] = 0
#             ans -= 1

# print(ans)

# 효율적인 풀이 => 최댓값이 갱신될 떄마다 카운팅
n = int(input())
applicants = []
for _ in range(n):
    cm, kg = map(int, input().split())
    applicants.append((cm, kg))
applicants.sort(reverse=True)

max_kg = 0

cnt = 0
for cm, kg in applicants:
    if kg > max_kg:
        max_kg = kg
        cnt += 1

print(cnt)