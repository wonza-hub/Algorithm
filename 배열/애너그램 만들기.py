import sys
input=sys.stdin.readline

la=list(input().rstrip())
lb=list(input().rstrip())
i=0
while i<len(la):
    if la[i] in lb:
        lb.remove(la[i])
        la.remove(la[i])
        i-=1
    i+=1

print(len(la)+len(lb))
