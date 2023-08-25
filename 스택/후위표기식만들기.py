a = input()
stack = []
ans = ''
for x in a:
    if x.isdecimal():
        ans += x
    else:
        # 여는 괄호 처리
        if x == '(':
            stack.append(x)
        # *(곱하기), /(나누기) 처리
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(x)
        # +(더하기), -(빼기) 처리
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(x)
        # 닫는 괄호 처리
        elif x == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()

print(ans)
