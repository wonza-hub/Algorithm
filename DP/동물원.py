import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)

d[0] = 1
d[1] = 3

for i in range(2, n + 1):
    d[i] = (d[i - 1] * 2 + d[i - 2]) % 9901

print(d[n])