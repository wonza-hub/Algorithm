def solution(dartResult):
    arr=[]
    tmp='' # 숫자 담는 변수
    for result in dartResult:
        if result.isnumeric():
            tmp+=result
        elif result=='S':
            arr.append(int(tmp)**1)
            tmp=''
        elif result=='D':
            arr.append(int(tmp)**2)
            tmp=''
        elif result=='T':
            arr.append(int(tmp)**3)
            tmp=''
        elif result=='*':
            if len(arr)==1:
                arr[-1]=arr[-1]*2
            else:
                arr[-1]=arr[-1]*2
                arr[-2]=arr[-2]*2
        elif result=='#':
            arr[-1]=arr[-1]*(-1)
            
    return sum(arr)