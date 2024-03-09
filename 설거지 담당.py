def largest_multiple_of_300(N, nums):
    total_sum = sum(nums)

    # 모든 정수의 합이 3의 배수가 아니면 300의 배수를 만들 수 없음
    if total_sum % 3 != 0:
        return -1

    # 정수를 내림차순으로 정렬
    nums.sort(reverse=True)

    # 정수들을 문자열로 이어붙이기
    result_str = ''.join(map(str, nums))

    # 만들어진 문자열이 0이면 결과는 0
    if result_str == '0':
        return '0'

    return result_str

# 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 결과 출력
result = largest_multiple_of_300(N, nums)
print(result)
