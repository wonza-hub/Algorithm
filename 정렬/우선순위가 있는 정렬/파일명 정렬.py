def solution(files):
    ans=[]
    arr=[]
    for i,file in enumerate(files):
        flag=False
        cnt=0
        num_s=0
        tail_s=None 
        for idx,ele in enumerate(file):
            if ele.isdecimal() and not flag:
                flag=True
                cnt+=1
                num_s=idx
                continue
            if flag and ele.isdecimal():
                if cnt==6:
                    tail_s=idx
                    break
                cnt+=1
            if flag and not ele.isdecimal():
                tail_s=idx
                break
    
        head=file[:num_s]
        number=file[num_s:tail_s] if tail_s is not None else file[num_s:]
        number='0' if set(number)=={'0'} else number.lstrip('0')
        
        arr.append([i,head.upper(),int(number)])
    arr.sort(key=lambda x:(x[1],x[2],x[0]))
        
    for i,_,_ in arr:
        ans.append(files[i])
        
    return ans