from itertools import product

def solution(users, emoticons):
    case = []
    for cwr in product([10, 20, 30, 40], repeat = len(emoticons)):
        case.append(cwr)
    res = [[0, 0] for _ in range(len(case))]    

    for user in users:
        for i in range(len(case)):
            cost = 0
            for j in range(len(case[i])):
                if case[i][j] >= user[0]:
                    cost += int(emoticons[j] * (100 - case[i][j]) / 100)
            if cost >= user[1]:
                res[i][0] += 1
            else:
                res[i][1] += cost
    res.sort(key = lambda x: (-x[0], -x[1]))
    
    return res[0]