dx=[-1,0,1,0]
dy=[0,1,0,-1]

def 거리두기(places,x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        # EARLY RETURN: 본인 상하좌우에 응시자 있는 경우
        if places[nx][ny]=='P':
            return False
        # EARLY RETURN: 상하좌우 빈테이블인 경우
        if places[nx][ny]=='O':
            # 빈테이블의 상하좌우 확인 (본인 제외)
            for j in range(4):
                nnx=nx+dx[j]
                nny=ny+dy[j]
                # 본인인 경우
                if nnx==x and nny==y:
                    continue
                # 응시자인 경우
                if places[nnx][nny]=='P':
                    return False
    # 거리두기 한 경우
    return True
    
    
def solution(places):
    answer = []
    for place in places:
        p_place=[[0]*7]+[list("0"+p+"0") for p in place]+[[0]*7]
        res=1
        flag=False
        for i in range(1,6):
            for j in range(1,6):
                if p_place[i][j]=='P':
                    거리두기여부=거리두기(p_place,i,j)
                    if 거리두기여부==False:
                        res=0
                        flag=True
                        break
            if flag==True:
                break
        answer.append(res)        
        
    return answer