ops = ['+']
ans = 0

exp = input()
for op in exp:
    if op == '-' or op == '+':
        ops.append(op)

tmp = exp.replace('-', '+')
operands = list(map(int, tmp.split('+')))

for i in range(len(ops)):
    if ops[i] == '-':
        ans = sum(operands[:i]) - sum(operands[i:])
        break
    ans += operands[i]

print(ans)

# 복습 풀이
nums = []
optrs = []
line = input() + '+'
tmp = ''
minus_flag = False

answer = 0
tmp_sum = 0

for op in line:
    if op == '-' or op == '+':
        optrs.append(op)
        num = int(tmp)
        tmp_sum += num
        nums.append(num)
        tmp = ''
    else:
        tmp += op

answer = sum(nums)
for i in range(len(optrs)):
    if optrs[i] == '-':
        b = sum(nums[:i + 1])
        answer = b - (tmp_sum - b)
        break


print(answer)