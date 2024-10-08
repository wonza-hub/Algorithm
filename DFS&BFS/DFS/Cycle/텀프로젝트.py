def dfs(x):
    global ans
    ch[x] = 1
    cycle.append(x)
    pick = picks[x]

    if ch[pick]:
        if pick in cycle:
            ans += cycle[cycle.index(pick):]
    else:
        dfs(pick)

t = int(input())
for _ in range(t):
    n = int(input())
    picks = [0] + list(map(int, input().split()))
    ch = [1] + [0] * n
    ans = []
    
    for i in range(1, n + 1):
        if not ch[i]:
            cycle = []
            dfs(i)
            
    print(n - len(ans))

# 복습 풀이
import sys
sys.setrecursionlimit(111111)

def dfs(x, picks, ch, cycle, team):
    ch[x] = 1
    cycle.append(x)
    pick = picks[x]

    if ch[pick]:
        if pick in cycle:
            team += cycle[cycle.index(pick):]  # team 리스트에 요소 추가
            return team
    else:
        dfs(pick, picks, ch, cycle, team)

def solution():
    n = int(input())
    picks = [0] + list(map(int, input().split()))
    ch = [1] + [0] * n
    team = []

    for i in range(1, n + 1):  # 인덱스 범위 수정: 1부터 n까지
        if not ch[i]:
            cycle = []
            dfs(i, picks, ch, cycle, team)
    print(n - len(team))

t = int(input())
for _ in range(t):
    solution()