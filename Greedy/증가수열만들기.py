# 생 구현에 가까움
# from collections import deque

# n = int(input())
# seq = list(map(int, input().split()))
# seq = deque(seq)
# last = 0
# ans_len = 0
# ans_LR = ''
# while seq:
#     l = seq[0]
#     r = seq[-1]
#     if last < l and last < r:
#         if l <= r:
#             seq.popleft()
#             ans_LR += 'L'
#             last = l
#         else:
#             seq.pop()
#             ans_LR += 'R'
#             last = r
#         ans_len += 1
#     elif last < l:
#         seq.popleft()
#         ans_LR += 'L'
#         last = l
#     elif last < r:
#         seq.pop()
#         ans_LR += 'R'
#         last = r
#     else:
#         break
        
# print(len(ans_LR))
# print(ans_LR)

# 그리디 다운 방식
n = int(input())
seq = list(map(int, input().split()))

L = 0
R = n - 1
last = 0
ans = ""
tmp = []

while L <= R:
    if seq[L] > last:
        tmp.append((seq[L], 'L'))
    if seq[R] > last:
        tmp.append((seq[R], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        ans += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            L += 1
        else:
            R -= 1
    tmp.clear()
    
print(len(ans))
print(ans)