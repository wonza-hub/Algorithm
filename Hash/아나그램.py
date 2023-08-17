# 간결한 풀이
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print('NO')
            break
    else:
        print('NO')
        break

else:
    print('YES')

# 내 풀이 
# import sys
# str_1 = input()
# keys = list(str_1)
# default_value = 0
# d = dict.fromkeys(keys, default_value)
# str_2 = input()
# ans = 'YES'

# for char in str_1:
#     d[char] += 1
# for char in str_2:
#     if char in d:
#         d[char] -= 1
#     else:
#         print('NO')
#         break
# for key, val in d.items():
#     if val != 0:
#         print('NO')
#         break
# else:
#     print('YES')
    