def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        score = []
        for j in range(len((photo[i]))):
            # count(값) => 리스트 안에 원하는 값이 몇개나 들었는지 반환해줌
            if name.count(photo[i][j]) == 1:
                #리스트.index(값) => 리스트에 값이 몇번째 인덱스에 위치하는지 인덱스 반환
                idx = name.index(photo[i][j])
                score.append(yearning[idx])
        answer.append(sum(score))
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))