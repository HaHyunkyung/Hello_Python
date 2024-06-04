"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문 여부 확인)
- 재귀함수에서 N개를 선택할경우 print

2. 시간복잡도
- N! > 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]

백트래킹은 트리구조라고 생각하면 쉬움
"""

import sys
input = sys.stdin.readlines

N,M = map(int, input().split)
rs = []
chk = [False]*(N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()

recur(0)