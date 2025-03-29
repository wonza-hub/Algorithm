def solution(arr1, arr2):
    a,b,c,d=len(arr1),len(arr1[0]),len(arr2),len(arr2[0])
    answer=[[0]*d for _ in range(a)]

    for i in range(a): # arr1의 행만큼 반복하며
        for j in range(d): # arr2의 열을 탐색
            tmp=0
            for k in range(c): # 그중, arr1의 열 또는 arr2의 행만큼 반복
                tmp+=arr1[i][k]*arr2[k][j]
            answer[i][j]=tmp
            
    return answer