def solution(s):
    answer = True
    st=[]
    for g in s:
        # if g=='(':
        #     st.append(g)
        if g==')':
            if st and st[-1]=='(':
                st.pop()
                continue
        st.append(g)
    
    return False if st else True