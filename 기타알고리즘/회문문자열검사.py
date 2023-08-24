n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1-j]:
            print(f"#{i + 1} NO")
            break
    print(f"#{i + 1} YES")

# 파이썬 다운 방식
# if s == s[::-1]:
#     print(f"#{i + 1} YES")
# else:
#     print(f"#{i + 1} NO")
    