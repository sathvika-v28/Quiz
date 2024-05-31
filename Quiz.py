print("Welcome to the game")
play = input("Do you want to play the game? ")

if play.lower() != "yes":
    quit()

print("Yayy! Let's play")

score = 0

answer = input("What is the full form of HTML? ")
if answer.lower() == "hypertext markup language":
    print("Correct :)")
    score+=1
else:
    print("Incorrect :(")

answer = input("What is the full form of SQL? ")
if answer.lower() == "structured query language":
    print("Correct :)")
    score+=1
else:
    print("Incorrect :(")

answer = input("What is the full form of CSS? ")
if answer.lower() == "cascading style sheets":
    print("Correct :)")
    score+=1
else:
    print("Incorrect :(")

answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct :)")
    score+=1
else:
    print("Incorrect :(")

print("Your score is " + str(score))
print("Your percentage of score is " + str((score/4)*100))

