'''
3
6
8
15
'''

def inorder(node):  # 중위순회
    # LVR순서로 값 하나씩 넣어주기
    global cnt
    if node <= N:
        inorder(node*2)  # 왼쪽
        tree[node] = cnt
        cnt += 1  # 1부터 N까지 채울거니까 하나씩 증가
        inorder(node*2+1)  # 오른쪽


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드개수
    tree = [0] * (N+1)  # 0빼고 다른곳 채울 것
    # print(tree)
    cnt = 1   # 1부터 N까지 채울것

    inorder(1)
    # print(tree)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))