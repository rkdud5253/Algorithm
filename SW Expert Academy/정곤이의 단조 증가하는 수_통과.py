'''
1
4
2 4 7 10

1
3
1 1 1

'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 숫자 개수
    num = list(map(int, input().split()))  # 숫자들

    maxV = 0
    flag = -1
    for i in range(0, N - 1):
        for j in range(i+1, N):
            # i < j 클때만 계산할 것
            if i < j:
                number = num[i] * num[j]
                str_number = str(number)
                # print(str_number)

                if len(str_number) == 1:
                    flag = 0

                for k in range(len(str_number) - 1):        # 단조 없을 때 나가게?
                    if int(str_number[k]) > int(str_number[k + 1]):
                        break
                else:
                    flag = 1
                    # print(number)
                    if maxV < number:
                        maxV = number

    # print(danJo)
    if flag == 1:  # 단조 증가하는 수 있으면
        print("#{} {}".format(tc, maxV))
    else:  # 없으면
        print("#{} {}".format(tc, -1))
