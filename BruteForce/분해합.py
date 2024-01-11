n = int(input())
ans = 0

for num in range(1, n + 1):
    str_num = str(num)
    tmp = 0
    for x in str_num:
        tmp += int(x)
    if num + tmp == n:
        ans = num
        break

print(ans)