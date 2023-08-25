n = input()
num = 0
cnt = 0

for x in n:
    if x.isdecimal():
        num = num * 10 + int(x)

for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1

print(cnt)
