def time_to_num(time):
    [h,m]=time.split(":")
    return 60*int(h)+int(m)

def num_to_time(num):
    h=str(num//60).zfill(2)
    m=str(num%60).zfill(2)
    return f'{h}:{m}'

def solution(video_len, pos, op_start, op_end, commands):
    cur=pos
    video_len=time_to_num(video_len)
    cur=time_to_num(cur)
    op_start=time_to_num(op_start)
    op_end=time_to_num(op_end)

    if op_start<=cur<=op_end:
        cur=op_end
    
    for com in commands:
        if com=='next':
            cur=min(cur+10,video_len)
        else:
            cur=max(cur-10,0)
            
        if op_start<=cur<=op_end:
            cur=op_end
    
    return num_to_time(cur)