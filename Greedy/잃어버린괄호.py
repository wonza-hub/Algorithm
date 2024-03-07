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