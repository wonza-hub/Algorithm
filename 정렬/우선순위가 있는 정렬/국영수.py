import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input().rstrip())):
    n,a,b,c=input().rstrip().split()
    arr.append([n,int(a),int(b),int(c)])
arr.sort(key=lambda x:[-x[1],x[2],-x[3],x[0]])
for n,a,b,c in arr:
    print(n)