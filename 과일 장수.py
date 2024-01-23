def solution(k, m, score):
    answer = 0
    mod = int(len(score))%m
    score.sort(reverse=True)
            
    for i in range(0,int(len(score)-mod),m):
        box = []
        for j in range(i, i+m,1):
            box.append(score[j])
       
        answer += min(box)*m
    return answer

k = 4
m = 3
score = [4,1,2,2,4,4,4,4,1,2,4,2]

print(solution(k,m,score))