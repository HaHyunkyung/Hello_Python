"""
1. 아이디어
- 2중 for, 값 1 && 방문x => DFS
- DFS를 통해 찾은 값을 저장 후 정렬해서 출력

2. 시간복잡도
- DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= 625 >> 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문 여부: bool[][]
- 결과값 : int[] 
"""

import sys
input = sys.stdin.readline

N = int(input()) # 지도의 크기
map = [list (map(int,input().split())) for _ in range(N)] # 지도
chk = [[False] * N for _ in range(N)] # 지도 크기와 똑같은 방문 지도
result = [] # 결과값
each = 0 # 단지 크기
dy = [0,1,0,-1] #방향키 (오 아 왼 위)
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each +=1 # 새로운 1을 찾았으므로 단지수 + 1
    for k in range(4): # 오아왼위 이므로 4번 반복
        ny = y + dy[k] # 받아온 위치에서 움직이며 탐방
        nx = x + dx[k]  # 받아온 위치에서 움직이며 탐방
        if 0<=ny<N and 0<=nx<N: # 지도 크기 넘지 않도록 
            if map[ny][nx]==1 and chk[ny][nx] == False: # 집이 있고, 방문하지 않은 곳 일때 실행
                chk[ny][nx] = True # 방문 노드로 변경
                dfs(ny, nx) # 재귀 함수 실행

for j in range(N): 
    for i in range(N):
        if map[i][j] ==1 and chk[j][i] == False: # 집이 있고, 방문하지 않은 곳 일때 실행
            chk[j][i] = True # 방문 노드로 변경
            each = 0 # 단지 부피 초기화 
            dfs(j,i) # dfs에 주소 넣기
            result.append(each) # 단지 부피 받아오기

result.sort() # 단지 부피 오름차순으로 정렬
print(len(result))
for i in result:
    print(i)