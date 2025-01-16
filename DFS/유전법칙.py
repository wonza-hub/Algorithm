def solution(queries):
    ans = []
    child = ["RR", "Rr", "Rr", "rr"]
    
    def dfs(gen, x):
        if gen == 1:
            return "Rr"
        parent = dfs(gen - 1, x // 4)
        if parent == "Rr":
            return child[x % 4]
        else:
            return parent
        
    for q in queries:
        n, p = q
        res = dfs(n, p - 1) # 몫을 활용하기 위한 조정
        ans.append(res)
    
    return ans