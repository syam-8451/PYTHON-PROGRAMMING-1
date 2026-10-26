
# 1. Take 2 numbers as input (X and Y) and a third number N. Display all the numbers between X and Y (X < i <= Y) that are divisible by N. 

# Using 'while' loop
x = int(input("Enter the starting number: "))
y = int(input("Enter the last number: "))
n = int(input("Enter the number which you want to divide: "))
while x <= y:
    if x % n == 0:
        print(x)
    x += 1

# Using 'for' loop
x = int(input("Enter the starting number: "))
y = int(input("Enter the last number: "))
n = int(input("Enter the number which you want to divide: "))
for i in range (x,y+1):
    if i % n == 0:
        print(i)

# 2. Take a positive integer as input and display the sum of its digits. The number can be of any length. 

n = int(input("Enter the number: "))
total = 0
while n != 0:
    d = n % 10
    total += d
    n = n // 10
print(total)

# 3. Take a positive integer N as input followed by repeatedly taking numbers from the user till the time user entered -999. At the end display the count of input numbers that are divisible by N and the count of input numbers that are not divisible by N.

n = int(input("Enter the number: "))
count1 = 0
count2 = 0
a = 0
while a != -999:
    a = int(input())
    if a % n == 0:
        count1 += 1
    else:
        count2 += 1
print("No. of numbers divisible by given number:",count1)
print("No. of numbers not divisible by given number:",count2)

# 4. Take a positive integer N as input and find its Factorial using a while loop. Handle invalid cases as well. 

n = int(input("Enter the number that you want to fing factorial: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("The factrial of the given number is:",fact)

# 5. Take a positive integer as input. It may be of any length. Check if it is palindrome or not. Do not use any inbuilt reverse functions. 

n = int(input("Enter the number: "))
s = n
rev = 0
while n != 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
if rev == s:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")

# 6. Display the first N terms of the Fibonacci sequence starting from 1. 
# 1, 1, 2, 3, 5, ….. till N terms 

n = int(input())
a = 0
b = 1
print(b)
while b <= n:
    c = a + b                            # gets the sum of previous numbers
    a = b                                # Updates the first number
    b = c                                # Updates the second number
    print(c)

# 7. Take an integer as input and check if it is prime or not. Handle invalid conditions and make your code efficient by minimizing the number of loop iterations.

n = int(input("Enter the number: "))
count = 0
if n <= 0:
    print("Enter positive number")
else:
    for i in range (1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Given number is a prime number")
    else:
        print("Given number is not a prime number")

# 8. Take a sentence as input and using while loop count the number of capital letters, small letters, digits, and special characters in the sentence. Do not use any inbuilt function.

n = input("Enter the sentence: ")
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in n:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count1 += 1
    elif i in "abcdefghijklmnopqrstuvwxyz":
        count2 += 1
    elif i in "1234567890":
        count3 += 1
    else:
        count4 += 1
print("No. of Capital letters are:",count1)
print("No. of Small letters are:",count2)
print("No. of Digits letters are:",count3)
print("No. of Special charecters letters are:",count4)