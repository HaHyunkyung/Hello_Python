import sys

def move(N, K):
    moves = 0
    while N < K:
        N += 3
        moves += 1
    moves = moves + N-K
    return moves

N, K = map(int, input().split())

result = move(N, K)
print(result)