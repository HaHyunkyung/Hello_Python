import sys
N = int(input())

for i in range(N):
    if(i>=1):
        for k in range(i):
            print(" ",end="")
    print("**",end="")
    print()
