# BMI Calculator

height = float(input("Enter your Height in centemeter : "))
weight = float(input("Enter your weight : "))

new_height = height/100
BMI = weight/(new_height * new_height)
print("Your body mass index is : ",BMI)

if BMI > 0:
    if BMI <= 16:
        print("You are severly underweight")
    elif BMI <= 18.5:
        print("You are underweight!")
    elif BMI <= 25:
        print("Your are healthy!")
    elif BMI <= 30:
        print("You are overweight !")
    else:
        print("You are severly overweight")
else:
    print("Enter Valid details.")