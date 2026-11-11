# 1.   Read a list of integers and a value V. Convert the list into a tuple and print the tuple, its length, the number of times V occurs in it, and the index of the first occurrence of V.

numbers = map(int,input().split())
numbers = tuple(numbers)
a = int(input())
count_a = 0
first_index = 0
for number in numbers:
    if number == a:
        count_a += 1
for j in range (len(numbers)):
    if numbers[j] == a:
        first_index = j
        break
print(f"Tuple: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of {a}: {count_a}")
print(f"First index of {a}: {first_index}")

# 2.   Write a function count_vowels(s) that returns the number of vowels in the string s. Read a string, call the function and print the result.

def count_vowels(sentence):
    if not sentence:
        return 0
    count = 0
    for ch in sentence:
        if ch in "aeiou":
            count += 1
        else:
            continue
    return count
sentence = input().lower()
print(f"Vowels: {count_vowels(sentence)}")

# 3.   Each section at JKLU is electing a class representative. Every student writes one candidate's name, and all the votes are entered on a single line. Store the vote count of each candidate in a dictionary and print the results in the order the candidates first appear. The candidate with the most votes wins; if there is a tie, the candidate who appears first in the list wins.

names = input().split()
dic = {}
for name in names:
    count = names.count(name)
    dic[name] = count
winner = None
highest_value = 0
for key, value in dic.items():
    if highest_value < value:
        highest_value = value
        winner = key
print(dic)
print(F"Winner: {winner}")

# 4.   Read a word and build a dictionary that stores how many times each letter occurs in it. Print the dictionary.

n = input().lower()
dic = {}
for ch in n:
    count = n.count(ch)
    dic[ch] = count
print(dic)

# 5.   Write a function simple_interest(p, r, t=1) that returns the simple interest p * r * t / 100. Read p and r, then print the interest for the default time and for t = 3.

def simple_interest(p,r,t):
    return (p*r*t)/100
p = float(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter default years: "))
print(f"For {t} Year(s): {simple_interest(p,r,t)}")
t = int(input("Enter no. of years you want to find interest: "))
print(f"For {t} Year(s): {simple_interest(p,r,t)}")

# 7.   Read a tuple of integers and create a new tuple containing only its even numbers. Print the new tuple.

numbers = tuple(map(int,input().split()))
tupp = ()
for number in numbers:
    if number % 2 == 0:
        tupp += (number,)
print(tupp)

# 10.   Write a function stats(nums) that returns a tuple containing the smallest number, the largest number and the average of the list nums. Read a list of integers, call the function and print the returned tuple.

def stats(numbers):
    if not numbers:
        return None
    total = 0
    tup = ()
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        total += number
        if largest < number:
            largest = number
        if smallest > number:
            smallest = number
    average = total / len(numbers)
    tup += (smallest,largest,average,)
    return tup
numbers = list(map(int,input().split()))
print(stats(numbers))

