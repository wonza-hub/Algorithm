# 리스트 pop() 연산은 리스트의 순서를 재조정하기에 시간복잡도 측면에서 비효율적임
# n, m = map(int, input().split())
# weights = list(map(int, input().split()))
# weights.sort()

# cnt = 0

# while weights:
#     min_weight = weights[0]
#     max_weight = weights[-1]
#     if len(weights) != 1 and min_weight + max_weight <= m:
#         weights.pop(0)
#     weights.pop()
#     cnt += 1

# print(cnt)

# deque 구현
from collections import deque

n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
weights = deque(weights)

cnt = 0

while weights:
    min_weight = weights[0]
    max_weight = weights[-1]
    if len(weights) != 1 and min_weight + max_weight <= m:
        weights.popleft()
    weights.pop()
    cnt += 1

print(cnt)

    