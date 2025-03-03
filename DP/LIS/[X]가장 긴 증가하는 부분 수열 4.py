import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))
d=[1]*n
o=[[a] for a in arr]
s=o.copy()

for i in range(1,n):
    for j in range(0,i):
        if arr[i]>arr[j]:
            if d[i]<d[j]+1:
                d[i]=d[j]+1
                tmp=s[j]+o[i]
                if len(tmp)>len(s[i]):
                    s[i]=tmp

ans=max(d)
print(ans)
idx=d.index(ans)
print(*s[idx])

# 복습 풀이
import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))

d=[1]*n
ad=[[arr[0]]]


for i in range(1,n):
    ad.append([arr[i]])
    for j in range(i):
        if arr[i]>arr[j]:
            if d[i]<d[j]+1:
                ad.pop()
                ad.append(ad[j]+[arr[i]])
            d[i]=max(d[i],d[j]+1)

len_ans=max(d)
print(len_ans)
for a in ad:
    if len(a)==len_ans:
        print(' '.join(list(map(str,a))))
        break

