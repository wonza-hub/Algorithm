from collections import Counter
import sys
input=sys.stdin.readline

r,c,k=map(int,input().rstrip().split())
arr=[list(map(int,input().rstrip().split())) for _ in range(3)]

def sort_arr(arr):
    max_len=0
    tmp_arr=[]
    for a in arr:
        a=[num for num in a if num!=0]
        ca=sorted(Counter(a).items(),key=lambda x:(x[1],x[0]))
        tmp=[]
        for x,y in ca:
            tmp.extend([x,y])
        max_len=max(max_len,len(tmp))
        tmp_arr.append(tmp)
        
    for ta in tmp_arr:
        ta+=[0]*(max_len-len(ta))
    
    return tmp_arr

def rotate_left(arr):
    n,m=len(arr),len(arr[0])
    tmp_arr=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp_arr[m-j-1][i]=arr[i][j]

    return tmp_arr

def rotate_right(arr):
    n,m=len(arr),len(arr[0])
    tmp_arr=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp_arr[j][n-i-1]=arr[i][j]

    return tmp_arr

time=0
while time<=100:
    n,m=len(arr),len(arr[0])
    if 0<=r-1<n and 0<=c-1<m:
        if arr[r-1][c-1]==k:
            print(time)
            break

    if n>=m:
        arr=sort_arr(arr)
    else:
        arr=rotate_left(arr)
        arr=sort_arr(arr)
        arr=rotate_right(arr)
    time+=1
else:
    print(-1)