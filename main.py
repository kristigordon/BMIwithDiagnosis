print("Welcome! Congratulations for taking your first step on your journey to better health")
weight = input("Let's start by getting your weight\n")
height = input("What is your height? Insert height in meters = 1.75\n")
bmi = int(weight) / float(height) ** 2
bmiFinal = int(bmi)
print("Your BMI is " + str(bmiFinal))

#Under 18.5 they are underweight
if int(bmiFinal) < 18.5:
    print("You are underweight")

#Over 18.5 but below 25 they have a normal weight

elif ((int(bmiFinal) > 18.5) and (int(bmiFinal)< 25)):
    print("You are a great weight")

#Over 25 but below 30 they are slightly overweight
elif ((int(bmiFinal) > 25) and (int(bmiFinal)< 30)):
    print("You are slightly overweight")

#Over 30 but below 35 they are obese
elif ((int(bmiFinal) > 30) and (int(bmiFinal)< 35)):
    print("You are obese")

#Above 35 they are clinically obese.
else:
    print("You are clinically obese")