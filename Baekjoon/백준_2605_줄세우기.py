'''
5
0 1 1 3 2
'''
N = int(input())  # 학생수
num = list(map(int, input().split()))  # 뽑은번호
students = list(range(1, N+1))  # 처음 학생 순서
line = []  # 마지막 순서를 담을 출력값

for i in range(N):
    # insert를 써야 정해진 위치에 값을 추가할 수 있다
    # 뽑은 번호수 만큼 앞으로 가야하므로 -해주기
    line.insert(i-num[i], students[i])

print(*line)  # 리스트안 요소들만 나오게 하기위해 *붙이기