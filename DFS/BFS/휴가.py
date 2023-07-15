n = int(input())
time = [0]
pay = [0]
max_pay = -10e9
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

def dfs(d, sum_pay):
    global max_pay
    if d == n + 1:
        max_pay = max(max_pay, sum_pay)
    if d > n:
        return
    else:
        dfs(d + 1, sum_pay)
        dfs(d + time[d], sum_pay + pay[d])
        
dfs(1, 0)
print(max_pay)