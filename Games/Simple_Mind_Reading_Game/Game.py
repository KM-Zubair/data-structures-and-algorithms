#Using import
import time

#Using function
def Number():
    print("Okay then, Let's start ")
    time.sleep(1)
    print("Pick any number between 0 to 9")
    time.sleep(2)
    print("Multiply that number by 2")
    time.sleep(2)
    print("Add 5 to the new number")
    time.sleep(2)
    print("Now Multiply the answer by 5")
    time.sleep(2)
    print("Remember this answer")
    time.sleep(3)
    print("Now pick another number between 0 to 9")
    time.sleep(2)
    print("Add this number with the previous answer")
    time.sleep(2)
    print("Now tell me the answer, I am gonna guess the two numbers that you picked.")

    guess = int(input())
    a = guess - 25
    b = str(a)

    #Using list
    numbers = list(map(int, b))
    print("Alright," + Name + ", let me guess ...")
    time.sleep(3)
    print("The first and second number you guessed were " + str(numbers))
    print("Ohhoo, got you again !\n")
    time.sleep(2)
    print("Want to play the answer game? Type yes or no .")
    Y = input()
    if Y == "YES" or Y == "yes":
        Answer()
    else :
        exit()

#Using function
def Answer():
    print("Okay, Let's start then.")
    print("Think of a number, any number.")
    time.sleep(2)
    print("Now multiply it by two.")
    time.sleep(2)
    print("Add 10 to your total.")
    time.sleep(2)
    print("Now divide yor total by two.")
    time.sleep(2)
    print("Finally, Substract the total from the First number you picked")
    time.sleep(3)
    print("Let me guess, " + Name + ", your answer is ...")
    time.sleep(2)
    print("5, isn't it ? Got you !\n")
    time.sleep(1)

    print("Want to play the number game? Type yes or no .")
    Y = input()
    if Y == "YES" or Y == "yes":
        Number()
    else:
        exit()

#Using function
def Answer1():
    print("Alright, let's start !")
    time.sleep(1)
    print("Pick a 3 digit number with 3 different digits")
    time.sleep(2)
    print("Now reverse the digits to get a new number.Like if the digits"
          " you took were 123 then reversed digit will be 321")
    time.sleep(4)
    print("Now you have two numbers. The one you guessed and the other one you reversed")
    time.sleep(2)
    print("Substract the smaller number from the larger number.")
    time.sleep(2)
    print("Add up the digits of your result. Like if your result is "
          "481 then you will add 4 + 8 + 1")
    time.sleep(4)
    print("Done ? Now let me guess...")
    time.sleep(3)
    print("After adding the digits, the answer is 18. Isn't it ?")
    time.sleep(2)
    print("Ohhoo,"+ Name + ", I got you !")

    print("Want to play the number game? Type yes or no .")
    Y = input()
    if Y == "YES" or Y == "yes":
        Number()
    else:
        exit()

if __name__ == "__main__":
    print("Please type your name")
    Name = input()
    print("Hey " + Name + " !! ")
    time.sleep(1)
    print(
        "You will get to Guess Numbers and I will tell you to calcualte them in your mind, \nlater I will tell you either the numbers you guessed or the answer.\n")
    time.sleep(4)
    print("So tell me, Which one do you want to try?\n")
    time.sleep(3)
    print("I will tell you the Two Numbers you guessed? ")
    time.sleep(1)
    print("Or")
    time.sleep(1)
    print("I will tell you the The Answer you get after guessing a number? \n")
    time.sleep(1)
    print("Type N for NUMBER or A for ANSWER")
    X = input()

    if X == "N" or X == "n":
        Number()
    elif X == "A" or X == "a":
        print("You want to guess any number ?  ")
        print("Or")
        print("you want to guess a number with three digits ?")
        time.sleep(1)
        print("Please type 'any' for guessing any number or type '3' for guessing a 3 digit number")
        Y = input()
        if Y == "any" or Y == "Any":
            Answer()
        elif Y == "3":
            Answer1()
        else:
            print("Please type 'any' or '3' only.")
    else:
        print("Type N or A only")

