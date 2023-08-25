n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = []
ap, bp = 0, 0

while ap != len(a) and bp != len(b):
    if a[ap] <= b[bp]:
        ans.append(a[ap])
        ap += 1
    else:
        ans.append(b[bp])
        bp += 1
    
if ap == len(a):
    ans.extend(b[bp:])
if bp == len(b):
    ans.extend(a[ap:])

ans = (' '.join(str(i) for i in ans))  
print(ans)