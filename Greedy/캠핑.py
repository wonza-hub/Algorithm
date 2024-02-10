def greedy(l, p, v):
    global ans
    remain = v
    while remain > p:
        remain -= p
        ans += l
    if remain > l:
        ans += l
    else:
        ans += remain
        
    return ans
    
i = 1
while True:
    ans = 0
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    ans = greedy(l, p, v)
    print(f'Case {i}: {ans}')
    i += 1