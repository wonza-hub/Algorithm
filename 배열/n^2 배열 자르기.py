def solution(n, left, right):
    ans=[]
    for i in range(left,right+1):
        a,b=i//n,i%n
        ans.append(max(a,b)+1)

    return ans