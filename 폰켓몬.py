def solution(nums):
    answer = 0
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2

nums = [3,1,2,3]
print(solution(nums))