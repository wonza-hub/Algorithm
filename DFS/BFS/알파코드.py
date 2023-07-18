code_num = list(map(int, input()))
end = len(code_num)
code_num.append(-1)
list = []
cnt = 0
ans = ''

def dfs(l):
    global cnt
    if l == end:
        cnt += 1
        result = ''.join(chr(num + 64) for num in list)
        print(result)
    else:
        for i in range(1, 27):
            if i == code_num[l]:
                list.append(i)
                dfs(l + 1)
                list.pop()
            elif i >= 10 and i // 10 == code_num[l] and i % 10 == code_num[l + 1]:
                    list.append(i)
                    dfs(l + 2)
                    list.pop()

dfs(0)
print(cnt)       