# 트라이 구현
import sys
input=sys.stdin.readline

class Trie():
    head={}

    def add(self,word):
        cur=self.head

        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur['*']=True
    
    def search(self,word):
        cur=self.head

        for ch in word:
            if ch not in cur:
                return False
            
            cur=cur[ch]
        if '*' in cur:
            return True
        else:
            return False

n,m=map(int,input().rstrip().split())
ans=0
        
trie=Trie()
for _ in range(n):
    trie.add(input().rstrip())
for _ in range(m):
    if trie.search(input().rstrip()):
        ans+=1

print(ans)
print(trie.head)