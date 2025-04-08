import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input().rstrip())):
    a,b=input().rstrip().split()
    # 숫자로 변환한 후 정렬해야함에 유의
    arr.append([int(a),b])
arr.sort(key=lambda x:(x[0]))

for a,b in arr:
    print(a,b)
