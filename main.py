# This program is meant to be a math trivia game where the user gives an answer to a question the program asks.

__author__ = "Liam Cunningham"


# Function definition for option 9, also instructs the function

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


# Welcome message and instructions

print("Welcome to my calculator and math trivia game!", end=' ')
print("Please select a question below by typing the number to begin!")

# end= is used here to organize the print statements. (character limit)

print("-Option 1: Easy Question")
print("-Option 2: Easy Question")
print("-Option 3: Medium Question")
print("-Option 4: Medium Question")
print("-Option 5: Hard Question")
print("-Option 6: Hard Question")
print("-Option 7: Calculator Needed for Question")
print("-Option 8: Calculator")
print("-Option 9: Factorial Calculator")

# Asks user for input to direct them to section

operation = input("Selection: ")

# Question 1 code

# If statement used to separate selection 1 from others

if operation == "1":
    print("Question 1: What is the difference of 49-21?")
    playerInput1 = input("Answer: ")
# int() Converts player input into an integer
    playerAns1 = int(playerInput1)
# If statement again to separate wrong and right answer messages
    if playerAns1 == 49 - 21:
        print("Congratulations, that is correct!")
    elif playerAns1 != 49 - 21:
        print("Incorrect, the correct answer is:", 49 - 21)

# Comments from question 1 apply to questions 2-7 as well

# Question 2 code

elif operation == "2":
    print("Question 2: What is the sum of 59+76?")
    playerInput2 = input("Answer: ")
    playerAns2 = int(playerInput2)
    if playerAns2 == 59 + 76:
        print("Congratulations, that is correct!")
    elif playerAns2 != 59 + 76:
        print("Incorrect, the correct answer is:", 59 + 76)

# Question 3 code

elif operation == "3":
    print("Question 3: What is the product of 5*20?")
    playerInput3 = input("Answer: ")
    playerAns3 = int(playerInput3)
    if playerAns3 == 5 * 20:
        print("Congratulations, that is correct!")
    elif playerAns3 != 5 * 20:
        print("Incorrect, the correct answer is:", 5 * 20)

# Question 4 code

elif operation == "4":
    print("Question 4: What is the quotient of 250/5?")
    playerInput4 = input("Answer: ")
    playerAns4 = int(playerInput4)
    if playerAns4 == 250 / 5:
        print("Congratulations, that is correct!")
    elif playerAns4 != 250 / 5:
        print("Incorrect, the correct answer is:", 250 / 5)

# Question 5 code

elif operation == "5":
    print("Question 5: What is the quotient of 59/8? Remove the remainder and round.")
    playerInput5 = input("Answer: ")
    playerAns5 = int(playerInput5)
    if playerAns5 == 59 // 8:
        print("Congratulations, that is correct!")
    elif playerAns5 != 59 // 8:
        print("Incorrect, the correct answer is:", 59 // 8)

# Question 6 code

elif operation == "6":
    print("Question 6: What is the solution to 3^4?")
    playerInput6 = input("Answer: ")
    playerAns6 = int(playerInput6)
    if playerAns6 == 3 ** 4:
        print("Congratulations, that is correct!")
    elif playerAns6 != 3 ** 4:
        print("Incorrect, the correct answer is:", 3 ** 4)

# Question 7 code

elif operation == "7":
    print("Question 7: What is the remainder of 163/9 rounded to the nearest tenth? (do not include the '.')")
    playerInput7 = input("Answer: ")
# float() used to convert player input into a floating number
    playerFloat7 = float(playerInput7)
    if playerFloat7 == 163 % 9:
        print("Congratulations, that is correct!")
    elif playerFloat7 != 163 % 9:
        ans7 = ".1"
        print("Incorrect, the correct answer is: " + ans7)

# The + operator is used to give the decimal version of the remainder.
# It adds the value of ans7 into the print statement

# Numeric operators used include +, -, *, **, /, //, and %.
# The question asked explains what each numeric operator represents and the code shows what they calculate when used.

# Simple calculator code for option 8
# The while loop allows the user to make several calculations without having to close and reopen the program

elif operation == "8":
    history = []
# line 133 defines the solution function
    solution = None
# While loop allows the user to stay in the calculator selection without having to re-run
    while True:
        sign = input("Enter a sign (+, -, *, /), type 'done' to quit, or type 'history': ")
        # The break function ends the program
        if sign == "done":
            break
        # print(history) prints the users history from the calculator loop
        elif sign == "history":
            print(history)
            break
        num1 = float(input("Input your first number: "))
        num2 = float(input("Input your second number: "))
        # The format(.2f) statement restricts the printed answer to 2 decimal places
        if sign == "+":
            solution = num1 + num2
            print("The answer is:", format(solution, '.2f'))
        if sign == "-":
            solution = num1 - num2
            print("The answer is:", format(solution, '.2f'))
        if sign == "*":
            solution = num1 * num2
            print("The answer is:", format(solution, '.2f'))
        if sign == "/":
            solution = num1 / num2
            print("The answer is:", format(solution, '.2f'))

        # The history code came from a YouTube video by SimpleCodePH, it just worked well with the calculator loop.

        history.append(solution)

# Some code and the idea came from GeeksForGeeks.com. Changes were made to the code to make it interactive.

elif operation == "9":
    option9Num = int(input("Please enter a positive whole number: "))
    # Gate the user-entered number must pass through to eliminate negatives and 0s
    if option9Num < 0 or option9Num == 0:
        print("Please enter a positive number and try again")
    # Code which calculates the factorial using the defined function (line 6)
    else:
        print("The factorial of your number is", factorial(option9Num))

# Any other entry besides a number between 1-9 results in a message explaining that the entry is invalid.

else:
    print("Invalid Entry, please select a number between 1-9")

# Works Cited:
# Kindson The Tech Pro on YouTube (https://www.youtube.com/watch?v=rNBrbt90bRk)
# tutorialspoint.com (https://www.tutorialspoint.com/python/python_strings.htm)
# SimpleCodePH on YouTube (https://www.youtube.com/watch?v=aTbNCOl8iso)
# GeeksForGeeks.com (https://www.geeksforgeeks.org)
