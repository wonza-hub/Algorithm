n = int(input())
nums = list(map(int, input().split()))
ans = 0

def is_prime_num(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True      
    
for num in nums:
    if is_prime_num(num):
        ans += 1

print(ans)