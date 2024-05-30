# -*- coding: utf-8 -*-
import sys
def check_dishwashing_day(day_number):
    dishwashing_days = [1, 3, 5, 7]  # 설거지를 하는 요일의 번호

    if day_number in dishwashing_days:
        return "RUN"
    else:
        return "STAY"

# 입력 받기
day_number = int(input())

# 결과 출력
result = check_dishwashing_day(day_number)
print(result)
