'''
2
3
4
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # print(arr)

    r = 0
    c = 0
    nr = 0
    nc = 0

    direction = 0
    dr = [0, 1, 0, -1]  # 우하좌상 으로 움직임
    dc = [1, 0, -1, 0]

    for i in range(1, N*N+1):
        r, c = nr, nc
        arr[r][c] = i
        nr = r + dr[direction]
        nc = c + dc[direction]
        # 배열을 벗어나거나 이미 숫자를 넣었으면
        if nr < 0 or nc < 0 or nr >= N or nc >= N or arr[nr][nc] != 0:
            direction = (direction + 1) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
