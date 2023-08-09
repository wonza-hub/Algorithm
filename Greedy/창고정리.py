l = int(input())
cols = list(map(int, input().split()))
m = int(input())
# 리스트를 이용한 해쉬
cnt = [0] * 101
max_h = int(-10e9)
min_h = int(10e9)

for col in cols:
    cnt[col] += 1
    if col > max_h: max_h = col
    if col < min_h: min_h = col

for _ in range(m):
    if cnt[max_h] == 1:
        cnt[max_h] -= 1
        max_h -= 1
        cnt[max_h] += 1
		# 동일 최고 높이가 존재하는 경우 max_h 갱신하지 않음
    else:
        cnt[max_h] -= 1
        cnt[max_h - 1] += 1

    if cnt[min_h] == 1:
        cnt[min_h] -= 1
        min_h += 1
        cnt[min_h] += 1
    else:
        cnt[min_h] -= 1
        cnt[min_h + 1] += 1
    
print(max_h - min_h)