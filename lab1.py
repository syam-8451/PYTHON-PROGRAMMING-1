'''
# 1. Write a Python program to display 'Hello JKLU!' and 'I am learning Python.'

print("Hello JKLU")
print("I'm learning python")

# 2. Accept the student's name and branch as input and display a welcome message.

name = input("Enter students name: ")
branch = input("Enter students branch: ")
print("Hello!"+name+",welcome to JKLU.Your branch is",branch)

# 3. Input the length and width (in metres) of a rectangular plot and calculate its area.

length = int(input("Enter length of the rectangle in meters: "))
width  = int(input("Enter width of rectangle in meters: "))
area = length * width
print("Area of rectangle:",area)

# 4. Modify Problem 3 to accept dimensions in feet and display the area in square metres. 

a = int(input("Enter length of the rectangle in feets: "))
b = int(input("Enter width of the rectangle in feets: "))
a_meters = a * 0.3048
b_meters = b * 0.3048
area = a_meters * b_meters
print(f"Area of rectangle: {area:.4f}sq.meters")

# 5. Input two positive integers x and y. Check whether y is divisible by x. For negative inputs, display 'Invalid Input'. 

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
if x < 0 or y < 0:
    print("Invalid input")
elif y % x ==0 :
    print(y," is divisible by", x)
    
# 6. Input an integer and determine whether it is even or odd. 

n = int(input("Enter your number: "))
if n % 2 == 0:
    print(n,"is even")
else:
    print(n,"is odd")
    
# 7. Input the radius of a circle (1–100 only) and calculate its area. Handle invalid inputs.
 
r = int(input("Enter radius of circle: "))
pi = 3.14
area = pi*r**2
if r <= 0 or r > 100:
    print("Invalid input")
else:
    print("Area of circle:",area)
    
# 8. Input temperature in Celsius and display the equivalent Fahrenheit and Kelvin values.

temp = float(input("Enter temparature in celcius: "))
F = (temp + 32)*(5/9)
K = temp + 273.15
print(f"Temparature in fahrenheit = {F}F")
print(f"Temparature in kelvins = {K}K")

# 9. Input the number of seconds (1-86400) and display the equivalent time in HH:MM: SS format. 

n = int(input("Enter time in seconds: "))
hour = n // 3600
min = (n % 3600) // 60
sec = (n % 3600) % 60
if 0 <= n or n > 86400:
    print("Invalid input")
else:
    print(f"{hour:02d}:{min:02d}:{sec:02d}")
    
# 10. Mini Challenge (Choose ONE):  
# (a) Attendance Percentage Calculator (eligible if attendance ≥75%), OR  
# (b) Simple Electricity Bill Calculator, OR  
# (c) ATM PIN Validation (4-digit PIN). 

# (a)

n = int(input("Enter your attendence percentage: "))
if n >= 75:
    print("Eligible")
else:
    print("Not eligible")
    
# (b)
# calculating electricity bill (Taking aproximate prices per unit) based on the units conserved

n = int(input("Enter no of units: "))
if 0 < n <= 100:
    print("Electricity bill = ",n*4)
elif 100 < n <= 200:
    print("Electricity bill = ",100*4 + (n-100)*5)
elif 200 < n <= 300:
    print("Elsectricity bill = ",200*5 + (n-200)*6)
else:
    print("Electricity bill = ",300*6 + (n-300)*7 )
    
# (c)
# Checking ATM pin

n = int(input("Enter your PIN: "))
if 1000 <= n < 10000:
    if n == 4862:
        print("Valid PIN")
    else:
        print("Invalid PIN")
else:
    print("Invalid PIN formate")'''