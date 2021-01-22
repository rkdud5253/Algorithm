'''
3
5 6
10 8 7 4 9
10 100
9 4 1 6 9 10 0 5 8 2
10 6
3 1 6 8 0 9 7 9 9 7

1
5 6
10 8 7 4 9
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 구역, M: 수레용량
    carrot = list(map(int, input().split()))
    # print(carrot)

    remain = 0      # 남은 당근 수
    dist = 0        # 이동 거리
    for i in range(N):
        time = (remain + carrot[i]) // M    # 반복 횟수
        remain = (remain + carrot[i]) % M   # 남은 당근 수
        dist += time * (i+1) * 2
    if remain > 0:      # 다 돌았는데 당근이 남았으면
        dist += 2 * N
    print("#{} {}".format(tc, dist))