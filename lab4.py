
# 1. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and years of service and print the net bonus amount.

salary = int(input("Enter your salary: "))
experience = int(input("Enter years of experience: "))
bonus = salary * 0.05
if experience >= 5:
    print(bonus)
else:
    print("No 'BONUS'")

# 2. Write a program that reads input data from the console - a password (one line of random text) and checks if the input matches the phrase "s3cr3t!P@ssw0rd". If it matches, print "Welcome", otherwise print "Wrong password!". 

password = input("Enter password: ")
if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong 'PASSWORD'")

# 3. Write a program that reads input data from the console - the measures of a geometric shape and calculates its area. shapes: square, rectangle, circle and triangle. 
# There are four types of The first line of input is the type of shape (square, rectangle, circle, triangle):
# If the shape is a square, the next argument will be one number - the length of its side.
# If the shape is a rectangle, the next argument will be two numbers - the lengths of its sides. 
# If the shape is a circle, the next argument will be one number - the radius of the circle. 
# If the shape is a triangle, the next argument will be two numbers - its base and the corresponding altitude. 

shape = input("Enter the geometric shape: ")
if shape == "square":
    side = float(input("Enter the side of the square: "))
    area = side * side
    print("Area of the square:",round(area))
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("Area of the rectangle:",round(area))
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: ")) 
    pi = 3.14
    area =  radius * pi
    print("Area of the circle:",round(area))
elif shape == "triangle":
    base = float(input("Enter the base of the trianle: "))
    altitude = float(input("Enter the altitude of the triangle: "))
    area = (1/2) * base * altitude
    print("Area of the triangle:",round(area))

# 4. Write a program that reads two integers - hours and minutes based on a 24-hour day format and calculates what time it will be 15 minutes later. The result should be printed in the following format hh:mm. Hours should always be between 0 and 23, while minutes should always be between 0 and 59. Hours should be written with one or two digits as needed, while the minutes should always be written with two digits - add a leading zero, as needed. Example, Given the time 1:46 as input, the output displayed should be 2:01. 

hour = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
minutes += 15
if minutes >= 60:
    hour += 1
    minutes -= 60
if hour >= 24:
    hour -= 24
print(f"{hour:02d}:{minutes:02d}")

# 5. A student has to travel n kilometers. He can choose between three types of transportation:
# Taxi. Starting fee: 33.58 INR. Day rate: 37.89 INR/km. Night rate: 43.17 INR/km.
# Bus. Day / Night rate: 4.32 INR/km. Can be used for distances of a minimum of 20 km.
# Train. Day / Night rate: 2.88 INR/km. Can be used for distances of a minimum of 100 km.
# Write a program that reads the number of kilometers n and period of the day (day or night) and calculates the price for the cheapest transport. 

distance = float(input("Enter no. of kilometers: "))
if distance <= 20:
    price = 4.32 * distance
    print("Cheapest transport is bus and the price of ticket is ",round(price),"/-",sep = "")
elif distance <= 100:
    price = 2.88 * distance
    print("Cheapest transport is train and the price of ticket is ",round(price),"/-",sep = "")
else:
    period = input("Enter period: ")
    if period == "day":
        price = 37.89 * distance
        print("Your transport is taxi the price charges is ",round(price),"/-",sep = "")
    elif period == "night":
        price = 43.17 * distance
        print("Your transport is taxi the price charges is ",round(price),"/-",sep = "")

# 7. Most of the people start planning their vacations well in advance. A young programmer from Bulgaria has a certain budget (BGN is the currency of Bulgaria) and spare time in a particular season. Write a program that accepts as input the budget and season and as output displays programmer's vacation place and the amount of money they will spend. The budget determines the destination, and the season determines what amount of the budget will be spent. If the season is summer, the programmer will go camping, if it is winter – he will stay in a hotel. If it is in Europe, regardless of the season, the programmer will stay in a hotel. Each camp or hotel, according to the destination, has its price, which corresponds to a particular percentage of the budget:
# • If 100 BGN or less – somewhere in Bulgaria. Summer – 30% of the budget Winter – 70% of the budget.
# • If 1000 BGN or less – somewhere in the Balkans. Summer – 40% of the budget. Winter – 80% of the budget. 
# • If more than 1000 BGN – somewhere in Europe. Upon traveling in Europe, regardless of the season, the programmer will spend 90% of the budget. 

bgn = int(input("Enter the budget: "))
if bgn <= 100:
    season = input("Enter season: ")
    if season == "summer":
        budget = bgn * (30/100)
        print("Vacation is somwher in Bulgaria and the budget is ",round(budget),"/-",sep = "")
    elif season == "winter":
        budget = bgn * (70/100)
        print("Vacation is somwher in Bulgaria and the budget is ",round(budget),"/-",sep = "")
elif bgn <= 1000:
    season = input("Enter season: ")
    if season == "summer":
        budget = bgn * (40/100)
        print("Vacation is somwher in Balkans and the budget is ",round(budget),"/-",sep = "")
    elif season == "summer":
        budget = bgn * (80/100)
        print("Vacation is somwher in Balkans and the budget is ",round(budget),"/-",sep = "")
else:
    budget = bgn * (90/100)
    print("Vacation is somwher in Europe and the budget is ",round(budget),"/-",sep = "")

# 8. Write a program that finds all numbers in the range [1 … 1000], that end in 6. 

# Using 'while' loop 
i = 1
while i <= 1000:
    if i % 10 == 6:
        print(i)
    i += 1

# Using 'for' loop
for i in range (1,1001):
    if i % 10 == 6:
        print(i)

# 9. Write a program that reads n integers and finds their sum.

# Using 'while' loop
n = int(input("Enter no. of integers: "))
total = 0
i = 0
while i <= n:
    totla += i
    i += 1
print(total)

# Using 'for' loop
n = int(input("Enter no. of integers: "))
total = 0
for i in range (1,n+1):
    total += i
print(total)

# 10. Take a positive integer N as input and print the multiplication of its.

# Using 'while' loop
n = int(input("Enter the number for which you want table: "))
a = int(input("Enter the number where to stop the multiplication table: "))
i = 1
while i <= a:
    print(f"{n} x {i} = {n*i}")
    i += 1

# Using 'for' loop
n = int(input("Enter the number for which you want table: "))
a = int(input("Enter the number where to stop the multiplication table: "))
for i in range (1,a+1):
    print(f"{n} x {i} = {n*i}")