for _ in range(int(input())):
    ps = input()
    stack = []
    for p in ps:
        if len(stack) != 0 and p == ')':
            if stack[-1] == '(':
                stack.pop()
        else:
            stack.append(p)
            
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')