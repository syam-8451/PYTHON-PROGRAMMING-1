
# 1. Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and a second point (x2, y2), and displays whether the second point lies inside, on the boundary of, or outside the circle. 
# The formula for computing the distance between two points is distance = √[(x2 – x1)2 + (y2 – y1)2]
x1 , y1 = map(int , input().split())
x2 , y2 = map(int , input().split())
r = int(input("Enter radius of the circle: "))
dis = ((x2-x1)**2 + (y2-y1)**2)**0.5
if r > dis:
    print(f"({x2},{y2}) lies inside the circle")
elif r == dis:
    print(f"({x2},{y2}) lies on the boundary")
else:
    print(f"({x2},{y2}) lies outside of the circle")

# 2. Write a program that prompts the user to enter the side of a regular pentagon and displays its area. The formula for computing the area of a pentagon is Area = (5 * s^2) / (4 * tan(π / 5)), where s is the length of a side.

s = int(input("Enter the side of regular pentagon: "))
Area = (5 * s**2) / (4 * 0.7265)
print(round(Area))

# 3. Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can, further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases also.

a = int(input("Enter angle a: "))
b = int(input("Enter angle b: "))
c = int(input("Enter angle c: "))
if a + b + c != 180:
    print("Enter valid angles")
elif a <= 0 or b <= 0 or c <= 0:
    print("Invalid angles")
elif a < 90 and b < 90 and c < 90:
    print("Acute angled triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right angled triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse angled traingle")

# 4. Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two digits separately. Also, check if the two sums are equal or not.

n = int(input("Enter 4 digit number: "))
n1 = n //1000
n2 = (n // 100) % 10
n3 = (n // 10) % 10
n4 = n % 10
if n1 + n2 == n3 + n4:
    print("Equal")
else:
    print("Not Equal")

# 5. Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built functions and do not use loops. Also print the position of that digit counted from the left. If the largest digit occurs more than once, print the position of its first occurrence.

n = int(input("Enter 5 digit number: "))
n1 = n // 10000
n2 = (n // 1000) % 10
n3 = (n // 100) % 10
n4 = (n // 10) % 10
n5 = n % 10
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 :
    print(f"{n1} is largest an it's position is 1 from left")
elif n2 > n3 and n2 > n4 and n2 > n5:
    print(f"{n2} is largest an it's position is 2 from left")
elif n3 > n4 and n3 > n5:
    print(f"{n3} is largest an it's position is 3 from left")
elif n4 > n5:
    print(f"{n4} is largest an it's position is 4 from left")
else:
    print(f"{n5} is largest an it's position is 5 from left")
    
# 6. Rotate the values of three integer variables cyclically, so that the value of a moves to b, the value of b moves to c, and the value of c moves to a, without using a fourth variable or multiple assignment operation.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
a,b,c = b,c,a
print(round(a))
print(round(b))
print(round(c))

# 7. Take a 3 digit number as input. Check if it is a Harshad number or not, i.e. whether the number is exactly divisible by the sum of its digits. E.g. 1 + 5 + 3 = 9 and 153 / 9 = 17, so 153 is a Harshad number.

n = int(input("Enter 3 digit number: "))
n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10
sum = n1 + n2 + n3
if n % sum == 0:
    print(f"{n} is a harshad number")
else:
    print(f"{n} is not a harshad number")