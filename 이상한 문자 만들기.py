def solution(s):
    answer = ''
    s_list = s.split(' ')
    for i in s_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            if j % 2 !=0:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]

s = "try hello world"
print(solution(s))