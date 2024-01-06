def Rides(price,count):
    Sum = 0
    for i in range(1,count+1):
        Sum = Sum + (price*i)
    return Sum

def solution(price, money, count):
    answer = Rides(price,count)-money
    if answer <=0 :
        return 0
    return answer

price = 3
money = 20
count = 4
result = 10

print(solution(price,money,count))