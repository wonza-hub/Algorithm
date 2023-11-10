n, m = map(int, input().split())
result = [0] * m
check = [0] * (n + 1)

def dfs(l):
    if l == m:
        for i in range(m):
            print(result[i], end = " ")
        print()
    else:
        for i in range(1, n + 1):
            if (check[i] == 1) or (l > 0 and result[l - 1] > i):
                continue
            result[l] = i
            check[i] = 1
            dfs(l + 1)
            check[i] = 0
dfs(0)

# 다른 사람의 풀이
n,m = list(map(int,input().split()))
s = []

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
            

            