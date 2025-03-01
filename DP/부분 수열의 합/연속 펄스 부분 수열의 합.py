# 연속된 부분 수열의 합의 최댓값을 구하는 함수
def find_max_part_sum(arr):
    d=[None]*len(arr)
    d[0]=arr[0]
    
    for i in range(1,len(arr)):
        d[i]=max(0,d[i-1])+arr[i]
        
    return max(d)
    
def solution(sequence):
    ap=[-e if i%2==0 else e for i,e in enumerate(sequence)]
    bp=[-e if i%2==1 else e for i,e in enumerate(sequence)]
    a=find_max_part_sum(ap)
    b=find_max_part_sum(bp)

    return max(a,b)