def solution(s):
    answer = 0
    a, b = 0, 0
    first_char = ""
    for i in range(len(s)):
        if a == b:
            first_char = s[i]
            a, b = 0, 0
            answer += 1
        if s[i] == first_char:
            a += 1
        else:
            b += 1

    return answer