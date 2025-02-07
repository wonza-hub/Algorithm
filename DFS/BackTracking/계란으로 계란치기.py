import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=[]
for _ in range(n):
    hp,w=map(int,input().rstrip().split())
    arr.append([hp,w])
ans=0

def dfs(l,cnt):
    global ans
    # EARLY RETURN:
    # 남은 계란을 전부 1타2피로 깨뜨렸음에도 최댓값(지금까지 나온 최선의 경우)보다 작은 경우
    if ans>=(cnt+(len(arr)-l)*2):
        return
    # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우
    if l==len(arr):
        ans=max(ans,cnt)
        return

    # 내구도 0보다 작거나 같은 경우, 즉 든 계란이 깨져있는 경우
    if arr[l][0]<=0:
        dfs(l+1,cnt)
    else:
        # FLAG:  한 개의 계란도 못 깨뜨리는 경우에도 깊이 탐색은 재개되어야 함
        # 즉, 깨지지 않은 다른 계란이 없는 경우에 해당
        flag=False
        for i in range(len(arr)):
            # 든 계란인 경우
            if i==l:
                continue
            # 깨뜨리려고 하는 계란이 이미 깨져있는 경우
            if arr[i][0]<=0:
                continue
            flag=True
            wa,wb=arr[l][1],arr[i][1]
            arr[l][0]-=wb
            arr[i][0]-=wa
            dfs(l+1,cnt+int(arr[l][0]<=0)+int(arr[i][0]<=0))
            arr[l][0]+=wb
            arr[i][0]+=wa
        # else: # 틀린풀이 => else:
        if flag==False:
            dfs(l+1,cnt)

dfs(0,0)
print(ans)
