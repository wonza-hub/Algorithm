def v(x, OorX):
    if x == n:
        print(OorX)
        return
    v(x + 1, OorX + 'O')
    v(x + 1, OorX + 'X')


n = int(input())
v(0, "")
    