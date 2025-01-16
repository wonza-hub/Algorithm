n, m = map(int, input().split())
result = [0] * m

def dfs(l):
    if l == m:
        for j in range(m):
            print(result[j], end = " ")
        print()
    else:
        for i in range(1, n + 1):
            if l > 0 and i < result[l - 1]:
                continue
            result[l] = i
            dfs(l + 1)
dfs(0)
            
# 다른 사람 풀이
n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)
            
        
            