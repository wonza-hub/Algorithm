n = int(input())
seq_rev = list(map(int, input().split()))
seq = [0] * n
for (num, cnt) in enumerate(seq_rev, 1):
    tmp = -1
    for i in range(0, len(seq)):
        if seq[i] == 0:
            tmp += 1
        if tmp == cnt:
            seq[i] = num
            break
for s in seq:
    print(s, end=' ')