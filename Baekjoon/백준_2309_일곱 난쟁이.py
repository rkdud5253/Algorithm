'''
20
7
23
19
10
15
25
8
13
'''

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
# print(dwarf)

allDwarf= sum(dwarf)
result = []
# 두개씩 조합해서 9개에서 뺀 값을 찾자
for i in range(9):
    for j in range(i+1, 9):
        # print(dwarf[i], dwarf[j], end=' ')
        if allDwarf - dwarf[i] - dwarf[j] == 100:
            # 이때의 키를 찾아야함
            # for d in dwarf:
            #     if d != dwarf[i] and d != dwarf[j]:
            #         result.append(d)
            # 요렇게 하니까 통과가 안된다
            result = [d for d in dwarf if d != dwarf[i] and d != dwarf[j]]
result.sort()
# print(result)
for i in result:
    print(i)