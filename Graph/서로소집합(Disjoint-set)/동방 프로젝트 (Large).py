import sys
input=sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())
acts=[]
for _ in range(m):
    acts.append(list(map(int,input().rstrip().split())))
acts.sort(key=lambda x:x[0])

p=[i for i in range(n+1)]

def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def uni(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

merged_acts = []
for act in acts:
    # 첫 번째 원소인 경우 처리 
    if not merged_acts:
        merged_acts.append(act)
    else:
        # 마지막 원소 기준으로
        last = merged_acts[-1]
        # 현재 원소의 start가 마지막 원소의 end보다 작은 경우는 겹치는 방이 있다는 의미
        if act[0] < last[1]:
            # 두 구간의 end 중 최댓값을 사용하여 병합
            last[1] = max(last[1], act[1])
        else:
            # 그렇지 않으면 새로운 구간으로 추가
            merged_acts.append(act)

for s,e in merged_acts:
    for i in range(s,e):
        uni(i,i+1)

print(len(set(p[1:])))