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
