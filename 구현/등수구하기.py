n, new_score, p = map(int, input().split())
ans = -1

if n > 0:
    existing_scores = list(map(int, input().split()))
    scores = [int(10e9)] + existing_scores + [-1] * (p - n)
    for rank, score in enumerate(scores):
        if new_score <= scores[-1]:
            break
        elif score > new_score:
            continue
        else:
            ans = rank
            break
else:
    ans = 1
    
print(ans)

        