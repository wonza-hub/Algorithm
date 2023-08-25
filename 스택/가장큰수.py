n, m = input().split()
m = int(m)
arr = list(map(int, n))
stack = []
for num in arr:
    while stack and m > 0 and stack[-1] < num:
        stack.pop()
        m -= 1
    stack.append(num)
if m != 0:
    stack = stack[:-m]

print(''.join(map(str, stack)))
    
