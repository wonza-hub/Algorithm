# 챗지피티 풀이
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
l = int(input())
ord_list = [int(input()) for _ in range(l)]

dp = [[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(l + 1)]


def dfs(idx, left, right):
    if idx == l:
        return 0  # 더 이상 열 벽장 없음

    if dp[idx][left][right] != -1:
        return dp[idx][left][right]

    target = ord_list[idx]

    # 이미 열려 있는 문이면 이동 불필요
    if target == left or target == right:
        dp[idx][left][right] = dfs(idx + 1, left, right)
        return dp[idx][left][right]

    # 두 경우 중 최소 이동 선택
    move_left = abs(left - target) + dfs(idx + 1, target, right)
    move_right = abs(right - target) + dfs(idx + 1, left, target)

    dp[idx][left][right] = min(move_left, move_right)
    return dp[idx][left][right]


print(dfs(0, a, b))
