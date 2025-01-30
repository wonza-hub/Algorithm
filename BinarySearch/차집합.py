# set 풀이
na,nb=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
amb=a-b
amb=list(amb)
amb.sort()
if amb:
    print(len(amb))
    for a in amb:
        print(a,end=" ")
else:
    print(0)