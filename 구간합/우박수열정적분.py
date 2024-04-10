def dfs(l, k, arr):
    if k == 1:
        arr.append((l, k))
        return
    if k > 1:
        if k % 2 == 0:
            arr.append((l, k))
            dfs(l + 1, k / 2, arr)
        if k % 2 == 1:
            arr.append((l, k))
            dfs(l + 1, k * 3 + 1, arr)            
    
def solution(k, ranges):
    answer = []
    arr = []
    dfs(0, k, arr)
    n = len(arr) - 1
    sum = 0
    prefix_sum = [0]
    for i in range(1, len(arr)):
        sum += (arr[i][1] + arr[i - 1][1]) / 2
        prefix_sum.append(sum)
    
    for r in ranges:
        a, b = r
        k = b + n
        if a > k:
            answer.append(-1)
            continue
        answer.append(prefix_sum[k] - prefix_sum[a])
    
    return answer