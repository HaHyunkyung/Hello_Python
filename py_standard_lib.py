from random import randint

user_choice = int(input("Choose number."))
pc_choice = randint(1,50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer choice", pc_choice)
     