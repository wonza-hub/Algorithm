def sepa(w):
    a,b=0,0
    u,v='',''
    for i in range(len(w)):
        if w[i]=='(':
            a+=1
        elif w[i]==')':
            b+=1
        if a>0 and b>0 and a==b:
            u,v=w[:i+1],w[i+1:]
            break
            
    return u,v

def correct(u):
    stack=[]
    for 괄호 in u:
        if 괄호==')':
            if stack and stack[-1]=='(':
                stack.pop()
                continue
        stack.append(괄호)

    return False if stack else True
        
def slice(u):
    return u[1:-1]
    
def reverse(u):
    # replace 시 겹치는 문자를 한 번에 바꾸는 방법
    # 둘 중 하나의 문자를 임의의 문자로 바꿔놓음 
    return u.replace('(','0').replace(')','(').replace('0',')')
    
def recurse(w):
    if w=='':
        return ''
    u,v=sepa(w)       
        
    if correct(u):
        return u+recurse(v)
    else:
        return '('+recurse(v)+')'+reverse(slice(u))
        
def solution(p):
    ans=recurse(p)
    
    return ans