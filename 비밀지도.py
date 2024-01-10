def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        #bin() =>10진수를 2진수로 바꿔주는 함수. string형 문자열로 반환되고 앞에 0b가 붙는다.
        # 앞에 0b를 없애줘야됨  
        # 각 arr의 bin()이 먼저 실행되고 or연산을 통해 합쳐지는듯 함  
        num = bin(arr1[i] | arr2[i])
        print(num)
        #문자열.zfill(n) => 문자열이 n자릿수가 되도록 앞에 0을 채워줌
        num = num[2:].zfill(n)
        #replace(old,new) => 문자열에서 old를 찾아서 new로 바꿔줌 
        num = num.replace('1','#').replace('0',' ')
        answer.append(num)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n,arr1,arr2))