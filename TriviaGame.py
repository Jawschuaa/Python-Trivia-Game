# Trivia Game with 3 different niches
# 3 lives per round
name = input("Enter your name!: ")
print("Hello " + name + ", please select a trivia game to play using numbers 1-3")

print("1. Technology")
print("2. Sports")
print("3. General Knowledge")

operation = input()
lives = 3

def incanswer():
    global lives
    lives = int(lives) - 1
    print("That's incorrect " + name + " you have " + str(int(lives)) + " lives remaining")
    if lives == 0:
        print("GAME OVER")
        quit()

def wingame():
    print("CONGRADULATIONS " + name + " YOU WON!")

def correctanswer():
    print("Thats correct " + name)

if operation == "1":
    print("Question 1. What is currently the highest valued tech company?")
    print("A. Apple")
    print("B. Tesla")
    print("C. Microsoft")
    print("D. Alibaba")
    answer = input()
    if answer == "A":
        correctanswer()
    else:
        incanswer()

    print("Question 2. What was the first tesla ever made?")
    print("A. Cybertruck")
    print("B. Model S")
    print("C. Roadster")
    print("D. Model 3")
    answer = input()
    if answer == "C":
        correctanswer()
    else:
        incanswer()

    print("Question 3: What does HTML stand for?: ")
    print("A. Hyperlink and Text Markup Language")
    print("B. Hyper Text Markup Language")
    print("C. Hyper Transfer Markup Language")
    print("D. High Tech Markup Language")
    answer = input()
    if answer == "B":
        correctanswer()
    else:
        incanswer()

    print("Question 4: Which company developed the popular web browser named Chrome?: ")
    print("A. Microsoft")
    print("B. Apple")
    print("C. Google")
    print("D. Yahoo")
    answer = input()
    if answer == "C":
        correctanswer()
    else:
        incanswer()

    print("Question 5: What is used to store data on a computer?: ")
    print("A. SSD")
    print("B. Hard Drive")
    print("C. RAM")
    print("D. Both A&B")
    answer = input()
    if answer == "D":
        correctanswer()
        wingame()
    else:
        incanswer()

if operation == "2":
    print("Question 1: What is the record for most wins in a regular NBA season?: ")
    print("A. 72-10")
    print("B. 70-12")
    print("C. 73-9")
    print("D. 82-0")
    answer = input()
    if answer == "C":
        correctanswer()
    else:
        incanswer()

    print("Question 2: What is known as Americas Sport?: ")
    print("A. Baseball")
    print("B. Basketball")
    print("C. Football")
    print("D. Soccer")
    answer = input()
    if answer == "A":
        correctanswer()
    else:
        incanswer()

    print("Question 3: What athlete has the most olympic gold medals?: ")
    print("A. LeBron James")
    print("B. Lionel Messi")
    print("C. Michael Jordan")
    print("D. Michael Phelps")
    answer = input()
    if answer == "D":
        correctanswer()
    else:
        incanswer()

    print("Question 4: What vehicle does the term F1 refer to?: ")
    print("A. Race cars")
    print("B. Monster trucks")
    print("C. Motorcycles")
    print("D. Trick Question")
    answer = input()
    if answer == "A":
        correctanswer()
    else:
        incanswer()

    print("Question 5: What is the most popular sport in the world?: ")
    print("A. Cricket")
    print("B. Rugby")
    print("C. Soccer")
    print("D. Tennis")
    answer = input()
    if answer == "C":
        correctanswer()
        wingame()
    else:
        incanswer()

if operation == "3":
    print("Question 1: The Statue of Liberty was a gift from which country?: ")
    print("A. England")
    print("B. Japan")
    print("C. France")
    print("D. America")
    answer = input()
    if answer == "C":
        correctanswer()
    else:
        incanswer()

    print("Question 2: Which country has the biggest landmass?: ")
    print("A. Russia")
    print("B. Canada")
    print("C. China")
    print("B. Austria")
    answer = input()
    if answer == "A":
        correctanswer()
    else:
        incanswer()

    print("Question 3: What yea did Christopher Colombus sail the ocean blue?: ")
    print("A. 1823")
    print("B. 1491")
    print("C. 1776")
    print("D. 1492")
    answer = input()
    if answer == "D":
        correctanswer()
    else:
        incanswer()

    print("Question 4: What color shows up in the most National flags?: ")
    print("A. Red")
    print("B. Green")
    print("C. Blue")
    print("D. White")
    answer = input()
    if answer == "A":
        correctanswer()
    else:
        incanswer()

    print("Question 5: What is python?: ")
    print("A. A snake")
    print("B. A coding language")
    print("C. A food")
    print("D. A car")
    answer = input()
    if answer == "B":
        correctanswer()
        wingame()
    else:
        incanswer()
        wingame()