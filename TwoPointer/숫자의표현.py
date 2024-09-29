def solution(n):
    a = [i for i in range(1, n + 1)]
    answer, sum, s, e = 0, 1, 0 , 0
    while True:
        if sum == n:
            answer += 1
            e += 1
            if e == len(a):
                break
            sum += a[e]
        elif sum > n:
            sum -= a[s]
            s += 1
        else:
            e += 1
            if e == len(a):
                break
            sum += a[e]
    return answer