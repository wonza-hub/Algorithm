n, m = map(int, input().split())
score_list = []
time_list = []
max_score = -10e9
for _ in range(n):
    score, time = map(int, input().split())
    score_list.append(score)
    time_list.append(time)

def dfs(l, sum_score, sum_time):
    global max_score
    if sum_time > m:
        return
    if l == n:
        if sum_time <= m:
            max_score = max(max_score, sum_score)
    else:
        dfs(l + 1, sum_score, sum_time)
        dfs(l + 1, sum_score + score_list[l], sum_time + time_list[l])
    
dfs(0, 0, 0)
print(max_score)