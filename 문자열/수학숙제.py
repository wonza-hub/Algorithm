import sys
input=sys.stdin.readline

n=int(input().rstrip())
ans=[]

def solution(string):
    res=[]
    tmp=''
    for s in string:
        if s.isdigit():
            tmp+=s
        else:
            if tmp:
                res.append(tmp)
            tmp=''

    return list(map(int,res))

for _ in range(n):
    string=input()
    res=solution(string)
    ans.extend(res)

ans.sort()
for a in ans:
    print(a)