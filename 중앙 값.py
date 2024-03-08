import sys

numbers = list(map(int, input().split()))

sorted_numbers = sorted(numbers)
median = sorted_numbers[2]

print(median)