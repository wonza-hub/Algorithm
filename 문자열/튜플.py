from collections import Counter

def to_num(s):
    num=0
    for ss in s:
        if ss.isdigit():
            num=num*10+int(ss)

    return num
    
def solution(s):
    arr=s[1:-1].split(',')
    arr=[to_num(a) for a in arr]
    
    c=Counter(arr)
    a=[(k,v) for k,v in c.items()]
    a.sort(key=lambda x:-x[1])
    ans=[k for k,v in a]
    
    return ans
    
# 다른 사람의 풀이
def solution(s):
    answer = []

    # strip, split 혼용
    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
