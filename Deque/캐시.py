from collections import defaultdict

def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5
    t=0
    ref_t=0
    cache=defaultdict(int)
    for c in cities:
        ref_t+=1
        c=c.upper()
        if c in cache:
            cache[c]=ref_t
            t+=1
        else:
            if len(cache)==cacheSize:
                a=list(cache.items())
                a.sort(key=lambda x:x[1])
                del cache[a[0][0]]
            cache[c]=ref_t
            t+=5

    return t

# 다른 사람의 풀이
def solution(cacheSize, cities):
    import collections
    # maxlen 활용
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time