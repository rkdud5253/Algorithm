'''
9
1 2 2 4 4 5 7 7 2

9
4 1 3 3 2 2 9 2 3

11
1 5 3 6 4 7 1 3 2 9 5
'''

# 백준은 실패! 정올은 통과.. 전에꺼랑 idx가 달라져서 그런가
# 뭐가 다른건지 궁금하다

N = int(input())
li = list(map(int, input().split()))


# 커질때
i = 0
cnt = 1
maxV = 0
while i < N-1:
    if li[i] <= li[i+1]:
        cnt += 1
    else:
        cnt = 1
    i += 1
    if maxV < cnt:
        maxV = cnt

# 작아질때
i = 0
cnt = 1
while i < N-1:
    if li[i] >= li[i+1]:
        cnt += 1
    else:
        cnt = 1
    i += 1
    if maxV < cnt:
        maxV = cnt

# N이 1일때는 무조건 1
if N == 1:
    maxV = 1

print(maxV)
