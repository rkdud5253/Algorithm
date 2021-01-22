'''
3
3 7
15 7
5 2
'''

num = int(input())
paper = [[0] * 100 for _ in range(100)]  # 흰색 도화지

for _ in range(num):
    x, y = map(int, input().split())  # 값 받아오기

    # 색종이 크기만큼 범위 설정해줘야하기 때문에
    # 받은 값에서 +10 범위만큼만 돌리기!! 10x10 나타내기
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1  # 1로 채워주고 그 값들 더할것

# for r in range(100):  # 이렇게 보면 설정을 위처럼했기 때문에
#     for c in range(100):  # 그림에서 보는걸 오른쪽으로 90도 회전한 모양
#         print(paper[r][c], end=' ')
#     print()

count = 0
for r in range(100):
    for c in range(100):
        if paper[r][c] == 1:
            count += 1
print(count)