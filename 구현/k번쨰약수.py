n, k = map(int, input().split())
ord = 0
for i in range(1, n + 1):
    if n % i == 0:
        ord += 1
    if ord == k:
        print(i)
        break
else:
    print(-1)
    
        
    
            