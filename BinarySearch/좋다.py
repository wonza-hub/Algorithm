n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0

for i in range(n):
    tmp = nums[:i] + nums[i + 1:]
    l, r = 0, len(tmp) - 1
    while l < r:
        t = tmp[l] + tmp[r]
        if t == nums[i]:
            ans += 1
            break
        if t < nums[i]:
            l += 1
        else:
            r -= 1
print(ans)