def solution(n, s):
    return [-1] if s//n==0 else [s//n]*(n-s%n)+[s//n+1]*(s%n)