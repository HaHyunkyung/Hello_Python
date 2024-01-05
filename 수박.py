def solution(n):
    first = '수'
    twice = '수박'
    if n ==1:
        return first
    if n % 2 == 0:
        return twice*(int(n/2))
    
    return twice*(int(n/2))+first

n = 5
print(solution(n))