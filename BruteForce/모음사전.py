from itertools import product

def solution(word):
    a = []
    for i in range(1, 6):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            a.append(''.join(p))
    a.sort()
    
    return a.index(word) + 1