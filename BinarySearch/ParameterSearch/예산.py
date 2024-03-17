n = int(input())
budgets = list(map(int, (input().split())))
budget_prepared = int(input())

l, r = 0, max(budgets)
while l <= r:
    mid = (l + r) // 2
    sum = 0
    for budget in budgets:
        if budget > mid:
            sum += mid
        else:
            sum += budget
            
    if sum > budget_prepared:
        r = mid - 1
    else:
        l = mid + 1

print((l + r) // 2)

