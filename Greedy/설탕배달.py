n = int(input())
sum = 0
s_bag = 0
b_bag = 0

while sum <= n:
    if (n - sum) % 5 == 0:
        b_bag = (n - sum) // 5
        print(s_bag + b_bag)
        break
    sum += 3
    s_bag +=1   

else:    
    print(-1)

# 다른 사람 풀이
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break
    sugar -= 3
    bag += 1
    
