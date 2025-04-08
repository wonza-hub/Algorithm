import sys
input=sys.stdin.readline

ans=0

def solution(s):
    stack=[]
    for al in s:
        if stack and stack[-1]==al:
            stack.pop()
            continue
        stack.append(al)

    return 1 if stack==[] else 0

for _ in range(int(input().rstrip())):
    ans+=solution(input().rstrip())

print(ans)