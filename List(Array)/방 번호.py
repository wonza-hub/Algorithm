import math
import sys
input=sys.stdin.readline

ch=[0]*10
n=int(input().rstrip())

while n!=0:
    ch[n%10]+=1
    n//=10

if not ch[6]:
    ch[9]=math.ceil(ch[9]/2)
elif not ch[9]:
    ch[6]=math.ceil(ch[6]/2)
elif ch[6] and ch[9]:
    s=ch[6]+ch[9]
    if s%2==0:
        ch[6],ch[9]=s//2,s//2
    else:
        ch[6],ch[9]=s//2+1,s//2+1

print(max(ch))