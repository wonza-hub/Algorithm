key_pad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
lr=['*','#']

d={}
for i in range(len(key_pad)):
    for j in range(3):
        d[key_pad[i][j]]=[i,j]
    
def calc_dis(a,b):
    return abs(d[a][0]-d[b][0])+abs(d[a][1]-d[b][1])


def solution(numbers, hand):
    ans=''
    for num in numbers:
        if num in [1,4,7]:
            lr[0]=num
            ans+='L'
        elif num in [3,6,9]:
            lr[1]=num
            ans+='R'
        else:
            left_d=calc_dis(num,lr[0])
            right_d=calc_dis(num,lr[1])
            if left_d<right_d:
                lr[0]=num
                ans+='L'
            elif left_d>right_d:
                lr[1]=num
                ans+='R'
            else:
                if hand=='right':
                    lr[1]=num
                    ans+='R'
                else:
                    lr[0]=num
                    ans+='L'
    
    return ans