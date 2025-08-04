import sys
input=sys.stdin.readline

s=input().rstrip()
z_cnt=s.count('0')
half_z_cnt=z_cnt//2
o_cnt=s.count('1')
half_o_cnt=o_cnt//2

tmp_z_cnt=0
ch=[1]*len(s)
for idx,i in enumerate(s):
    if z_cnt == half_z_cnt and o_cnt == half_o_cnt:
        break
    if i=='1':
        if o_cnt == half_o_cnt:
            continue
        o_cnt-=1
        ch[idx]=0
    if i=='0':
        if tmp_z_cnt==half_z_cnt:
            z_cnt-=1
            ch[idx] = 0
        else:
            tmp_z_cnt+=1
ans=''
for idx,c in enumerate(ch):
    if c:
        ans+=s[idx]
print(ans)