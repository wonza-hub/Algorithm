def solution(numlist, n):
    return sorted(numlist,key=lambda num:[abs(num-n),-num])