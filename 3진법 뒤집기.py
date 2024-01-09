def solution(n):
    answer = ''
    while n > 0:
        #divmod(변수,나눌 값) => 변수를 나눌 값으로 나눈 몫과 나머지를 반환함
        n, re = divmod(n,3)
        #나머지를 string으로 변환해서 차례대로 붙임
        answer += str(re)
    #int(string형 변수, base) => base진법으로 구성된 str형 변수를 10진법 으로 변환해줌
    return int(answer,3)

n = 45
print(solution(n))