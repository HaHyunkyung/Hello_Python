def solution(s):
    return (''.join(sorted(s)[::-1]))
s = "Zbcdefg"
print(solution(s))