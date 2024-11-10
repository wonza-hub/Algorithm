def solution(s):  
    ans=[]
    s=s.split(' ')
    for word in s:
        if word:
            ans.append(word[0].upper()+word[1:].lower())
        else:
            ans.append(word)
    return ' '.join(ans)