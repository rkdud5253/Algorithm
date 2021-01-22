'''
10 5
3
1 4
3 2
2 8
2 3
'''

import sys
sys.stdin = open('input_경비원.txt')

# 교수님,,!! 저 코드 3000줄이 넘었지만,, 이걸로 통과했어요...!ㅎㅎ

c, r = map(int, input().split())  # c:가로길이, r:세로길이
store = int(input())
dist = [list(map(int, input().split())) for _ in range(store)]
guard = list(map(int, input().split()))
# print(dist)
# print(guard)

# 동서남북.. 계산 다르게? 4군데를 다 생각해야하나
# 시계방향, 반시계방향 구해서 둘 중 적은거
# 전체길이 = (c + r) * 2  에서 빼주면 되겠지

minV = []
allDist = (c + r) * 2

if guard[0] == 1:       # 북
    for i in range(store):
        if dist[i][0] == 1:
            minV.append(abs(guard[1]-dist[i][1]))
        elif dist[i][0] == 2:
            left = guard[1] + r + dist[i][1]
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        elif dist[i][0] == 3:
            left = guard[1] + dist[i][1]
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        else:
            right = (c - guard[1]) + dist[i][1]
            left = allDist - right
            if left < right:
                minV.append(left)
            else:
                minV.append(right)

elif guard[0] == 2:     # 남
    for i in range(store):
        if dist[i][0] == 1:
            left = guard[1] + r + dist[i][1]
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        elif dist[i][0] == 2:
            minV.append(abs(guard[1]-dist[i][1]))
        elif dist[i][0] == 3:
            left = guard[1] + (r - dist[i][1])
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        else:
            right = (c - guard[1]) + (r - dist[i][1])
            left = allDist - right
            if left < right:
                minV.append(left)
            else:
                minV.append(right)

elif guard[0] == 3:     # 서
    for i in range(store):
        if dist[i][0] == 1:
            left = guard[1] + dist[i][1]
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        elif dist[i][0] == 2:
            left = guard[1] + (r - dist[i][1])
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        elif dist[i][0] == 3:
            minV.append(abs(guard[1]-dist[i][1]))
        else:
            left = guard[1] + c + dist[i][1]
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)

else:                   # 동
    for i in range(store):
        if dist[i][0] == 1:
            right = guard[1] + (c - dist[i][1])
            left = allDist - right
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        elif dist[i][0] == 2:
            left = (r - guard[1]) + (c - dist[i][1])
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        elif dist[i][0] == 3:
            left = (r - guard[1]) + c + (r - dist[i][1])
            right = allDist - left
            if left < right:
                minV.append(left)
            else:
                minV.append(right)
        else:
            minV.append(abs(guard[1]-dist[i][1]))

# print(minV)
sum = 0
for i in minV:
    sum += i
print(sum)