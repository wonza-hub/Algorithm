import sys
input=sys.stdin.readline

s=input().rstrip()
stack=[]
t=['P','P','A','P']
for i in s:
    stack.append(i)
    if stack[-4:]==t:
        for _ in range(4):
            stack.pop()
        stack.append('P')
print('PPAP' if stack==['P'] else 'NP')