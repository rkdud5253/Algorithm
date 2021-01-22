'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''


# 백준 2606 바이러스
# 재귀
def dfs(v):
    if visited[v] == 0:
        visited[v] = 1
        for w in range(1, V + 1):
            if arr[v][w] == 1 and visited[w] == 0:
                dfs(w)


V = int(input())  # 컴퓨터의 수
E = int(input())  # 컴퓨터 쌍의 수
pair = [list(map(int, input().split())) for _ in range(E)]
# print(pair)
arr = [[0] * (V + 1) for _ in range(V + 1)]
# print(arr)
visited = [0] * (V + 1)
for i in range(E):
    n1, n2 = pair[i][0], pair[i][1]
    arr[n1][n2] = 1
    arr[n2][n1] = 1
# for r in arr:
#     print(r)
dfs(1)
# print(visited)
result = visited.count(1)
print(result - 1)


# # 재귀아닌거
# def dfs(v):
#
#     stack = []
#     stack.append(v)
#
#     while stack:
#         v = stack.pop()
#         if visited[v] == 0:
#             visited[v] = 1
#
#             for w in range(1, V+1):
#                 if arr[v][w] == 1 and visited[w] == 0:
#                     stack.append(w)
#
#
#
# V = int(input())  # 컴퓨터의 수
# E = int(input())  # 컴퓨터 쌍의 수
# pair = [list(map(int, input().split())) for _ in range(E)]
# # print(pair)
#
# arr = [[0] * (V+1) for _ in range(V+1)]
# # print(arr)
# visited = [0] * (V+1)
#
# for i in range(E):
#     n1, n2 = pair[i][0], pair[i][1]
#     arr[n1][n2] = 1
#     arr[n2][n1] = 1
#
# # for r in arr:
# #     print(r)
#
# dfs(1)
# # print(visited)
#
# result = visited.count(1)
# print(result-1)