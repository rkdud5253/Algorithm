'''
7 6
11
'''

# 달팽이 숫자 생각해서 풀기!!
# 문제에서는 C: 가로, R: 세로지만 나는 오른쪽으로 90도 돌려서 계산할거니까
# C랑 R이랑 바꿔서 생각할 것..

R, C = map(int, input().split())
K = int(input())    # 어떤 관객의 대기번호
arr = [[0] * C for _ in range(R)]   # 공연장
# for row in arr:
#     print(row)

# 자리가 우하좌상으로 배정됨
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r = 0
c = 0
direction = 0
nr = 0
nc = 0

# 만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력해야 함
# 이 말이 이해가 안돼서 한참 보다가.. 아 자리수를 넘어가면 0을 출력해라..!!!
# 근데 for문을 다 돌고 나서 출력하니 출력 초과가 난다
# 그니까 아예 돌기전부터 자리수넘으면 벤!해주자
if K > R*C:
    print("0")
else:
    for i in range(1, R*C+1):
        r, c = nr, nc       # if문 안에 들어갔다 나왔을때 값을 넣어줘야함
        arr[r][c] = i
        nr = r + dr[direction]
        nc = c + dc[direction]
        # 만약 배열을 벗어나거나 이미 값이 존재한다면 방향바꾸기
        if nr < 0 or nr >= R or nc < 0 or nc >= C or arr[nr][nc] != 0:
            direction = (direction + 1) % 4     # 방향이 4개니까 돌아가면서 해주기위해 배열 길이만큼 나눔
            nr = r + dr[direction]
            nc = c + dc[direction]

    for i in range(R):
        for j in range(C):
            # print(arr[i][j], end=' ')
            if arr[i][j] == K:
                print(i+1, j+1)
                break       # 값 찾으면 더 안돌아도 되니까 break해주면 좋겠지!
