n, s = map(int, input().split())
seq = list(map(int, input().split()))
MAX_LEN = 100000

min_len = MAX_LEN
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += seq[end]
        end += 1
    if interval_sum >= s:
        min_len = min(min_len, end - start)
    interval_sum -= seq[start]

print(0 if min_len == MAX_LEN else min_len)