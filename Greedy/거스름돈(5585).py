PAID = 1000
EXCHANGEABLE_YEN = [500, 100, 50, 10, 5, 1]
cost = int(input())
exchange = PAID - cost
ans = 0

for yen in EXCHANGEABLE_YEN:
    while exchange // yen != 0:
        exchange -= yen
        ans += 1
print(ans)