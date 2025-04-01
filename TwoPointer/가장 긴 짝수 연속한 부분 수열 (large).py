import sys
input=sys.stdin.readline

n,k=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))

ans,odd,even=0,0,0
s,e=0,0

def is_odd(idx):
    return True if arr[idx]%2!=0 else False

# e 포인터를 x(while 반복문 횟수)칸 뒤로 이동
def forward(odd,even):
    global ans,e
    while odd<=k and e<n:
        if is_odd(e):
            odd+=1
        else:
            even+=1

        e+=1

    return [odd,even]

# s 포인터를 한 칸 뒤로 이동
for s in range(n):
    odd,even=forward(odd,even)
    ans=max(ans,even)

    if is_odd(s):
        odd-=1
    else:
        even-=1
        
print(ans)
    