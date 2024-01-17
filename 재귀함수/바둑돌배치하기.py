def solution(row, col):
    if row % 2 == 0 or col % 2 == 0:
        return 0
    
    return 1 + 4 * solution(row // 2, col // 2)

n, m = map(int, input().split())
print(solution(n, m))