import sys
input=sys.stdin.readline

class Trie:
    head={}

    def add(self,words):
        cur=self.head

        for word in words:
            if word not in cur:
                cur[word]={}
            cur=cur[word]
        cur['*']=True

    # 깊이우선탐색 수행
    def read(self):
        def dfs(sub_head,depth):
            for key in sorted(sub_head.keys()):
                if key=='*':
                    continue
                print("--"*depth+key)
                dfs(sub_head[key],depth+1)
        dfs(self.head,0)

trie=Trie()
arr=[]
for _ in range(int(input().rstrip())):
    tmp=list(input().rstrip().split())
    arr.append(tmp[1:])

for a in arr:
    trie.add(a)

trie.read()