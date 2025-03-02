from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def translate(route):
    op,n=route.split(' ')
    i=0
    if op=='E':
        i=1         
    elif op=='S':
        i=2
    elif op=='W':
        i=3
    elif op=='N':
        i=0
    
    return [i,int(n)]
    
def solution(park, routes):
    park=[list(p) for p in park]
    q=deque()
    h,w=len(park),len(park[0])
    x,y=0,0
    for i in range(h):
        for j in range(w):
            if park[i][j]=='S':
                x,y=i,j
                break
                
    for route in routes:
        i,n=translate(route)
        if 0<=x+dx[i]*n<h and 0<=y+dy[i]*n<w:
            tx,ty=x,y
            while n>0:
                n-=1
                tx+=dx[i]
                ty+=dy[i]
                if park[tx][ty]=='X':
                    break
            else:
                x=tx
                y=ty
            
    return [x,y]