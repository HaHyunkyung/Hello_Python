
def solution(babbling):
    answer = 0
    for b in babbling:
        for word in [ "aya", "ye", "woo", "ma" ]:
            if word * 2 not in b:
                b = b.replace(word, ' ')
        #strip() => 공백제거 strip('특정문자')=>특정문자 제거 
        if len(b.strip()) == 0:
            answer += 1

    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))