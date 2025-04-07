import sys
input=sys.stdin.readline
from collections import deque


def solution(arr,p):
    q=deque(arr)
    r_flag=False

    for op in p:
        # 실제 reverse 연산을 수행하지 않고 플래그 값만 변경
        if op=='R':
            r_flag=not r_flag
        elif op=='D':
            if len(q)==0:
                return 'error'
            # 플래그 값에 따라 데크 앞이나 뒤에서 pop 연산 수행
            if not r_flag:
                q.popleft()
            else:
                q.pop()
    if r_flag:
            q.reverse()

    return list(q)

for _ in range(int(input().rstrip())):
    p=input().rstrip()
    n=int(input().rstrip())
    arr=input().rstrip()
    if p.count('D')>n:
        print('error')
        continue
    
    arr=arr[1:-1].split(',')

    ans=solution(arr,p)
    if ans=='error':
        print(ans)
    else:
        print('['+','.join(ans)+']')