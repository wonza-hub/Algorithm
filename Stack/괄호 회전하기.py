def check(arr):
    stack=[]
    for a in arr:
        if stack:
            if a==')' and stack[-1]=='(':
                stack.pop()
            elif a=='}' and stack[-1]=='{':
                stack.pop()
            elif a==']' and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(a)    
        else:
            stack.append(a)
    if len(stack):
        return 0
    else:
        return 1
    
def solution(s):
    ans=0
    l=len(s)
    s*=2
    for i in range(l):
        ans+=check(s[i:i+l])
        
    return ans
