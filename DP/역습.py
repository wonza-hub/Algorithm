def solution(a, b, ap, ad, bp, bd):
    for i in range(1, n):
        a[i] = min(a[i - 1] + ad[i - 1], b[i - 1] + bp[i - 1])
        b[i] = min(b[i - 1] + bd[i - 1], a[i - 1] + ap[i - 1])
    

t = int(input())
for _ in range(t):
    n, l1, l2, s1, s2 = map(int, input().split())
    a = [0] * n
    b = [0] * n
    a[0] = l1
    b[0] = l2
    ap = list(map(int, input().split()))
    ad = list(map(int, input().split()))
    bp = list(map(int, input().split()))
    bd = list(map(int, input().split()))
    solution(a, b, ap, ad, bp, bd)
    answer = min(a[n - 1] + s1, b[n - 1] + s2)
    print(answer)