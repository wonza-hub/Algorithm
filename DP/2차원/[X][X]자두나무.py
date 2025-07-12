t,w=map(int,input().split())
tree=[0]*(t+1)
arr=[[0]*(w+1) for _ in range(t+1)]

for i in range(1,t+1):
    tree[i]=int(input())

def where_jadu(idx):
    return 1 if idx%2==0 else 2

for j in range(w+1):
    for i in range(j,t+1):
        p=where_jadu(j)
        if j==0:
            if tree[i]==p:
                arr[i][j]=arr[i-1][j]+1
            else:
                arr[i][j]=arr[i-1][j]
        if tree[i]==p:
            arr[i][j]=max(arr[i-1][j-1]+1, arr[i-1][j]+1)
        else:
            arr[i][j]=max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[t]))

# 복습 풀이
import sys
input=sys.stdin.readline

t,w=map(int,input().rstrip().split())
tree=[0]*(t+1)
arr=[[0]*(w+1) for _ in range(t+1)]

for i in range(1,t+1):
    tree[i]=int(input().rstrip())

for j in range(w+1):
    for i in range(1,t+1):
        # 현재 자두 위치
        loc=1 if j%2==0 else 2
        if j==0:
            arr[i][0]+=arr[i-1][0]+int(loc==tree[i])
        else:
            arr[i][j]=max(arr[i-1][j-1],arr[i-1][j])+int(loc==tree[i])

print(max(arr[t]))

# 복습2 풀이
import sys
input=sys.stdin.readline

jadu=[0]
t,w=map(int,input().rstrip().split())
for _ in range(t):
    jadu.append(int(input().rstrip()))

arr=[[0]*(w+1) for _ in range(t+1)]

def jadu_loc(w):
    return 1 if w%2==0 else 2

for t in range(1,t+1):
    arr[t][0]=arr[t-1][0]+int(jadu_loc(0)==jadu[t])

arr[1][1]=int(jadu_loc(1)==jadu[1])
for t in range(2,t+1):
    for w in range(1,w+1):
        arr[t][w]=max(arr[t-1][w-1],arr[t-1][w])+int(jadu_loc(w)==jadu[t])

print(max(arr[t]))