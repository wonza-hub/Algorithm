from collections import defaultdict

def is_banned(id,b_id):
    for i in range(len(id)):
        if b_id[i]=='*':
            continue
        if id[i]!=b_id[i]:
            return True
    return False
    
def solution(user_id, banned_id):
    answer = 0
    n=len(banned_id)
    ch=defaultdict(int)
    ans=set()
    
    def dfs(l,id,ch,arr):
        if l==n:
            sarr=str(sorted(arr))
            ans.add(sarr)     
            return
        
        length=len(banned_id[l])
        b_id=banned_id[l]
        for id in user_id:
            if ch[id]:
                continue
            if len(id)!=length:
                continue
            if is_banned(id,b_id):
                continue
            ch[id]=1
            dfs(l+1,id,ch,arr+[id])
            ch[id]=0
        
    dfs(0,"",ch,[])
    
    return len(ans)