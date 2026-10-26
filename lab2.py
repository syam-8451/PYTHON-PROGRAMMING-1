
# 1. Write a program to display “Hi” if the number entered by user is divisible by 5, otherwise print “Bye”. 

n = int(input("Enter your number: "))
if n % 5 == 0:
    print("Hi")
else:
    print("Bye")

# 2. If the lengths of the two parallel sides of a trapezoid are X meters and Y meters, respectively, and the height is H meters, what is the area of the trapezoid? Write Python code to output the area by taking X, Y and H as input from the user.

x = int(input("Enter the length of logest side in meters: "))
y = int(input("Enter the length of shortest side in meters: "))
h = int(input("Enter the height in meters: "))
area = (1/2)*(x + y)*h
print(area,"sq. meters")

# 3. Write a program that interprets the Body Mass Index (BMI) based on a user’s weight and height. It should tell them the interpretation of their BMI based on the BMI value.
# • Under 18.5 they are underweight 
# • Over 18.5 but below 25 they have a normal weight 
# • Over 25 but below 30 they are slightly overweight 
# • Over 30 but below 35 they are obese 
# • Above 35 they are clinically obese. 

w = float(input("Enter weight in KG: "))
h = float(input("Enter height in meters: "))
BMI = w/(h**2)
if BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normalweight")
elif BMI <= 30:
    print("Slightly overweight")
elif BMI <= 35:
    print("Obese")
else:
    print("Clinically obese")

# 4. Write a Python program to check whether an alphabet is a vowel or consonant. 

n = input("Enter your letter: ")
n = n.lower()
if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
    print("Vowel")
else:
    print("Consonant")

# 5. Suppose a surface initially contained 2.19x10^14 bacterial cells. After some time, the surface contained 4.68x10^14 bacterial cells. Calculate the percentage of bacterial growth. Display the answer rounded to the nearest whole number. 

n = float(input("Enter no. of bacteria initially: "))
s = float(input("Enter no. of bacteria finally: "))
percentage_growth = (s - n)* 100
print(round(percentage_growth),"%")

# 6. Write a program that asks the user to enter a whole number of months as input and then converts that amount of time to years and months. The program should use both integer division and the modulus operator. 

months = int(input("Enter no. of months: "))
years = months // 12
months = months % 12
print(years,"years",months,"months")

# 7. The color of the beacon light atop Boston’s old John Hancock building forecasts the weather according to the following rhyme: 
# Steady blue, clear view.  
# Flashing blue, clouds due.  
# Steady red, rain ahead.  
# Flashing red, snow instead.  
# Write a program  that requests a color (Blue or Red) and a mode (Steady or Flashing) as input and then displays the weather forecast. 

color = input("Enter color: ").capitalize()
mode = input("Enter mode: ").capitalize()
if  color == "Blue":
    if mode == "Steady":
        print("Clear view")
    elif mode == "Flashing":
        print("Clouds due")
elif color == "Red":
    if mode == "Steady":
        print("Rain ahead")
    elif mode == "Flashing":
        print("Snow instead")

# 8. Write a program that requests the costs and revenue for a company and displays the message “Break even” if the costs and revenue are equal; otherwise, it displays the profit or loss.

cost = int(input("Enter total cost: "))
revenue = int(input("Enter total revenue: "))
if cost > revenue:
    print("Loss")
elif cost == revenue:
    print("Break even")
else:
    print("Profit")

# 9. A store sells widgets at 25 cents each for small orders or at 20 cents each for orders of 100 or more. Write a program that requests the number of widgets ordered and displays the total cost. 

n = int(input("Enter no. of widgets: "))
if n < 100:
    print("No. of widgets =",n)
    print("Total cost =",n*25)
else:
    print("No. of widgets =",n)
    print("Total cost =",n*20)

# 10. A supermarket sells apples for $2.50 per pound. Write a cashier’s program that requests the number of pounds and the amount of cash tendered as input and displays the change from the transaction. If the cash is not enough, the message “You owe $x.xx more.” should be displayed, where $x.xx is the difference between the total cost and the cash. 

n = int(input("Enter no. of pounds of apples: "))
cash = int(input("Total cash given: "))
total_cost = n*2.50
if total_cost > cash:
    print("You owe $",total_cost-cash,"more.")
elif cash < total_cost:
    print("Take your change $",cash-total_cost)
else:
    print("You have given the exact amount")

# 11. Find the largest of 3 numbers using nested if else condition.

a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(a,"is largest among the given three numbers")
    else:
        print(c,"is largest among the given three numbers")
elif b > c:
    print(b,"is largest among the given three numbers")
else:
    print(c,"is largest among the given three numbers")

# 12. Calculate the gross salary of an employee by taking as input the basic Salary. HRA = 20% of basic salary, TA is 5% of basic salary, and DA is 10% of basic salary. Gross Salary = Basic Salary + HRA + TA + DA.

basic = int(input())
HRA = basic * (20/100)
TA = basic * (5/100)
DA = basic * (10/100)
Gross_salary = basic + HRA + TA + DA
print("Gross salary =",Gross_salary)

# 13. Further, in the above question, find the income tax slab in which the employee lies. 
# Gross Salary                      Income Tax
# < Rs. 3 LPA                           0%
# Rs. 3,00,000 – Rs. 10,00,000      10% of the gross salary 
# Rs. 10,00,000 – Rs. 25,00,000     20% of the gross salary 
# Above Rs. 25,00,000               30% of the gross salary 

basic = int(input())
HRA = basic * (20/100)
TA = basic * (5/100)
DA = basic * (10/100)
Gross_salary = basic + HRA + TA + DA
if Gross_salary < 300000:
    print("Tax =",0)
elif 300000<= Gross_salary < 1000000:
    print("Tax =",Gross_salary * (10/100))
elif 1000000 <= Gross_salary < 2500000:
    print("Tax =",Gross_salary * (20/100))
else:
    print("Tax =",Gross_salary * (30/100))

# 14. The flowchart given below calculates a person’s state income tax. Write a program

income = int(input("Enter employees income: "))
if income <= 20000:
    set_tax = 0.02 * income
    print(set_tax)
elif income <= 50000:
    set_tax = 400 + 0.025 * (income - 20000)
    print(set_tax)
else:
    set_tax = 1150 + 0.035 * (income - 50000)
    print(set_tax)