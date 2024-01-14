import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[0]*(N+1)for _ in range(N+1)]

visited = [False]*(N+1)

for _ in range(N):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True