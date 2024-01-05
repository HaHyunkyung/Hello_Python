def divisor(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count = count+1
    return count

def distinction(num,plus):
    if num % 2 !=0:
        return (-1)*plus
    return plus

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer = answer + distinction(divisor(i),i)
        
    return answer

left = 13
right = 17
print(solution(left,right))