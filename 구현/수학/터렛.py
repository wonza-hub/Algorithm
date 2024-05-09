import math

def calcdis(x1, y1,x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    
def solution(x1, y1, r1, x2, y2, r2):
    d = calcdis(x1, y1,x2, y2)
    if d == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    if r1 >= r2:
        s, l = r2, r1
    elif r1 < r2:
        s, l = r1, r2
    if s + l < d or l - s > d:
        return 0
    if s + l == d or l - s == d:
        return 1
    if l - s < d < s + l:
        return 2
    
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    ans = solution(x1, y1, r1, x2, y2, r2)
    print(ans)