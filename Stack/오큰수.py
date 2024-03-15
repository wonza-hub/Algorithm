import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
NGE = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
        
ans = ' '.join(map(str, NGE))
print(ans)
