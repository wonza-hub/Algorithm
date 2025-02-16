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

    def search(self,word):
        cur=self.head

        for ch in word:
            if ch not in cur:
                return False
            
            cur=cur[ch]
        return True

ans=0
trie=Trie()
n,m=map(int,input().rstrip().split())
for _ in range(n):
    trie.add(input().rstrip())
for _ in range(m):
    if trie.search(input().rstrip()):
        ans+=1

print(ans)