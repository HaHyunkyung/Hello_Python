def solution(s):
    dic = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i in range(len(dic)):
        # replace(old,new) => 문자열에서 old를 찾아 new로 바꿔줌
        # dic에 저장된 문자열을 찾아 i를 str형으로 바꿔 넣어줌
        s = s.replace(dic[i],str(i))
        # s를 int형으로 바꿔줌
    return int(s)

s = "2three45sixseven"
print(solution(s))