cards = list(i for i in range(0, 21))
for _ in range(10):
    s, e = map(int, input().split())
    cards[s:e+1] = cards[e:s-1:-1]
    
print(' '.join(str(card) for card in cards[1:]))