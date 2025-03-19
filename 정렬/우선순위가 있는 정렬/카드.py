from collections import defaultdict
import sys
input=sys.stdin.readline

dic=defaultdict(int)
for _ in range(int(input().rstrip())):
    dic[int(input().rstrip())]+=1

a=list(set(dic.items()))
a.sort(key=lambda x:(-x[1],x[0]))

print(a[0][0])