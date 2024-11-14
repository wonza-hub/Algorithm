import heapq as hq

def ttm(bt):
    st,et=bt
    st=st.split(':')
    et=et.split(':')
    s=int(st[0])*60+int(st[1])
    e=int(et[0])*60+int(et[1])+10
    return [s,e]

def solution(book_time):
    arr=[]
    answer = 0
    for bt in book_time:
        s,e=ttm(bt)
        arr.append([s,e])
    arr.sort(key=lambda x:x[0])
    ends=[]
    
    for s,e in arr:
        if ends and s>=ends[0]:
            hq.heappop(ends)
        hq.heappush(ends,e)
    
    return len(ends)