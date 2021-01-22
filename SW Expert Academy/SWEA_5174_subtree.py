'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

def preorder(node):  # 전위순회
    global cnt     # cnt를 global로 불러와줘야함
    if node:       # 노드가 있다면
        cnt += 1   # 개수를 알기위해 +1
        preorder(tree[0][node])   # 왼쪽
        preorder(tree[1][node])   # 오른쪽


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # E:간선 N:서브트리 시작노드
    temp = list(map(int, input().split()))  # 부모자식 노드 쌍
    tree = [[0] * (E+2) for _ in range(2)]  # 0부분 안쓰고 인접리스트로 표현하기 위해 만들어줌
    cnt = 0  # 개수 세기 위해 만들어줌
    # print(tree)

    # tc 1번이라면
    # 부모        1 2 3 4 5 6
    # 왼쪽자식   0 [6 1 0 0 3 4]  요기
    # 오른쪽자식 0 [0 5 0 0 0 0]   요기만쓸것
    for i in range(E):   # 간선개수만큼 넣어준다
        p, c = temp[i*2], temp[i*2+1]  # 받은 쌍을 홀짝으로 받기
        if tree[0][p] == 0:   # 왼쪽에 없으면 왼쪽 먼저 넣어주기
            tree[0][p] = c  # left
        else:                # 왼쪽에 있으면 오른쪽 넣어주기
            tree[1][p] = c  # right

    # for t in tree:
    #     print(*t)

    preorder(N)  # 서브트리 값을 순회하겠다
    print("#{} {}".format(tc, cnt))

