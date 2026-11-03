## This Program:
# - asks a number
# - checks and prints if number is positive, negative, or nul


user_number = int(input("Give any number: "))

if user_number > 0:
    print("Number is Positive")
elif user_number < 0:
    print("Number is Negative")
else:
    print("Number is NUL")
