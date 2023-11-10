card_dict = dict()

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
other = list(map(int, input().split()))

for key in other:
    card_dict[key] = 0
    
for num in nums:
    if num in card_dict:
        card_dict[num] = 1

for key in card_dict.keys():
    print(card_dict[key], end = " ")
        
            