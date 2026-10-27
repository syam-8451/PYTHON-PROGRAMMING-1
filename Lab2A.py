# # 1. Write a program to display “Hi” if the number entered by user is divisible by 5, otherwise print “Bye”. 

# n = int(input("Enter the number: "))
# if n % 5 == 0:
#     print("Hi")
# else:
#     print("Bye")

# # 2. If the lengths of the two parallel sides of a trapezoid are X meters and Y meters, respectively, and the height is H meters, what is the area of the trapezoid? Write Python code to output the area by taking X, Y and H as input from the user.
#  
# x = float(input("Enter the length of side X: "))
# y = float(input("Enter the length of side Y: "))
# h = float(input("Enter the length of heght: "))
# area = (x + y) * h * (1/2)
# print(F"Area of trepezoid is {area}m^2")

# # 3. Suppose a surface initially contained 2.19x1014 bacterial cells. After some time, the surface contained 4.68x1014 bacterial cells. Calculate the percentage of bacterial growth. Display the answer rounded to the nearest whole number.
#  
# n1 = float(input("Enter the initial no. of bacteria: "))
# n2 = float(input("Enter the final no. of bacteria: "))
# percentage = ((n2-n1)/n1) * 100
# print(f"Percentage growth of bacteria is {percentage:.2f}")

# # 4. Write a program that asks the user to enter a whole number of months as input and then converts that amount of time to years and months. The program should use both integer division and the modulus operator. 
# 
# months = int(input("Enter the no. of month(s): "))
# years = months // 12
# months = months % 12
# print(f"{years} year(s) and {months} month(s)")