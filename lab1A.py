# # 1. Take 2 integers x and y as input and find whether y is divisible by x or not. For negative integers, display the message “Invalid input”.
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
# if y % x == 0:
#     print(f"{round(y)} is divisible by {round(x)}")
# else:
#     print(f"{round(y)} is not divisible by {round(x)}")

# # 2. Take an integer as input and check whether it is even or odd.
# n = int(input("Enter the number: "))
# if n % 2 == 0:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is not an even number")

# # 3. Find the area of a Circle of radius r. Only radius between 1 and 100 should be accepted.
# radius = float(input("Enter the radius of the circle: "))
# pi = 3.14
# area = pi * radius**2
# if 1 < radius < 100:
#     print("Area of the circle is",area)
# else:
#     print("Enter valid radius")

# # 4. Using the temperature conversion formula, calculate the value at which the Celsius and corresponding Fahrenheit values are the same.
# temp = float(input("Enter tenperature in celcius: "))
# f = (temp + 32) * (5/9)
# if temp == f:
#     print(f)
# else:
#     print("Temperature is not equal to Fahrenheit")

# # 5. The a value of year as input and find whether it is a leap year or not. Consider all the cases of valid and invalid inputs. Write down the test cases for the same.
# year = int(input("Enter year: "))
# if year <= 0:
#     print("Invalid input")
# else:
#     if year % 4 == 0:
#         print(f"{year} is a Leap year")
#     else:
#         print(f"{year} is not a leap year")

# # 9. You are designing a software for a bank. The bank calculates interest on their RD accounts at 7.1% p.a. You need to develop the functionality, where the user can check their returns for a given duration and for a given monthly installment amount. Note that the bank does not allow monthly installment less than Rs. 500/- and the duration of RD should be atleast 6 months.  Check for valid and invalid inputs.
# amount = int(input("Enter the amount you want to get RD: "))
# duration = int(input("Enter the duration: "))
# rd= 7.1
# if amount < 500:
#     print("Money is less than expected amount")
# elif duration < 6:
#     print("Duration is less thann 6 months")
# else:
#     i = (amount*duration*rd)/(12*100)
#     print(amount*duration + i)

#  