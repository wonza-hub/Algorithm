def solution(dots):
    if inclination(dots[0], dots[1]) == inclination(dots[2], dots[3]):
        return 1
    if inclination(dots[0], dots[2]) == inclination(dots[1], dots[3]):
        return 1
    if inclination(dots[0], dots[3]) == inclination(dots[1], dots[2]):
        return 1
    return 0

def inclination(dot1, dot2):
    return (dot1[0] - dot2[0]) / (dot1[1] - dot2[1])