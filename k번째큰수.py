n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = arr[i] + arr[j] + arr[k]
            res.add(sum)

res = list(res)
res.sort(reverse = True)    
print(res[k - 1])