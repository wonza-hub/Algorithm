def reverse(x):
    x = x[::-1]
    return x

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
arr = list(input().split())

for a in arr:
    a = reverse(a)
    num = 0
    for x in a:
        if x.isdecimal():
            num = num * 10 + int(x)
        
    if isPrime(num) == True:
        print(num, end=" ")

    
