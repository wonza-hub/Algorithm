import sys
input=sys.stdin.readline
from collections import defaultdict

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

dic=defaultdict(list)
N,M,K=map(int,input().split())
for _ in range(M):
	r,c,m,s,d=map(int,input().split())
	dic[(r-1,c-1)].append((m,s,d))

cnt=M
for _ in range(K):
	# 이동한 파이어볼들을 담을 임시 딕셔너리
	new_dic=defaultdict(list)

	# 파이어볼 이동
	for (x,y),balls in dic.items():
		for m,s,d in balls:
			nx=(x+dx[d]*s)%N
			ny=(y+dy[d]*s)%N
			new_dic[(nx,ny)].append((m,s,d))

	# 질량, 속력, 방향 계산
	# 딕셔너리 초기화
	dic=defaultdict(list)
	for (x,y),balls in new_dic.items():
		개수=len(balls)
		
		if 개수==1:
			dic[(x,y)].append(balls[0])
			continue
			
		질량합=sum([b[0] for b in balls])
		질량=질량합//5
		# 새로운 질량이 0인 경우 소멸
		if 질량==0:
			continue
			
		속력합=sum([b[1] for b in balls])
		속력=속력합//개수
		
		방향s=[b[2] for b in balls]

		# all 함수
		if all(방향%2==0 for 방향 in 방향s) or all(방향%2==1 for 방향 in 방향s):
			for 방향 in [0,2,4,6]:
				dic[(x,y)].append((질량,속력,방향))
		else:
			for 방향 in [1,3,5,7]:
				dic[(x,y)].append((질량,속력,방향))

ans=sum(m for balls in dic.values() for m,_,_ in balls)
print(ans)
