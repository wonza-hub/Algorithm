import sys
input=sys.stdin.readline

def solution(sa,sb):
    # 정렬을 통해 비교 처음부터 비교
    la=list(sa)
    la.sort()
    lb=list(sb)
    lb.sort()
    # 길이가 같은 경우에만 비교가 유의미함
    if len(la)!=len(lb):
        return False
    for i in range(len(la)):
        if la[i]!=lb[i]:
            return False

    return True

for _ in range(int(input().rstrip())):
    a,b=input().rstrip().split()
    if solution(a,b):
        print('Possible')
    else:
        print('Impossible')