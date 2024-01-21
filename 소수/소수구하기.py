import math

m, n = map(int, input().split())
check = [True for i in range(n + 1)]
check[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if check[i] == True:
        j = 2
        while i * j <= n:
            check[i * j] = False
            j += 1

for num in range(m, n + 1):
    if check[num] == True:
        print(num)
