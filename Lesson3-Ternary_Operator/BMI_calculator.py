height = float(input("What's your height(in)? "))
weight = float(input("What's your weight(lb)? "))

BMI = (weight / (height * height)) / 703
category = ("Underweight" if BMI < 18.5 else
            "Normal" if 18.5 <= BMI <= 25 else
            "Overweight" if 25 <= BMI <= 30 else
            "Obese"
            )
print(f"BMI: {BMI}")
print(f"Category: {category}")
