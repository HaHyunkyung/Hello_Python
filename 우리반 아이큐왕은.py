# 학생 수 입력
n = int(input())
students = []
input_order = 0

# 학생 정보 입력
for _ in range(n):
    name, iq = input().split()
    students.append((name, int(iq), input_order))
    input_order += 1

# IQ가 높은 순서, 먼저 입력된 순서로 정렬
students.sort(key=lambda x: (-x[1], x[2]))

# 상위 3명 출력
for i in range(3):
    print(students[i][0])

