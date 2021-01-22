'''
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max_sum = 0
    # 작은 사각형이 큰 사각형 안에서만 돈다
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            # 작은 사각형 범위
            for r in range(M):
                for c in range(M):
                    sum += arr[i+r][j+c]
                #     print(arr[i+r][j+c], end=' ')
                # print()
            # print(sum)

            if sum > max_sum:
                max_sum = sum

    print("#{} {}".format(tc, max_sum))