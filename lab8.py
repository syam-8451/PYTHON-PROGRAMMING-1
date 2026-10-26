# 1.   Read a string and count how many characters in it are vowels, consonants, digits, spaces and other symbols.
n = input()
vowel = 0
consonent = 0
space = 0
others = 0
digit = 0
for ch in n.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowel += 1
        else:
            consonent += 1
    elif ch.isdigit():
        digit += 1
    elif ch == " ":
        space += 1
    else:
        others += 1
print(f"Vowels: {vowel}")
print(f"Cosanents: {consonent}")
print(f"Digits: {digit}")
print(f"Spaces: {space}")
print(f"Others: {others}")

# 2.   Read a string and rewrite it so that the characters at even positions (0, 2, 4, …) are in uppercase and those at odd positions are in lowercase. Characters that are not letters stay unchanged but still occupy a position.
n = input()
st = ""
for i in range(len(n)):
    if i % 2 == 0:
        st += n[i].upper()
    else:
        st += n[i].lower()  
print(st)  

# 03
n = input()
count = 0
upp = False
low = False
spe = False
dig = False
for i in n:
    if i.isalpha():
        if i.isupper():
            upp = True
        else:
            low = True
    elif i.isdigit():
        dig = True
    elif i not in "QWERTYUIOPLKJHGFDSAZXCVBNM 1234567890qwertyuioplkjhgfdsazxcvbnm":
        spe = True
count = upp + low + dig + spe
if len(n) < 8:
    print("Weak")
else:
    if count == 4:
        print("Strongest")
    elif count < 4:
        print("Moderate")

# 04
n = input().lower()
ch = input()
count = 0
c = 0
if ch not in n:
    print("-1")
for i in range (len(n)):
    if n[i] == ch:
        count += 1
        c += i 
        print(i,end = " ")      
print()
print("Count:",count)

# 05
n = input()
count1 = 0
count2 = 0
rev = ""
for i in n:
    if i != " ":
        count1 += 1
    else:
        print(count1,end = " ")
        count1 = 0
for j in range (len(n)-1,-1,-1):
    rev += n[j]
    if n[j] == " ":
        break
count2 = len(rev)
print(count2-1,end = " ")

# 06
n = input().upper()
count1 = 0
count2 = 0
for i in n:
    if i.isalpha():
        if n[0] == "R" and n[1] == "J":
            count1 += 1
    elif i.isdigit():
        count2 += 1
print(n)
if count1 == 4 and count2 == 6:
    print("True")
else:
    print("False") 

# 07
n = input()
count = 0
for i in range(len(n)):
    b = n[i]
    c = n[len(n)-1-i]
    if b != c:
        count += 0.5
print(f"Changes required: {count:.0f}")

# 8.   Read a string and remove all repeated characters, keeping only the first occurrence of each.
n = input()
new = ""
for i in n:
    if i in new:
        continue
    else:
        new += i
print(new)

# 9.   At the college hackathon, teams receive their problem statement as a coded message. To encode it, each letter of the original message is shifted forward by K positions in the alphabet (with K = 3, a becomes d and c becomes f). If the shift goes beyond z, counting continues again from a (with K = 3, y becomes b). Spaces are left as they are. Write the program that encodes a message so the organisers can prepare the clues.
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