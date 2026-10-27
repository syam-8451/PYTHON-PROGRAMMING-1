# 1. Write a program that prompts the user to enter the three points (x1, y1) , (x2, y2) , and (x3 , y3) of a triangle and displays its area. The formula for computing the area of a triangle is 
# s = (side1 + side2 + side3) / 2 
# area = √[s(s - side1)(s - side2)(s – side3)]

x1,y1 = map(int,input("Enter x1 and y1: ").split())
x2,y2 = map(int,input("Enter x2 and y2: ").split())
x3,y3 = map(int,input("Enter x3 and y3: ").split())
side1 = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
side2 = ((x3-x2)**2 + (y3-y2)**2)**(1/2)
side3 = ((x1-x3)**2 + (y1-y3)**2)**(1/2)
s = (side1 + side2 + side3) / 2
area = (s*(s - side1)*(s - side2)*(s - side3))**(1/2)
print(f"Area of the triangle is {area:.2f}")

# 2. Write a program that prompts the user to enter the side of a hexagon and displays its area. The formula for computing the area of a hexagon is Area = (3√3 / 2) * s^2 , where s is the length of a side. 

n = float(input("Enter the length of the side of the hexagon: "))
area = ((3*(3**(1/2)))/2) * n**2
print(f"Are of hexagon is {area:.2f}")

# 3. Take 3 numbers as input, and find whether they form the sides of a triangle or not. Consider invalid cases also. 

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
if x < 0 or y < 0 or z < 0:
    print("Enter valid input.")
else:
    print(f"{x}, {y} and {z} can form a triangle.")

# 4. Take a 3 digit number as input and find the sum of its digits. Also, check if the sum is divisible by 3 or not.

n = int(input("Enter a three digit number: "))
n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10
total = n1 + n2 + n3
if total % 3 == 0:
    print("The sum of three digits is divisible by 3.")
else:
    print("The sum of three digits is not divisible by 3.")

# 5. Take a 5 digit number as input and print the reverse of the number. Do not use any in-built functions for reversing. Check whether the input number and the reversed number are the same. If so, print “Number is Palindrome”, else print “Number is not Palindrome”.

n = int(input("Enter a five digit number: "))
n1 = n // 10000
n2 = (n // 1000) % 10
n3 = (n // 100) % 10
n4 = (n // 10) % 10
n5 = n % 10
reverse = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
if reverse == n:
    print("Given number is a palindrome.")
else:
    print("Given number is not a palindrome.")

# 6. Take a 3 digit number as input. Check if it is an Armstrong number or not. E.g. 1^3 + 5^3 + 3^3 = 153

n = int(input("Enter a three digit number: "))
n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10
if n1**3 + n2**3 + n3**3 == n:
    print("Given number is an amstrong number.")
else:
    print("Given number is not an amstrong number.")

# square star pattern with diagonal in it
n = int(input())
for i in range (1,n+1):
    for j in range (1,n+1):
        if i == 1 or j == 1 or i == n or j == n or i == j:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()

# Alphabetical reverse right angled triangle
n = input()
s = len(n)
for i in range (s):
    print(" "*(s-i),end = "")
    for j in range (i+1):
        print(n[j].upper(),end = "")
    print()
    