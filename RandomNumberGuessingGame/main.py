import random
num_range_start=int(input("Enter the starting point of the range u want to play:>> "))
num_range_end=int(input("Enter the ending  point of the range u want to play:>> "))
num = random.randint(num_range_start,num_range_end)
while True:
    user_input=int(input("Enter the number: "))
    if (user_input==num):
        print("Right Guess")
        break
    elif (user_input<num):
        print("Ur guess is less than the actual number ")
    elif (user_input>num):
        print("Ur guess is greater than the actual number ")

