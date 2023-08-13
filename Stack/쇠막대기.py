a = input()
stack = []
ans = 0
for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
    else:
        stack.pop()
        # 레이저 등장
        if a[i - 1] == '(':
            ans += len(stack)
        # 막대기 오른쪽 끝부분
        else:
            ans += 1

print(ans)