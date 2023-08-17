# 해시(딕셔너리) 풀이
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items():
    if val == 1:
        print(key)
        break


# 세트로 풀이
# n = int(input())
# tmps = []
# words = []
# for _ in range(n):
#     tmp = input()
#     tmps.append(tmp)

# for _ in range(n-1):
#     word = input()
#     words.append(word)

# print(''.join(set(tmps)-set(words)))