def solution(s):
    answer = -1
    st=[]
    for al in s:
        if st and st[-1]==al:
            st.pop()
            continue
        else:
            st.append(al)

    return 0 if st else 1