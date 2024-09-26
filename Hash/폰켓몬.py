def solution(nums):
    dic = {}
    for n in nums:
        if n in dic:
            continue
        dic[n] = 0
    
    return min(len(dic), len(nums) // 2)