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

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    # print(arr)

    i = 0       # arr를 돌기 위한 인덱스
    cnt = 0     # 1찾으면 개수를 세기 위한 카운트
    max_num = 0

    while i < N:
        if int(arr[i]) == 1:
            cnt += 1
            i += 1
            if max_num < cnt:
                max_num = cnt
        else:       # 0일때
            i += 1
            if max_num < cnt:
                max_num = cnt
            cnt = 0
    print("#{} {}".format(tc, max_num))