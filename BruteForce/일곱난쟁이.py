dwarf = []
TARGET_H = 100
isAnswer = False

for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort()
length = len(dwarf)
total = sum(dwarf)
diff = total - TARGET_H

for i in range(length - 1):
    for j in range(i + 1, length):
        if dwarf[i] + dwarf[j] == diff:
            fake_1 = dwarf[i]
            fake_2 = dwarf[j]
            isAnswer = True
            dwarf.remove(fake_1)
            dwarf.remove(fake_2)
            break
    if isAnswer == True:
        break
        
for d in dwarf:
    print(d)