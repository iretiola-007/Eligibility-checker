
print("Grading Application.\n You must be 18+ to use this application")

name = input("Please, enter your name: ")
print(f"Hello, {name}!")
age = int(input("How old are you? "))

if age >= 18:
    print("Please accept our 'Terms of Use' below")
    terms_of_use = input("Type an answer: ")
    agree = "yes"
    no_agree = "no"
    if terms_of_use.lower() == agree:
        print("Please hold on while we redirect you....")
    else:
        print("Something went wrong :(. Please try again later")
else:
    print("You are not eligible to use this service")

print("Welcome to my app! Please fill in the details below")
pass_mark = 75
exam_score = int(input("Enter your score: "))
difference_in_score = exam_score - pass_mark
if exam_score >= pass_mark:
    print(f"Congratulations! You passed! You got {difference_in_score} marks above the pass mark")
elif exam_score >= 65:
    print("You have been put into the waiting list")
else:
    print("Try again next time :(")