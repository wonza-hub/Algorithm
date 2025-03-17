from collections import defaultdict
import sys
input=sys.stdin.readline

for _ in range(int(input().rstrip())):
    dic=defaultdict(list)
    for _ in range(int(input().rstrip())):
        v,k=input().rstrip().split()
        dic[k].append(v)
    ans=1
    tmp=[len(dic[k])+1 for k in dic.keys()]
    for t in tmp:
        ans*=t
    ans-=1
    print(ans)