# 입차 후 출차된 내역 없다면, 23:59 출차로 간주
# 누적시간 기본 시간 이하: 기본 요금
# 기본 시간 초과: 기본 요금 + 단위 시간(단위 시간으로 나누어 떨어지지 않으면 올림) * 단위 요금
# 출력: 차량 번호 작은 순, 청구 주차 요금 정수 배열
from collections import defaultdict
import math

입차=defaultdict(list)
출차=defaultdict(list)

def calc_time(s,e):
    s_m,e_m=s.split(':'),e.split(':')
    return 60*int(e_m[0])+int(e_m[1])-(60*int(s_m[0])+int(s_m[1]))
    
def calc_fee(누적시간,기본시간,기본요금,단위시간,초과요금):
    if 누적시간<=기본시간:
        return 기본요금
    초과시간=누적시간-기본시간
    return 기본요금+math.ceil(초과시간/단위시간)*초과요금
    
def solution(fees, records):
    기본시간,기본요금,단위시간,초과요금=fees
    for r in records:
        time,num,io=r.split(' ')
        if io=='IN':
            입차[num].append(time) 
        else:
            출차[num].append(time) 
            
    arr=[]
    for num,times in 입차.items():
        누적시간=0
        for i,time in enumerate(times):
            if 출차[num]:
                if len(times)!=len(출차[num]):
                    출차[num].append('23:59')
                누적시간+=calc_time(time,출차[num][i])
                
                # if 출차[num][i]:
                #     t=calc_time(time,출차[num][i])
                # else:
                #     t=calc_time(time,"23:59")
            else:
                누적시간+=calc_time(time,"23:59")
    
        fee=calc_fee(누적시간,기본시간,기본요금,단위시간,초과요금)
        arr.append([num,fee])
    arr.sort(key=lambda x:int(x[0]))
    
    return [x[1] for x in arr]