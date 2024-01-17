n, k = map(int, input().split())
q = list(map(int, input().split()))

ans = -10e9
def f(sum):
    global ans
    if n < sum:
        return ans
    
    ans = max(ans, sum)
    for i in range(k):
        f(sum * 10 + q[i])
        
f(0)
print(ans)

