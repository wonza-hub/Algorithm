from collections import Counter
import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
arr=[list(input().rstrip()) for _ in range(n)]
ans=''
hd=0
for j in range(m):
    tmp=[]
    for i in range(n):
        tmp.append(arr[i][j])
    l=len(tmp)
    # 개수가 큰 순서대로 배열로 반환
    # 예시 1) [('A', 5), ('T', 1)]
    # 예시 2) [('A', 1), ('C', 1), ('G', 1), ('T', 1)]
    c=Counter(tmp).most_common()
    print(c)
    # 정렬기준: 개수순, 뉴클레오티드 사전순
    c.sort(key=lambda x:(-x[1],x[0]))
    hd+=l-c[0][1]
    ans+=c[0][0]

print(ans)
print(hd)
