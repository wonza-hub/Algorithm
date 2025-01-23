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