'''
1
4
2 4 7 10

1
3
1 1 1
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자 개수
    num = list(map(int, input().split()))   # 숫자들

    # 1<=i<j<N
    # 조합? 으로 푸는건가? 일단 인덱스로..해보기

    danJo = []
    for i in range(0, N-1):
        for j in range(i+1, N):
            # i < j 클때만 계산할 것
            if i < j:
                # print(num[i], num[j])
                # print(num[i] * num[j])
                number = num[i] * num[j]
                str_number = str(number)

                # 단조 증가하는 수가 있으면 result에 넣기
                # result가 있으면 그중에서 Max값 찾기
                # result가 비었으면 -1 출력

                # 한자리 수는 무조건 단조 증가하는 수가 아니네!
                # print(len(str(number)))
                if len(str_number) >= 2:
                    # str_num을 하나하나 리스트에 넣어줌
                    # 그리고 그안에서 숫자 순서대로 커지는지 볼것
                    num_line = []
                    for s in str_number:
                        num_line.append(s)
                    # print(num_line)
                    for k in range(len(str_number)-1):
                        if num_line[k] < num_line[k+1]:
                            danJo.append(number)
    # print(danJo)
    # danJo.sort()
    # maxV = danJo[-1]        # 단조증가하는 수 중에 가장 높은거
    # print(maxV)
    # print(max(danJo))

    if danJo:       # 단조 증가하는 수 있으면
        print("#{} {}".format(tc, max(danJo)))
    else:           # 없으면
        print("#{} {}".format(tc, -1))