'''
# 1. Write a program to reverse a string without using inbuilt function.
n = input()
rev = ""
for ch in n:
    rev = ch + rev
print(rev)

# 2. Write a program to find the length of the last word in a sentence. 
n = input()
rev = ""
count = 0
for ch in n:
    rev = ch + rev
b = ""
for j in rev :
    if j == " ":
        break
    b = j + b
print(len(b))
print(b)

# 3. Take a sentence and a word as input and check if the string contains the word in it. Also, count the number of times that word occurs in the string. Do this by using inbuilt string functions and then without using inbuilt string functions. 
n = input()
word = input()
if word in n:
    print("Yes the given sentence contains the word")
    print(n.count(word),"time(s)")
else:
    print("No such word found")

# 4. A program that takes a string as input and checks where the string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog" 
n = input()
count = 0
for ch in n:
    if ch in "abcdefghijklmnopqrstuvwxyz":
        count += 1
if count >= 26:
    print("The given sentence is a pangram")
else:
    print("The given sentence is not a pangram")

# 5. The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”. Take a string as input from user which contains English alphabets only in lower or upper case. Also, take the shift (an integer) as input from the user. Write a program to convert the string into its corresponding Ceaser Cipher which also contains English alphabets only. 
n = input()
key = int(input())
new = ""
for i in n:
    if i != " ":
        k = ord(i)+key
        if k > 122:
            k = 96 +(k-122)
            new += chr(k)
        else:
            new += chr(k)
    elif i == " ":
        new += i
print(new)

# 6. Repeatedly take input from the user in the range of 1 – 10 till the time they enter -1. It then displays the histogram shown as follows. Note that the percentage values are displayed till 2 decimal places: 
# 1 - 2: # # # # # # # # # # 52.00 %
# 3 – 4: # # # # # # 28.00 % 
# 5 – 6: # 4.00 %
# 7 – 8: 0.00 %
# 9 – 10: # # # 16 % 
a = b = c = d = e = 0
total = 0
while True:
    n = int(input())
    if n == -1:
        break
    elif 1 <= n <= 2:
        a += 1
    elif 3 <= n <= 4:
        b += 1
    elif 5 <= n <= 6:
        c += 1
    elif 7 <= n <= 8:
        d += 1
    elif 9 <= n <= 10:
        e += 1
    total += 1
print(f"1 - 2: {"#"*a} {(a/total)*100:.2f}%")
print(f"3 - 4: {"#"*b} {(b/total)*100:.2f}%")
print(f"5 - 6: {"#"*c} {(c/total)*100:.2f}%")
print(f"7 - 8: {"#"*d} {(d/total)*100:.2f}%")
print(f"9 - 10: {"#"*e} {(e/total)*100:.2f}%")

# 7. Write a program to check if a string is palindrome or not without using any inbuilt function except len(). 
n = input().lower()
rev = ""
for ch in n:
    rev= ch + rev
if rev == n:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")

# 11. Take a paragraph as input and find the count of digits, alphabets, and special characters present in the paragraph. For alphabets, also check how many of them are upper case and how many are lower case alphabets. Use inbuilt string functions to check. 
n = input()
alp = 0
upper = 0
lower = 0
dig = 0
spe = 0
for ch in n:
    if ch.isalpha():
        alp += 1
        if ch == ch.upper():
            upper += 1
        else:
            lower += 1
    elif ch.isdigit():
        dig += 1
    else:
        spe += 1
print("No. of alphabets:",alp)
print("No. of upper case alphabets:",upper)
print("No. of lower case alphabets:",lower)
print("No. of digits:",dig)
print("No. of special charecters:",spe)

# 12
n = input()
new = ""
for i in n:
    if i in new:
        continue
    else:
        new += i
print(new)

# 9. Sort the elements of the list in descending order without using any inbuilt function. 
n = list(map(int,input().split()))
s = len(n)
for i in range(s):
    for j in range(s-1):
        if n[j]>n[j+1]:
            n[j],n[j+1] = n[j+1],n[j]
print(n)'''

