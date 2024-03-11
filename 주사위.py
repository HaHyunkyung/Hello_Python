def find_dice_combinations(N):
    # 주사위의 눈금은 1부터 6까지이므로 가능한 경우의 수를 찾습니다.
    for i in range(1, 7):
        # 두 번째 주사위의 눈금을 계산합니다.
        j = N - i

        # 두 번째 주사위의 눈금이 1부터 6까지의 범위에 속하면 출력합니다.
        if 1 <= j <= 6:
            # 두 주사위의 눈금을 오름차순으로 출력합니다.
            print(f"{i} {j}")

# 사용자로부터 합 N을 입력받습니다.
N = int(input("합 N을 입력하세요: "))

# 함수를 호출하여 경우의 수를 출력합니다.
find_dice_combinations(N)
