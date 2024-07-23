def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = list('0' + bin(num)[2:])
        last_zero_idx = ''.join(bin_num).rfind('0')
        bin_num[last_zero_idx] = '1'
        # 홀수인 경우 추가 작업 수행
        if num % 2 == 1:
            bin_num[last_zero_idx + 1] = '0'
        
        answer.append(int(''.join(bin_num), 2))
        
    return answer