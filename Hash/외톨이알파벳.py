from collections import defaultdict

def solution(input_string):
    ans = ''
    d = defaultdict(int)
    prev = None
    for cur in input_string:
        if cur != prev:
            d[cur] += 1
        prev = cur
    for [key, val] in d.items():
        if val >= 2:
            ans += key
    if len(ans) == 0:
        return "N"
    
    return "".join(sorted(ans))