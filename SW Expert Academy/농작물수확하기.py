'''
1
5
14054
44250
02032
51204
52212
'''
# 보충 들고 이해하고 다시 혼자 풀어보기!!

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 농장의 크기 NxN
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)

    mid = N//2

    sum = 0
    # 커질때
    for i in range(mid+1):
        for j in range(mid-i, i+mid+1):
            sum += farm[i][j]
            # print(farm[i][j], end=' ')
    # print(sum)

    # 줄어들때
    for i in range(mid+1, N):
        # 여기 규칙찾기 어려워 (i-mid, N-(i-mid-1)-1)
        for j in range(i-mid, N-i+mid):
            sum += farm[i][j]
            # print(farm[i][j], end=' ')

    print("#{} {}".format(tc, sum))





# 이건 보충 교수님 답
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input())) for _ in range(N)]
#
#     mid =  N // 2
#     start = mid
#     end = mid
#     sum = 0
#
#     for i in range(N):
#         for j in range(start, end+1, 1):
#             sum += data[i][j]
#         if i < mid :
#             start -= 1
#             end += 1
#         else:
#             start += 1
#             end -= 1
#     print("#{} {}".format(tc, sum))