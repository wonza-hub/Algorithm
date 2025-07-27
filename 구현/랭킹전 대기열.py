import sys
input=sys.stdin.readline

rooms=[]

def search(lv):
    global m
    if rooms==[]:
        return -1
    for i in range(len(rooms)):
        if len(rooms[i])==m:
            continue
        if rooms[i][0][0]-10<=lv<=rooms[i][0][0]+10:
            return i
    return -1


def sol(l,n):
    lv=int(l)
    room_num=search(lv)
    if room_num==-1:
        rooms.append([(lv,n)])
    else:
        rooms[room_num].append((lv,n))


p,m=map(int,input().rstrip().split())
for _ in range(p):
    l,n=input().rstrip().split()
    sol(l,n)

for r in rooms:
    if len(r)==m:
        print('Started!')
    else:
        print('Waiting!')
    r.sort(key=lambda x:x[1])
    for l,n in r:
        print(l,n)