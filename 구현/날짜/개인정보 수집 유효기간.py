dic={}

def calc_date(y,m,d):
    y,m,d=int(y[2:4]),int(m),int(d)
    # map(int, ~) 사용하면 코드 간소화 가능
    return 28*12*y+28*m+d

def is_over(today_d,privacy_d,약관):
    global dic
    return True if today_d-privacy_d>=dic[약관] else False
    
def solution(today, terms, privacies):
    ans=[]
    
    y,m,d=today.split('.')
    today_d=calc_date(y,m,d)
    
    for term in terms:
        약관,유효기간=term.split(' ')
        dic[약관]=28*int(유효기간)
        
    for idx,p in enumerate(privacies):
        date,약관=p.split(' ')
        y,m,d=date.split('.')
        privacy_d=calc_date(y,m,d)
        res=is_over(today_d,privacy_d,약관)
        if res:
            ans.append(idx+1)
        
    return ans