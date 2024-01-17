# 문제 설명
# 숫자 N과 집합 Q의 원소 개수 K, Q의 원소들이 주어집니다.

# N보다 작거나 같은 자연수 중 Q의 원소로만(중복가능) 만든 수 중 가장 큰 수를 출력해주세요.

# 집합 Q는 1부터 9 사이의 자연수로만 이루어져 있습니다.
# 예를 들어, N= 657이고 Q = {1,5,7}일 때 답은 577입니다.
# 예를들어
# 657 3
# 1 5 7
# 의 입력이 있을 때
# 1, 5, 7 로 만들 수 있는 가장 큰 숫자는 577입니다.

n, k = map(int, input().split())
q = list(map(int, input().split()))

ans = -10e9
def f(sum):
    global ans
    if n < sum:
        return ans
    
    ans = max(ans, sum)
    for i in range(k):
        f(sum * 10 + q[i])
        
f(0)
print(ans)

