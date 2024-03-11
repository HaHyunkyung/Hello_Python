import sys

def time(hour, minute):
    if minute <30:
        if hour == 0 :
            hour = 23
        elif hour !=0 :
            hour -= 1
        minute = 60 + minute - 30
    elif minute>=30 :
        minute -= 30
    return hour, minute
hour, minute = map(int, input().split())
pt_hour,pt_minute = time(hour,minute)
print(pt_hour,end=" ")
print(pt_minute)