def solution(k, score):
    answer = []
    rank = []
    for i in range(len(score)):
        if i<k:
            rank.append(score[i])
            rank.sort(reverse = True)
            answer.append(rank[i])
        if i >= k:
            rank.append(score[i])
            rank.sort(reverse = True)
            answer.append(rank[k-1])
            
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k,score))