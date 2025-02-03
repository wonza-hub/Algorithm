n=int(input())
d={}

for _ in range(n):
    name,st=input().split()
    if name in d:
        del d[name]
    else:
        d[name]=1

arr=list(d.keys())
arr.sort(reverse=True)
for a in arr:
    print(a)
