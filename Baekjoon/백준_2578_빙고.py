'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''

bingo = [list(map(int, input().split())) for _ in range(5)]     # 빙고판
num = [list(map(int, input().split())) for _ in range(5)]       # 사회자가 부르는 숫자
# print(bingo)
# print(num)

# 사회자가 부르는 숫자 리스트 안에 순서대로 넣기
num_list = []
for i in range(5):
    for j in range(5):
        num_list.append(num[i][j])
# print(num_list)

# 숫자 불릴 때마다 그 자리 0으로 바꿔주고
# 가로줄, 세로줄, 대각선1, 대각선2 확인해야함
# 세개이상 빙고면 그때의 숫자 출력

# print(num_list.pop(0)

cnt = 0
order = 0
order_list = []
for k in range(25):
    order += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num_list[k]:
                bingo[i][j] = 0

                line_cnt = 0
                # 여기서 이제 ,,!!! 빙고 됐는지 찾아야함
                # 가로
                for h in range(5):
                    cnt = 0
                    while cnt < 5 and bingo[h][cnt] == 0:
                        cnt += 1
                    if cnt == 5:
                        line_cnt += 1

                # 세로
                for h in range(5):
                    cnt = 0
                    while cnt < 5 and bingo[cnt][h] == 0:
                        cnt += 1
                    if cnt == 5:
                        line_cnt += 1

                # 왼쪽 대각선
                cnt = 0
                while cnt < 5 and bingo[cnt][cnt] == 0:
                    cnt += 1
                if cnt == 5:
                    line_cnt += 1

                # 오른쪽 대각선
                cnt = 0
                while cnt < 5 and bingo[4-cnt][cnt] == 0:
                    cnt += 1
                if cnt == 5:
                    line_cnt += 1

                # print(bingo)
                # 빙고가 3개 이상이면
                if line_cnt >= 3:
                    # print(order)
                    order_list.append(order)
print(order_list[0])