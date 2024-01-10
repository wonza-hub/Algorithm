x, y, z = 1, 1, 1
year = 1
E_CYCLE, S_CYCLE, M_CYCLE = 15, 28, 19

E, S, M = map(int, input().split())

while True:
    if ((year-E) % E_CYCLE == 0) and ((year-S) % S_CYCLE == 0) and ((year-M) % M_CYCLE == 0):
        break
    year += 1
    
print(year)    