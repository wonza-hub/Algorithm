n = int(input())
ans = -10e9

for i in range(n):
    a = list(map(int, input().split()))
    if len(set(a)) == 1:
        ans = max(ans, 10000 + a[0] * 1000)
    elif len(set(a)) == 3:
        ans = max(ans, max(a) * 100)
    else:
        if a[0] == a[1] or a[0] == a[2]:
            
            dup_num = a[0]
        elif a[1] == a[2]:
            dup_num = a[1]
        ans = max(ans, 1000 + dup_num * 100)
print(ans)
    
        