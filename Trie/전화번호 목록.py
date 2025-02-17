import sys
input=sys.stdin.readline

class Trie():
    head={}

    def add(self,word):
        cur=self.head

        for ch in word:
            if '*' in cur:
                return False
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur['*']=True

        return True

trie=Trie()
for _ in range(int(input().rstrip())):
    # Test Case마다 루트, 플래그 초기화 유의
    trie.head={}
    FLAG=True
    arr=[]

    for _ in range(int(input().rstrip())):
        arr.append(input().rstrip())
    arr.sort(key=lambda x:len(x))

    for a in arr:
        if not trie.add(a):
            FLAG=False

    if FLAG:
        print('YES')
    else:
        print('NO')
