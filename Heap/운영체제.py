import heapq as hq

def solution(program):
    answer = [0 for _ in range(11)]
    # 시작시간이 빠른 프로그램, 같으면 우선순위가 큰 것을 먼저 정렬()
    program.sort(key = lambda x : (x[1],x[0]))
    
    # 대기중 프로그램
    waiting_q = []
    hq.heapify(waiting_q)
    time = 0

    def call_program():
        # 남은 프로그램도 있고, 맨 앞의 프로그램의 호출시간이 현 시각보다 앞에 있다면
        while program and program[0][1] <= time:
            # 프로그램을 꺼내서 대기 순번에 넣어줌
            hq.heappush(waiting_q, program.pop(0))

    # 대기중 또는 실행 예정인 프로그램이 없을때까지
    while program or waiting_q:
        # 프로그램은 있는데 당장 실행할 프로그램이 없다면(대기중이 없다면)
        if program and not waiting_q:
            time = program[0][1]
            call_program()
        # 당장 실행 가능한 프로그램을 하나 꺼내어 실행
        exec = hq.heappop(waiting_q)
        # 꺼낸 프로그램 대기시간 체크 (현재시각 - 원래 실행됐어야 할 시작시각)
        answer[exec[0]] += (time - exec[1])
        # 꺼낸 프로그램 동작을 끝냄 (시간이 흐름)
        time += exec[2]
        call_program()

        
    #프로그램 -> 대기 -> 동작 (시간의 흐름)
    answer[0] = time
    return answer