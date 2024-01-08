def solution(d, budget):
    answer = 0
    # sort() => 리스트.sort()로 쓰며 리스트 원본값을 직접 수정함
    # sorted() => sorted(리스트)로 쓰며 리스트 원본은 그대로이고 정렬값을 반환함
    d.sort()
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            answer += 1
        if budget < d[i]:
            break
    return answer

d = [1,3,2,5,4]
budget = 9

print(solution(d,budget))