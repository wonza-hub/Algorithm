dict = {}
dict['zero'] = '0'
dict['one'] = '1'
dict['two'] = '2'
dict['three'] = '3'
dict['four'] = '4'
dict['five'] = '5'
dict['six'] = '6'
dict['seven'] = '7'
dict['eight'] = '8'
dict['nine'] = '9'

def solution(s):
    answer = ''
    tmp = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            tmp += char
            if tmp in dict:
                answer += dict[tmp]
                tmp = ''
    
    return int(answer)