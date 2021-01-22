'''
3
5
10 8 7 4 9
10
9 4 1 6 9 10 0 5 8 2
10
3 1 6 8 0 9 7 9 9 7

1
5
10 8 7 4 9
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N개의 구역
    carrot = list(map(int, input().split()))    # 당근 개수
    # print(carrot)

    min_num = 987654321
    idx = 0

    # 구역 사이사이를 한번씩 돌아가면서 나눠보기?
    for i in range(1, N):

        a = carrot[:i]
        b = carrot[i:]
        # print(a, b, end=' ')

        sum1 = 0
        sum2 = 0
        for j in a:
            sum1 += j
        # print(sum1)

        for j in b:
            sum2 += j
        # print(sum2)

        result = abs(sum1 - sum2)   # 절대값!
        # print(result)

        if result < min_num:
            min_num = result
            idx = i
    print("#{} {} {}".format(tc, idx, min_num))