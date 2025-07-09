import sys
input=sys.stdin.readline

start=input().rstrip()
target=input().rstrip()

ans=0
def recursive(t):
    global ans 
    if len(start)==len(t):
        if start==t:
            ans=1
        return
    if t[-1]=='A':
        recursive(t[:-1])
    if t[0]=='B':
        recursive(t[:0:-1])

recursive(target)
print(ans)
    


