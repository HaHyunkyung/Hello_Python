# -*- coding: utf-8 -*-
import sys
def count_seconds_with_number(N):
    total_seconds = 0
    # 00:00:00부터 23:59:59까지의 모든 시간을 확인
    for hour in range(24):
        for minute in range(60):
            for second in range(60):
                # 시, 분, 초를 문자열로 변환하여 해당 문자열에 N이 포함되어 있는지 확인
                time_str = '{:02d}{:02d}{:02d}'.format(hour, minute, second)
                if str(N) in time_str:
                    total_seconds += 1
    
    return total_seconds

# 정수 N 입력 받기
N = int(input())

# N이 포함된 시간의 초를 계산하여 출력
result = count_seconds_with_number(N)
print(result)
