from itertools import combinations

def is_prime(num):
    for n in range(2,(num//2)+1):
        if num%n == 0:
            return False
    return True

def solution(nums):
    answer = 0
    #num에 있는 숫자 중복없이 3개 뽑아 리스트에 담기
    #2차원 배열로 저장됨
    cmb = list(combinations(nums,3)) 
    for arr in cmb:
        if is_prime(sum(arr)):
            answer += 1
    return answer

nums = [1,2,7,6,4]
print(solution(nums))