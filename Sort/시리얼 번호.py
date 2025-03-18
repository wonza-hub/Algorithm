import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input().rstrip())):
    tmp=input().rstrip()
    a=len(tmp)
    b=sum([int(t) for t in list(tmp) if 48<=ord(t)<=57])
    arr.append((tmp,a,b))
arr.sort(key=lambda x:(x[1],x[2],x[0]))

for a in arr:
    print(a[0])