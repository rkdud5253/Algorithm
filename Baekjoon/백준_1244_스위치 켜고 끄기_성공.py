'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

N = int(input())
switch = list(map(int, input().split()))
student_N = int(input())
student = [list(map(int, input().split())) for _ in range(student_N)]
# print(switch)
# print(student)

for i in range(student_N):
    # 1-남 : 두번째인덱스의 배수값 on off 바꿔줌
    if student[i][0] == 1:
        for k in range(N):
            if (k+1) % student[i][1] == 0:  # 배수일때
                if switch[k] == 1:
                    switch[k] = 0
                else:
                    switch[k] = 1

    # 2-여 : 두번째인덱스와 양쪽이 대칭인지 비교하고 on off 바꿔줌
    else:
        for k in range(N):
            if (k+1) == student[i][1]:  # 이 숫자를 중심으로!

                # 양쪽 비교
                idx = 0
                # 마지막 부분을 밑에 if로 쓰는거랑 while안에 넣는거랑 차이가 있군요!!
                while k-idx >= 0 and k+idx < N and switch[k-idx] == switch[k+idx]:
                    if switch[k-idx] == 1:
                        switch[k-idx] = 0
                        switch[k+idx] = 0
                    else:
                        switch[k-idx] = 1
                        switch[k+idx] = 1
                    idx += 1


# 한줄에 20개씩 출력해야하네! 20줄씩,,!
for i in range(N):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()