from collections import Counter

def solution(topping):
    answer = 0
    a,b=Counter(topping[:1]),Counter(topping[1:])
    for i in range(1,len(topping)-1):
        a[topping[i]]+=1
        b[topping[i]]-=1
        if b[topping[i]]==0:
            del(b[topping[i]])
        if len(a)==len(b):
            answer+=1

    return answer