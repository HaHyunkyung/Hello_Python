x = 18
answer = True
#str(x)로 x를 list형태로 한자리씩 다 끊어줌
#map(int,str(x)) str(x)를 int형으로 만들어줌
#int형을 list에 넣어줌
ls = list(map(int,str(x)))

#sum(리스트) =>리스트에 있는 숫자들 다 더해줌
Sum = sum(ls)

if x % Sum != 0:
    answer = False

print(answer)
