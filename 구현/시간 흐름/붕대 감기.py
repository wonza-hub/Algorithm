# 체력 0이하 -1
from collections import deque

class Character:
    def __init__(self,체력):
        self.체력=체력
        self.최대체력=체력
    
    def 붕대감기(self,x):
        self.체력=min(self.체력+x,self.최대체력)
        
    def 추가회복(self,y):
        self.체력=min(self.체력+y,self.최대체력)
        
    def 공격받음(self,z):
        self.체력=max(self.체력-z,0)
    
def solution(bandage, health, attacks):
    answer=0
    t,x,y=bandage
    캐릭터=Character(health)
    seq=0
    attacks.sort(key=lambda x:x[0])
    attacks=deque(attacks)
    
    cur_time=0
    while attacks:
        cur_time+=1
        if cur_time==attacks[0][0]:
            공격시간,피해량=attacks.popleft()
            캐릭터.공격받음(피해량)
            if 캐릭터.체력==0:
                answer=-1
                break
            seq=0
        else:
            캐릭터.붕대감기(x)
            seq+=1
            if seq==t:
                캐릭터.추가회복(y)
                seq=0
    else:
        answer=캐릭터.체력
    
    return answer