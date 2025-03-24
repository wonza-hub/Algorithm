import sys
input=sys.stdin.readline

dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]

dice=[0]*6

def roll(com):
    a,b,c,d,e,f=dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    if com==1:
        dice[0],dice[2],dice[3],dice[5]=d,a,f,c
    elif com==2:
        dice[0],dice[2],dice[3],dice[5]=c,f,a,d
    elif com==3:
        dice[0],dice[1],dice[4],dice[5]=e,a,f,b
    elif com==4:
        dice[0],dice[1],dice[4],dice[5]=b,f,a,e

def solution():
    n,m,x,y,k=map(int,input().rstrip().split())
    arr=list(list(map(int,input().rstrip().split())) for _ in range(n))
    command=map(int,input().rstrip().split())

    for com in command:
        nx=x+dx[com]
        ny=y+dy[com]
        if 0<=nx<n and 0<=ny<m:
            x,y=nx,ny
            roll(com)
            if arr[x][y]==0:
                arr[x][y]=dice[5]
            else:
                dice[5]=arr[x][y]
                # 조건 유의: 칸에 쓰여 있는 수는 0이 된다.
                arr[x][y]=0
            print(dice[0])

solution()