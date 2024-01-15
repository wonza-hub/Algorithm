t = int(input())
for ord in range(1, t + 1):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_new = arr[s-1:e]
    arr_new.sort()
    print(f'#{ord} {arr_new[k-1]}')
      
    
            