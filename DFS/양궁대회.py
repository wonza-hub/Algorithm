# 오답 풀이 (동점 차일 때 낮은 점수 비교 누락)
def dfs(info,l,cnt,어피치점수,라이언점수,n,arr):
    global max_diff,answer
    if l==10:
        if cnt>n:
            return
        if 어피치점수<라이언점수:
            if cnt<n:
                arr[-1]=n-cnt
            if max_diff<=라이언점수-어피치점수:
                max_diff=라이언점수-어피치점수
                answer=arr
        return
    dfs(info,l+1,cnt+info[l+1]+1,어피치점수,라이언점수+10-(l+1),n,arr+[info[l+1]+1])
    dfs(info,l+1,cnt,어피치점수+10-(l+1) if info[l+1]>0 else 어피치점수,라이언점수,n,arr+[0])
    
def solution(n, info):
    global max_diff,answer
    answer = []
    max_diff=0
    dfs(info,-1,0,0,0,n,[])    
    return [-1] if answer==[] else answer

# 정답 풀이
def dfs(info, l, cnt, 어피치점수, 라이언점수, n, arr):
    global max_diff, answer
    
    if l == 10:
        if cnt > n:
            return
        if 어피치점수 < 라이언점수:
            if cnt < n:
                arr[-1] = n - cnt  # 남은 화살 0점에 배정
            diff = 라이언점수 - 어피치점수
            if diff > max_diff:
                max_diff = diff
                answer = arr[:]
            elif diff == max_diff:  # ✅ 수정 1: 동점 차일 때 낮은 점수 비교
                for i in range(10, -1, -1):
                    if arr[i] != answer[i]:
                        if arr[i] > answer[i]:
                            answer = arr[:]
                        break
        return
    
    # 다음 레벨 인덱스
    next_l = l + 1
    
    # 해당 점수를 가져오는 경우
    dfs(info, next_l, cnt + info[next_l] + 1,
        어피치점수, 라이언점수 + (10 - next_l),
        n, arr + [info[next_l] + 1])
    
    # 해당 점수를 포기하는 경우
    dfs(info, next_l, cnt,
        어피치점수 + (10 - next_l if info[next_l] > 0 else 0),
        라이언점수,
        n, arr + [0])

def solution(n, info):
    global max_diff, answer
    answer = []
    max_diff = 0
    dfs(info, -1, 0, 0, 0, n, [])
    return [-1] if answer == [] else answer