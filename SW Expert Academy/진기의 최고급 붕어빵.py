'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2

1
2 2 2
1 2
'''

import sys
sys.stdin = open('input_붕어빵.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N:사람수, M초에 K개의 붕어빵 만들어짐
    person = list(map(int, input().split()))  # 사람들 도착하는 시간(초)
    person.sort()       # 사람 온 순서로 정렬해주기
    # print(person)
    # print(person[-1])

    bread = 0       # 붕어빵 개수
    t = 0           # 시간
    ox = 1          # 1일때 Possible, 0일때 Impossible
    while t <= person[-1]:      # 마지막 사람올 때까지만 돌 것
        if t > 0 and t % M == 0:        # t가 0보다 크고 M의 배수일때!! 빵을 K개 만큼 더해줄 것
            bread += K
        for i in range(N):          # 사람올때 붕어빵 하나씩 빼주기 위해
            if t == person[i]:      # 사람올 때 시간과 t가 일치할 때
                bread -= 1          # 빵 하나씩 줄거니까 -1
                if bread < 0:       # 근데 빵이 0밑으로 내려가면 Impossible
                    ox = 0
                    break           # 그러니까 반복문 아예 나가줘야 함 (다음사람 안넘어가게)
        t += 1
    # print(bread)

    if ox == 1:
        print("#{} Possible".format(tc))
    elif ox == 0:
        print("#{} Impossible".format(tc))