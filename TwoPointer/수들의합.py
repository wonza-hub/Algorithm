n, m = map(int, input().split())
seq = list(map(int ,input().split()))
sum = seq[0]
cnt = 0
lp, rp = 0, 1

while True:
    if sum < m:
        if rp < n:
            sum += seq[rp]
            rp += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= seq[lp]
        lp += 1
    else:
        sum -= seq[lp]
        lp += 1
        
print(cnt)