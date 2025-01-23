d=[0]*1000001
d[1],d[2],d[3]=1,2,4

for i in range(4,1000001):
    d[i]=(d[i-1]+d[i-2]+d[i-3])%1000000009
for _ in range(int(input())):
    print(d[int(input())])