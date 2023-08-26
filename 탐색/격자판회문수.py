grid = [list(map(int, input().split())) for _ in range(7)]
ans = 0

for i in range(7):
    row = []
    col = []
    for j in range(7):
        row.append(grid[i][j])
        col.append(grid[j][i])
    for k in range(3):
        tmp_row = row[k:k + 5]
        if tmp_row == tmp_row[::-1]:
            ans += 1
    for s in range(3):
        tmp_col = col[s:s + 5]
        if tmp_col == tmp_col[::-1]:
            ans += 1

print(ans)
        
# 간결한 풀이
grid = [list(map(int, input().split())) for _ in range(7)]
ans = 0

for i in range(3):
    for j in range(7):
        tmp = grid[j][i:i + 5]
        if tmp == tmp[::-1]:
            ans += 1
        for k in range(2):
            if grid[i + k][j] != grid[i + 5 - k - 1][j]:
                break
            else:
                ans += 1

print(ans)
        
    
            
    
            