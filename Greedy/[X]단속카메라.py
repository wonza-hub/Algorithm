def solution(routes):
    routes.sort(key = lambda x : (x[1], x[0]))
    
    end = routes[0][1]
    ans = 1
    
    for i in range(len(routes) - 1):
        if end < routes[i + 1][0]:
            end = routes[i + 1][1]
            ans += 1
            
    return ans

# 복습 풀이
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치

def solution(routes):
    answer = 1
    routes.sort(key = lambda x: (x[1], x[0]))
    e = routes[0][1]
    
    for i in range(1, len(routes)):
        if routes[i][0] > e:
            answer += 1
            e = routes[i][1]
    
    return answer