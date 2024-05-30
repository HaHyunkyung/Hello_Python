"""
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 >> 가능!

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""


from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # 세로 n, 가로 m
map = [list(map(int, input().split())) for _ in range(n)] # 그림
chk = [[False]*m for _ in range(n)] # 그림 크기와 똑같은 False로 채워진 이차원배열

dy =[0,1,0,-1]
dx = [1,0.-1,0]
# 오른쪽, 아래, 왼쪽, 위 

def bfs(y,x):
    rs = 1 # 그림 부피
    q = deque() # 앞뒤로 요소를 추가하고 삭제할 수 있는 자료구조
    q.append((y,x)) # 큐에 (y,x) 좌표 넣기
    while q: # 큐에 값이 있을때 돌아감. pop되서 없어지면 탈출
        ey, ex = q.popleft() # 제일 앞의 요소가 삭제됨
        for k in range(4): # 앞 뒤 양옆이라 4번 반복함
            ny = ey + dy[k] # 원래 y좌표에 앞뒤양옆 옮겨다님
            nx = ex + dx[k] # 원래 x좌표에 앞뒤양옆 옮겨다님
            if 0 <=ny < n and 0 <= nx < m: # 앞뒤양옆 옮겨다니면서 그림 크기 안넘어가게 하기
                if map[ny][nx] == 1 and chk[ny][nx] == False: # 옮겨다니다가 값이 1이고 방문한 노드가 아닐때 실행함
                    rs +=1 # 그림 부피 + 1
                    chk[ny][nx] = True # 방문한 노드로 바꿔줌
                    q.append((ny, nx)) # q에 방문한 노드로 넣어줌
    return rs # 그림 부피 반환
                

cnt = 0 # 그림 갯수
maxv = 0 # 그림 부피의 최댓값

for j in range(n): 
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False: # 한칸씩 그림을 옮겨다니다가 1이고 방문하지 않은 노드면 실행
            chk[j][i] = True # 방문한 노드로 바꿔주기
            cnt += 1 # 그림 갯수 +1
            maxv = max(maxv, bfs(j,i)) # bfs 돌려서 그림 부피 구하고 max에 넣어서 최대 그림 부피 갱신

print(cnt) # 그림 갯수
print(maxv) # 최대 그림 부피
