n = 118372
answer = 0
ls = list(str(int(n)))
# sort()는 기준에 따라 오름차순 or 내림차순 정렬
# reverse()는 그냥 냅다 리스트 순서 뒤집기
ls.sort(reverse = True)
# "".join(문자열) => 공백을 기준으로 리스트를 문자열로 변경
answer = int("".join(ls))
print(answer)