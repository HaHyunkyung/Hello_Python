phone_number = "01033334444"
answer = ''
length = len(phone_number)
#[-4:]=>뒤에서 4자리 빼고 자르겠다는 뜻(4444만 남음)
#[3:]=>앞에서 3자리만 자르겠다는 뜻(010만 남음)
#[0:7]=>7개 문자 까지만 자르겠다는뜻 (0103333만 남음)
num = phone_number[-4:]
answer = "*"*(length-4)+num
print(answer)