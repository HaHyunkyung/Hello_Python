import sys

def dfs(idx):
    #처음에 만든 visited 배열 가져옴
    global visited
    # 들어온 노드는 방문한걸로 바꿔줌
    visited[idx] = True
    print(idx , end=' ')
    for next in range(1, N+1):
        #만약에 다음 노드를 방문하지 않고, 그래프에 노드끼리 연결되어 있다면 다음 노드를 불러와서 실행
        if not visited[next] and graph[idx][next]:
            dfs(next)
            
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
    
#0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int, input().split())

#(N*1)+(N*1) 배열로 그래프 정보 저장
graph = [[False]*(N + 1) for _ in range(N+1)]
#해당 노드에 방문했는지 확인하는 1차원 배열
visited = [False]*(N +1)

#1. graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    #만약 (1,2)에 방문했다면 (2,1)도 방문한것이 됨
    graph[a][b] = True
    graph[b][a] = True
    
#2. dfs
#V는 시작노드
dfs(V)
print()

#3. bfs
#visited를 전체 False로 초기화
visited = [False] * (N+1)
#V는 시작노드
q = [V]
visited[V] = True
bfs()