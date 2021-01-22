'''
3
10
0011001110
10
0000100001
10
0111001111

1
10
0111001111
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    # print(num)

    i = 0
    cnt = 0
    maxV = 0
    while i < N:
        if num[i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        else:
            cnt = 0
        i += 1
    print("#{} {}".format(tc, maxV))