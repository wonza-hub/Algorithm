import sys
input=sys.stdin.readline

def recursion(si,sj,n):
    if n==1:
        return
    for i in range(si,si+n,n//3):
        for j in range(sj,sj+n,n//3):
            if i==si+n//3 and j==sj+n//3:
                for k in range(i,i+n//3):
                    for s in range(j,j+n//3):
                        arr[k][s]=' '
            else:
                recursion(i,j,n//3)

n=int(input().rstrip())
arr=[['*']*n for _ in range(n)]
recursion(0,0,n)
for row in arr:
    print(''.join(row))