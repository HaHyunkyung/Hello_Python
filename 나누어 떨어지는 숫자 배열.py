arr = [5,9,7,10]
divisor = 5
answer = []

for i in range(len(arr)):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
        
answer.sort()
    
if len(answer)==0 :
    answer.append(-1)

print(answer)

answer.sort(reverse=True)

print(answer)