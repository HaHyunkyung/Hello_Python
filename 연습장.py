N, K = map(int, input().split())
items = []
for _ in range(N):
    weight, value = map(int, input().split())
    items.append((weight, value))
bags = [int(input()) for _ in range(K)]
    
items.sort(key=lambda x: x[1], reverse=True)
bags.sort()

count = 0

for i in range(len(bags)):
    for j in range(len(items)):
        if items[j][0] <= bags[i] :
            count += items[j][1]
            items = items[1:]
            items = items[1:] + [items[0]]
            break
print(N,K)
print(items)
print(bags)
print(count)