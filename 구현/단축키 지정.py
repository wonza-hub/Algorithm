import sys
input=sys.stdin.readline

def check_first(arr):
    global sc
    for i in range(len(arr)):
        if arr[i][0].upper() in sc:
            continue
        else:
            sc.append(arr[i][0].upper())
            return (i,0)
    return (None,None)

def check_all(arr):
    global sc
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].upper() in sc:
                continue
            else:
                sc.append(arr[i][j].upper())
                return (i,j)
    return (None,None)

def search(arr):
    i1, i2 = check_first(arr)
    if i1 != None and i2 != None:
        return (i1,i2)
    i3,i4 = check_all(arr)
    if i3 != None and i4 != None:
        return (i3,i4)
    return (None,None)

def sol(str):
    ans=''
    tmp = str.split(' ')
    a,b=search(tmp)
    if a==None and b==None:
        ans=str
    else:
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if i==a and j==b:
                    ans+=f'[{tmp[i][j]}]'
                else:
                    ans+=tmp[i][j]
            ans+=' '
    return ans

sc=[]
for _ in range(int(input().rstrip())):
    opt=input().rstrip()
    ans=sol(opt)
    print(ans)

# 다른 사람의 풀이
# 출처: https://itstorytelling.tistory.com/110 [꾸준히 공부:티스토리]
# 인덱스를 반환하지 않고, 배열 자체를 수정하고 불리언을 반환하는 방식으로 구현
def first_rule(words):
    for i in range(len(words)):
        if words[i][0].lower() not in shortcut_key:
            shortcut_key.add(words[i][0].lower())
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            return True


# 단어 두 번째 글자부터 검사
def second_rule(words):
    for i in range(len(words)):
        for j in range(1, len(words[i])):
            if words[i][j].lower() not in shortcut_key:
                shortcut_key.add(words[i][j].lower())
                words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                return


n = int(input())
shortcut_key = set()

for _ in range(n):
    words = input().split()

    # 첫 번째 규칙을 적용
    if not first_rule(words):
        # 첫 번째 규칙을 적용할 수 없으면 두 번째 규칙을 적용 시도
        second_rule(words)

    print(' '.join(words))