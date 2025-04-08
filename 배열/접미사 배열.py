import sys
input=sys.stdin.readline

s=input().rstrip()
arr=[s[i:] for i in range(len(s))]
arr.sort()
for a in arr:
    print(a)