string = input()
bomb = input()
stack = []
bomb_len = len(bomb)

for i in string:
    stack.append(i)
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()
    
print('FRULA' if len(stack) == 0 else ''.join(stack))

