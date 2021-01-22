'''
3
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2
5 5
3 4 1 2 3
3 4 1 3 2
2 3 2 4 1
1 4 4 1 3
2 2 3 4 4
5 8
1 3 4 4 4 4 3 3
4 1 2 4 3 1 4 4
4 1 4 4 1 4 2 1
3 2 4 2 1 1 2 1
4 4 1 4 4 2 2 2

1
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2
'''

dr = [-1, 0, 1, 0]     # 상우좌하
dc = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N x M 행렬
    balloon = [list(map(int, input().split())) for _ in range(N)]
    # for row in balloon:
    #     print(row)

    maxV = 0  # 꽃가루 최대 개수
    for r in range(N):
        for c in range(M):
            dist = balloon[r][c]    # 여기 값만큼 거리 갈 것
            sum = 0     # 꽃가루 개수

            for k in range(4):
                for d in range(1, dist+1):      # 이만큼 반복해야함
                    nr = r + (dr[k] * d)
                    nc = c + (dc[k] * d)
                    if 0 <= nr < N and 0 <= nc < M:
                        # print(balloon[nr][nc], end=' ')
                        sum += balloon[nr][nc]
            flower = sum + dist
            # print(flower)
            if maxV < flower:   # 가장큰값찾기
                maxV = flower
    print("#{} {}".format(tc, maxV))