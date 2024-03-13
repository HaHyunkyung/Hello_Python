from itertools import permutations

def find_largest_multiple(nums):
    # 모든 순열 생성
    perms = permutations(nums)
    
    max_multiple = -1
    
    # 각 순열을 문자열로 변환하여 300의 배수인지 확인
    for perm in perms:
        num_str = ''.join(map(str, perm))
        num = int(num_str)
        if num % 300 == 0 and num > max_multiple:
            max_multiple = num
            
    return max_multiple

# 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 가장 큰 300의 배수 찾기
result = find_largest_multiple(nums)

# 결과 출력
print(result)