'''
10
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
7
9 3 1 8 5 0 5
1 1 1 7 9 1 8
3 6 1 4 7 7 4
3 1 8 5 3 0 7
2 5 2 5 7 6 8
2 8 5 2 6 7 0
0 5 5 9 3 6 0
3
6 0 4
7 9 3
8 1 2
6
1 6 4 0 8 1
0 8 0 4 1 2
7 7 6 8 4 3
8 6 3 8 0 0
5 7 7 7 6 4
9 1 8 1 7 1
3
4 1 9
9 9 7
8 0 1
5
1 0 2 2 7
5 2 4 8 5
4 7 8 2 3
9 6 2 8 5
9 6 1 6 6
3
4 8 3
4 6 3
3 9 6
3
4 9 7
0 1 3
4 4 3
5
1 1 7 4 1
0 7 9 3 5
5 2 5 8 6
6 1 9 0 6
7 0 1 3 9

1
3
1 2 3
4 5 6
7 8 9
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N x N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for row in arr:
    #     print(*row)
    result1 = [[0] * N for _ in range(N)]
    result2 = [[0] * N for _ in range(N)]
    result3 = [[0] * N for _ in range(N)]

    # 숫자 하나씩 인덱스에 넣어줄 거야
    num = []
    for i in range(N):
        for j in range(N):
            num.append(arr[i][j])
    # print(num)

    # 90도
    num_idx = 0
    for c in range(N-1, -1, -1):
        for r in range(0, N):
            result1[r][c] = num[num_idx]
            num_idx += 1

    # 180도
    num_idx = 0
    for r in range(N-1, -1, -1):
        for c in range(N-1, -1, -1):
            result2[r][c] = num[num_idx]
            num_idx += 1

    # 270도
    num_idx = 0
    for c in range(0, N):
        for r in range(N-1, -1, -1):
            result3[r][c] = num[num_idx]
            num_idx += 1

    # 출력을 잘 모르겠다..
    # 아 테스트케이스 수 빼먹었다
    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(result1[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(result2[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(result3[i][j], end='')
        print()