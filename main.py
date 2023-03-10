print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to be taller before you can ride.")
  
  
#BMI Calculator Nested Elif
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round((weight / height ** 2))
if BMI < 18.50:
    print(f"Your BMI is {BMI}, you are underweight")
elif 18.50 < BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight") 
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight") 
elif 30 < BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
elif 35 < BMI:
    print(f"Your BMI is {BMI}, you are clinically obese") 

    
#Leap year checker
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leapyear = year % 4
if leapyear == 0:
    leapyear2 = year % 100
    if leapyear2 == 0:
        leapyear3 = year % 400
        if leapyear3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
    
#Pizza Order exercise
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    bill = 15     
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
if add_pepperoni == "Y":
    bill = bill + 2 if size == "S" else bill + 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")

#Love Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_name= (name1 + name2).lower()
truecount = total_name.count("t")+total_name.count("r")+total_name.count("u")+total_name.count("e")
lovecount = total_name.count("l")+total_name.count("o")+total_name.count("v")+total_name.count("e")
lovescore = int(str(truecount) + str(lovecount))

if lovescore > 90 or lovescore < 10:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore > 40 and lovescore < 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")

#treasure island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
crossroad = input("You're at a crossroad. Which way do you want to go? Type 'left' or 'right'.")
if crossroad == "left":
  lakepoint = input("You're now at a lake. Do you want to swim or wait for the boat? Type 'swim' or 'wait'")
  if lakepoint == "swim":
    print("You got attacked by a trout and died. Game Over.")
  elif lakepoint == "wait":
    door = input("The boat has arrived and brought you to the island. Now there are three doors. Which door do you choose? Type 'red' , 'blue', or 'yellow'.")
    if door == "red":
      print("Flames burst out and burned you. You have died. Game over.")
    elif door == "blue":
      print("A beast came out and ate your face and you died. Game over.")
    elif door == "yellow":
      print("There's the treasure! You win! Congrats!")
elif crossroad == "right":
  print("You fell into a hole and died. Game Over.")    

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to be taller before you can ride.")
