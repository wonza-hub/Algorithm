# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# n, m = map(int, input().split())
# parent = [0] * (n + 1)

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a == b:
#         return
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# for i in range(n + 1):
#     parent[i] = i

# for _ in range(m):
#     calc, a, b = map(int, input().split())
#     if calc == 0:
#         union_parent(parent, a, b)
#     elif calc == 1:
#         if find_parent(parent, a) == find_parent(parent, b):
#             print('YES')
#         else:
#             print('NO')

import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

def find(p,x):
    if p[x]!=x:
        p[x]=find(p,p[x])
    return p[x]

def uni(p,a,b):
    if a==b:
        return
    a=find(p,a)
    b=find(p,b)
    p[a]=b

n,m=map(int,input().rstrip().split())
p=[0]*(n+1)

for i in range(n+1):
    p[i]=i

for _ in range(m):
    op,a,b=map(int,input().rstrip().split())
    if op==0:
        uni(p,a,b)
    elif op==1:
        if find(p,a)==find(p,b):
            print('YES')
        else:
            print('NO')
