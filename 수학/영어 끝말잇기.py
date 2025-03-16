def solution(n, words):
    arr=[] # 배열 없이 풀이 가능
    for word in words:
        if (arr and arr[-1][-1]!=word[0]) or (word in arr):
            return [len(arr)%n+1,len(arr)//n+1]
        arr.append(word)

    return [0,0]