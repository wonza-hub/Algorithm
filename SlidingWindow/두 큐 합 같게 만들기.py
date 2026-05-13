def solution(queue1, queue2):
    all_sum=sum(queue1)+sum(queue2)
    if all_sum%2!=0:
        return -1
    
    target=all_sum//2
    q=queue1+queue2
    q1_sum=sum(queue1)
    n=len(queue1)
    q1,q2=0,n
    all_len=q2*2
    cnt=0
    
    # KEY POINT: 상한을 정해야 한다. 
    # q1은 최대 n + q2는 최대 2n
    while q1!=q2 and cnt<3*n:
        if q1_sum==target:
            return cnt
        elif q1_sum>target:
            tmp=q[q1]
            q1=(q1+1)%all_len
            q1_sum-=tmp
        else:
            tmp=q[q2]
            q2=(q2+1)%all_len
            q1_sum+=tmp
        cnt+=1
        
    return -1