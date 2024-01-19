def solution(command):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    x, y = 0, 0
    
    for c in command:
        if c == "G":
            x, y = x + dx[i % 4], y + dy[i % 4]
        if c == "B":
            x, y = x - dx[i % 4], y - dy[i % 4]
        if c == "R":
            i += 1
        if c == "L":
            i -= 1
            
    return [x, y]
        