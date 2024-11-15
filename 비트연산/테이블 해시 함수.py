def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    answer=0
    for r in range(row_begin,row_end+1):
        if r==row_begin:
            answer=sum([i%r for i in data[r-1]])
            continue
        answer=answer^sum([i%r for i in data[r-1]])
        
    return answer