'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
import sys
sys.stdin = open("input_노드의거리.txt", "r")

def bfs(v):
    Q = []   # 큐, 방문처리
    Q.append(v)  # enQ
    visit[v] = 1

    while Q:  # 큐가 비어있지 않은 동안
        v = Q.pop(0)   # deQ
        for w in range(1, V+1):
            if graph[v][w] == 1 and visit[w] == 0:  # 방문안했으면
                Q.append(w)
                visit[w] = visit[v] + 1   # 거리를 구하기 위한 계산
                if w == G:   # w가 도착정점이면 차를 계산해준다
                    return visit[G]-visit[S]
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())   # 정점, 간선
    graph = [[0] * (V+1) for _ in range(V+1)]   # 인접행렬 초기화
    visit = [0] * (V+1)   # 방문

    for i in range(E):   # 인접행렬 저장
        s, e = map(int, input().split())   # start, end
        graph[s][e] = 1
        graph[e][s] = 1

    S, G = map(int, input().split())   # 출발노드, 도착노드
    print("#{} {}".format(tc, bfs(S)))