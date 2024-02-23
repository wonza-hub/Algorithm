from collections import defaultdict

def solution(phone_book):
    d = defaultdict(int)
    phone_book.sort(key = lambda x: (len(x)))
    for num in phone_book:
        for i in range(len(num) - 1):
            if num[:i + 1] in d.keys():
                return False 
        d[num] = 1
        
    return True