#divmod()
mok,na =divmod(20,3) #//20/3의 몫과 나머지를 차례대로 반환함
print(mok,na)

#int(str,base) =>base 진법으로 구성된 str형 문자열을 10진법으로 변환함
num = int('110',2)
print(num)

#sort(), reverse(오름차순,내림차순)
sort_set = [3,5,4,1,2,9,7,8]
sort_set.sort() #리스트를 직접 오름차순으로 수정함
print(sort_set)

sort_set.sort(reverse=True) #리스트를 직접 내림차순으로 수정함
print(sort_set)

#set() => 리스트의 중복 제거 *주의할점* set써준 뒤에 다시 list 형으로 바꿔야됨 그래야 sort로 정렬 가능
set_set = [6,5,6,1,7,11,11,11,44,24,24,88,31,31,31]
set_set = list(set(set_set))
print(set_set)
set_set.sort()
print(set_set)

#isdigit() => str형 문자열이 정수로만 이루어져있는지 확인.음수,소숫점,문자가 섞이면 False
digit_str = "12345"
digit_str_2 = "-0.12"
digit_str_3 = "#1234"
print(digit_str.isdigit())
print(digit_str_2.isdigit())
print(digit_str_3.isdigit())

#join() => list를 구분자 끼워서 str형으로 만들 수 있음
join_set = ['가','나','다','라']
print(''.join(join_set))
print('_'.join(join_set))

join_str = "Zbcdfg"
print(''.join(sorted(join_str)[::-1])) #문자열[::-1] => 문자열 거꾸로 뒤집음

#bin() => 10진수를 2진수로 바꿔주는 함수. str형으로 반환되고 앞에 0b가 붙는다
bin_num = 10
print(bin(bin_num))
print(bin(bin_num)[2:])

#문자열.zfill(n)=> 문자열이 n자리수가 될때까지 앞을 0으로 채워줌
z_num = "1234"
print(z_num.zfill(9))

#replace(old,new) => 문자열에서 old를 찾아 new로 바꿔줌
re_str = "hello world"
print(re_str.replace('world','today'))
print(re_str.replace('hello','welcome').replace('world','cosmos')) #=>연달아서도 가능

#거꾸로 for문 (시작,마지막,줄어주는 수)
for i in range(9,-1,-1):
    print(i)

#문자열.count(특정문자) => 문자열에서 특정 문자 몇개 있는지 확인
count_str = 'abababa'
print(count_str.count('a'))

#split('구분자') => 문자열을 구분자 기준으로 잘라서 리스트에 넣음
sp_str = 'a b c d e'
sp_list = []
sp_list = sp_str.split(' ')
print(sp_list)
print(sp_str.split(' ')[1]) #->한개씩 보는것도 가능함

#dictionary => 키:값 순으로 저장됨

dic = {1:'봄', 2:'여름',3:'가을',4:'겨울'}
print(dic.keys()) #=>키만 전부 가져오기
print(dic.values()) #=>값만 전부 가져옴
print(dic.get(1)) #=> 키값에 맞는 값 가져옴
dic[5] = '사계절' #=> 변수[키] = 값 써주면 딕셔너리에 키와 값 추가됨
print(dic.get(5))

#sorted
ed_str = "54321"
ed_str = ''.join(sorted(ed_str))
print(ed_str)