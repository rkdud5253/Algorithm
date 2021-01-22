'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    # print(Ci)

    q = []
    # 피자가 1개 남을 때까지
    while len(q) != 1:
        if C[q[0]] != 1:
            C[q[0]] = C[q[0]]//2
            q.append(q.pop(0))
        # 치즈가 녹아 0이 되면 pop
        else:
            C.pop(0)

    print("#{} {}".format(tc, q[0]))