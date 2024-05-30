def apply_rule(arr):
    # 배열의 가로 길이와 세로 길이를 구합니다.
    n = len(arr)
    m = len(arr[0])

    # 배열의 가로 길이가 세로 길이보다 길거나 같을 경우
    if n >= m:
        new_arr = []
        for i in range(0, n, 2):
            new_row = []
            for j in range(m // 2):
                new_row.append(max(arr[i][2 * j], arr[i][2 * j + 1]))
            new_arr.append(new_row)
    # 배열의 가로 길이가 세로 길이보다 짧을 경우
    else:
        new_arr = []
        for j in range(0, m, 2):
            new_row = []
            for i in range(n // 2):
                new_row.append(min(arr[2 * i][j], arr[2 * i + 1][j]))
            new_arr.append(new_row)

    return new_arr

def transform_array(arr, k):
    for _ in range(k):
        arr = apply_rule(arr)
    return arr

# 예시 입력과 출력
arr1 = [[5,4,8,7],[7,3,1,2],[3,8,12,6],[11,4,5,4]]
k1 = 4
print(transform_array(arr1, k1))  # [[5]]

arr2 = [[1,2],[9,10]]
k2 = 10
print(transform_array(arr2, k2))  # [[2]]

arr3 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]]
k3 = 2
print(transform_array(arr3, k3))  # [[1,2],[9,10]]
