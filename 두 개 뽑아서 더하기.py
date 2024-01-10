def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    #set으로 중복 제거
    #set은 순서가 없음
    #answer를 set형에서 list로 변경함
    answer = list(set(answer))
    answer.sort()
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))