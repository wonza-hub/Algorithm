# 딕셔너리 구현
class Trie:
    head={}

    def add(self,word):
        # 트라이의 루트부터 탐색 시작
        cur=self.head

        for ch in word:
            # 현재보고 있는 정점 확인
            if ch not in cur:
                cur[ch]={} # 정점이 해당 문자가 아닌 경우, 키:값 을 문자:{}로 하는 요소 추가
            cur=cur[ch] # 다음 정점 탐색
        # 문자열이 트라이에 존재하는 경우, * 키:값 을 *:Boolean로 하는 표시 추가
        cur['*']=True

    def search(self,word):
        # 트라이의 루트부터 탐색 시작
        cur=self.head

        for ch in word:
            if ch not in cur:
                return False

            cur=cur[ch]
        # 탐색 완료 시, *을 마주치면 찾는 문자열이 있다는 의미
        if '*' in cur:
            return True
        else:
            return False