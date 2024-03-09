import math

def combination_count(A, B):
    # A개의 원소에서 B개의 원소를 뽑는 조합의 경우의 수 계산
    result = math.comb(A, B)
    return result

# 입력 받기
A, B = map(int, input().split())

# 조합의 경우의 수 출력
result = combination_count(A, B)
print(result)
