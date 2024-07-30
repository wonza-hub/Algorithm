def dfs(cards, idx, cnt, ch):
    global arr
    if ch[idx]:
        arr.append(cnt)
        return
    ch[idx] = 1
    dfs(cards, cards[idx], cnt + 1, ch)

def solution(cards):
    global arr
    answer = 0
    cards = [0] + cards
    arr = []
    ch = [0] * len(cards)
    for idx in range(1, len(cards)):
        if ch[idx]:
            continue
        cnt = 0
        dfs(cards, idx, cnt, ch)
    arr.sort(reverse=True)
    
    return 0 if len(arr) == 1 else arr[0] * arr[1]
