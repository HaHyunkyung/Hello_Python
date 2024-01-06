def solution(s):
    # String변수.isdigit() => 문자열이 정수인지 확인. 음수, 소숫점,문자가 섞이면 False
    if(len(s)==4 or len(s)==6)and s.isdigit():
        return True
    return False

s = "1234"
t = "a1234"

print(solution(s))
print(solution(t))