# 하노이 탑 (백준)
def hanoi(n,s,e,o):
    if n==0:
        return
    hanoi(n-1,s,o,e)
    print(s,e)
    hanoi(n-1,o,e,s)

n=int(input())
answer = []
print(2**n-1) # 이동 횟수 공식
if n <= 20:
    hanoi(n,1,3,2)

# 하노이의 탑 (프로그래머스)
def move_disk(s,e):
    answer.append([s,e])
    
def hanoi(n,s,e,o):
    if n==0:
        return
    hanoi(n-1,s,o,e)
    move_disk(s,e)
    hanoi(n-1,o,e,s)
        
    
def solution(n):
    global answer
    answer = []
    hanoi(n,1,3,2)
    
    return answer
