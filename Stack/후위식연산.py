a = input()
stack = []
ans = 0
for opt in a:
    if opt.isdecimal():
        stack.append(int(opt))
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if opt == '+':
            tmp = op1 + op2
        if opt == '-':
            tmp = op1 - op2
        if opt == '*':
            tmp = op1 * op2
        if opt == '/':
            tmp = op1 / op2
        stack.append(tmp)
        ans = tmp
print(ans)