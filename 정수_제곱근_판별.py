n = 121
answer = 0
#**은 제곱근 계산
num = n**0.5

if num == int(num):
    answer = (num+1)**2
if num != int(num):
    answer = -1

print(answer)