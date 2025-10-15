
print("How you know if you passed. You must be 18+ to use this application")

name = input("Please, enter your name: ")
print(f"Hello, {name}!")
age = int(input("How old are you? "))

if age >= 18:
    print("Please accept our 'Terms of Use' below")
    terms_of_use = input("Type an answer: ")
    if terms_of_use == "Yes":
        print("Please hold on while we redirect you....")
    else:
        print("Something went wrong :(. Please try again later")
else:
    print("You are not eligible to use this service")

print("Welcome to my app! Please fill in the details below")
pass_mark = 75
math_score = int(input("Enter your score: "))
difference_in_score = math_score - pass_mark
if math_score >= pass_mark:
    print(f"Congratulations! You passed! You got {difference_in_score} marks above the pass mark")
elif math_score >= 65:
    print("You have been put into the waiting list")
else:
    print("Try again next time :(")