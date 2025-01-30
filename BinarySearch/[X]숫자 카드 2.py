# 해쉬 풀이
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
others = list(map(int, input().split()))

card_dict = {} 

for num in cards:
    if num in card_dict:
        card_dict[num] += 1
    else:
        card_dict[num] = 1

for num in others:
    if num in card_dict:
        print(card_dict[num], end=' ')
    else:
        print(0, end=' ')

# 이진 탐색 풀이
from bisect import bisect_left,bisect_right

def find_lidx(v):
    return bisect_left(arr,v)
def find_ridx(v):
    return bisect_right(arr,v)

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
tarr=list(map(int,input().split()))

for t in tarr:
    left=find_lidx(t)
    right=find_ridx(t)
    print(right-left,end=" ")