n = int(input())
nums = list(input().split())
max_sum = -10e9
ans = nums[0]

def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

for num in nums:
    tmp_sum = digit_sum(num)
    if tmp_sum > max_sum:
        max_sum = tmp_sum
        ans = num

print(ans)
    