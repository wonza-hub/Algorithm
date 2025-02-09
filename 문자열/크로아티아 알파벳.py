import sys
input=sys.stdin.readline

alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input().rstrip()
for al in alpha:
    s=s.replace(al,'#')
print(len(s))


