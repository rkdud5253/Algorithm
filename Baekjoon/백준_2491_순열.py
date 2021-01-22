'''
9
1 2 2 4 4 5 7 7 2

9
4 1 3 3 2 2 9 2 3

11
1 5 3 6 4 7 1 3 2 9 5
'''

N = int(input())
li = list(map(int, input().split()))
# print(li)

# 커지는 값
idx = 1
cnt = 1
i = 0
max_num = 0
while i < N and idx < N:
    if li[i] <= li[idx]:
        cnt += 1
        idx += 1
    else:
        cnt = 1
        idx += 1
    i += 1

    if max_num <= cnt:
        max_num = cnt

# print(max_num)

# 작아지는 값
idx = 1
cnt = 1
i = 0

while i < N and idx < N:
    if li[i] >= li[idx]:
        cnt += 1
        idx += 1
    else:
        cnt = 1
        idx += 1
    i += 1

    if max_num <= cnt:
        max_num = cnt

# 맞왜틀!!!!!!!!!!
# 뭐가 문젤까 했는ㄷ 1일때 조건을 생각 못한거였다
# 밑에꺼 넣으니까 통과~~~ 뿌듯해 ㅎㅎㅎㅎ
if N == 1:
    max_num = 1

print(max_num)