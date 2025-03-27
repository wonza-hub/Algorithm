# 다른 사람의 풀이
ipv6=input()
ipv6=ipv6.split(':')

# 양 끝에 빈 문자열이 있는 경우
if ipv6[0]=='':
    ipv6=ipv6[1:]
if ipv6[-1]=='':
    ipv6=ipv6[:-1]

result = ''
for i in ipv6:
    if i=='':
        result += '0000:'*(8-len(ipv6)+1)
    else:
        result += i.zfill(4)+':'

print(result[:-1])