print("Welcome to my Quiz Game!")

ask = input("Would you like to play ? (yes/no)")

if ask.lower() != "yes":
    quit()

print("Okay! Let's play :)")

name = input("What should we call you? ")

print(f"Lets begin with the quiz {name.upper()}")

score = 0
question = 0

answer = input("W")
if answer.lower() == "a":
    print('Correct!')
    question += 1
    score += 4
else:
    print("Incorrect!")
    score -= 1

answer = input("W")
if answer.lower() == "a":
    print('Correct!')
    question += 1
    score += 4
else:
    print("Incorrect!")
    score -= 1

print("You answered " + str(question) + " questions correctly, earning a score of " + str(score) + ".")