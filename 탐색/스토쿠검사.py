def sdoku(puz):
    # 가로, 세로
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            if ch1[puz[i][j]] != 1 and ch2[puz[j][i]] != 1:
                ch1[puz[i][j]] = 1
                ch2[puz[j][i]] = 1
            else:
                return False
    # 3x3 영역
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    if ch3[puz[i * 3 + k][j * 3 + s]] != 1:
                        ch3[puz[i * 3 + k][j * 3 + s]] = 1
                    else:
                        return False
    return True
    
puz = [list(map(int, input().split())) for _ in range(9)]
if sdoku(puz):
    print("YES")
else:
    print("NO")
            