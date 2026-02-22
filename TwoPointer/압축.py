def solution(msg):
    ans=[]
    al=[chr(i) for i in range(65,91)]
    idx=[i for i in range(1,27)]
    dic=dict(zip(al,idx))
    
    s=e=0
    while True:
        e+=1
        if e==len(msg):
            ans.append(dic[msg[s:e]])
            break
        if msg[s:e+1] not in dic:
            dic[msg[s:e+1]]=len(dic)+1
            ans.append(dic[msg[s:e]])
            s=e
            
    return ans