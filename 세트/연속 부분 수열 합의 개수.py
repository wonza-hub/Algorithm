def solution(elements):
    s=set()
    l=len(elements)
    elements=elements*2
    for i in range(1,l+1):
        for j in range(l):
            s.add(sum(elements[j:j+i]))
    
    return len(s)