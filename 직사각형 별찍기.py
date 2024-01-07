# strip(매개변수) => 문자열 시작 또는 끝에서 매개변수가 제거됨. 매개변수가 없으면 공백이 삭제됨
a, b = map(int, input().strip().split(' '))
for j in range(b):
    for i in range(a):
        print('*',end ='')
    print('')