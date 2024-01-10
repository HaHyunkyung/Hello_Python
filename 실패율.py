def solution(N, stages):
    #{}는 딕셔너리 . 딕셔너리는 순서가 있기 때문에 인덱스 사용 가능함
    answer = {}
    people = len(stages)
    
    for i in range(1, N+1):
        if people == 0:
            answer[i] = 0
        if people != 0 :
            #문자열.count(변수) => 문자열에서 변수를 몇개나 포함하고 있는지 반환함
            answer[i] = stages.count(i)/(people)
            people -= stages.count(i)
    #딕셔너리에서는 딕셔너리.get으로 값을 꺼내볼 수 있다
    answer = sorted(answer, key = answer.get, reverse = True)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))