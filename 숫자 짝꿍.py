def solution(X, Y):
    answer = ''
    #9~0까지 -1씩 빼면서 반복문 돌아감
    for i in range(9,-1,-1):
        #문자열.count('특정문자열') => 문자열에서 특정 문자가 몇개 있는지 알려줌
        answer += (str(i)*min(X.count(str(i)),Y.count(str(i))))
        
    if answer == '':
        return '-1'
    elif len(answer) ==answer.count('0'):
        return '0'
    else:
        return answer
    
x = "12321"
y = "42531"
print(solution(x,y))