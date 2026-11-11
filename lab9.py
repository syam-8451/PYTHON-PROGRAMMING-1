# 1.   Read a line of space-separated integers and store the even and odd numbers in two separate lists. Print both lists.

n = list(input().split())
even = []
odd = []
for i in n:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
print("Odd:",odd)

# 2.   Read a sentence and build a list of all the words that have more than 3 letters, in the order they appear. Print the list.
n = input().split()
more = []
for i in n:
    if len(i) > 3:
        more.append(i)
print(more)


# 3.
n = input().split()
wickets = 0
total_runs = 0
boundaries = 0
count = 0
runs = 0
count1 = 0
runs_in_each_over = []
for i in n:
    count += 1
    if i.upper() == "W":
        wickets += 1
    else:
        if int(i) == 4 or int(i) == 6:
            boundaries += 1
        total_runs += int(i)
        if count <= 6:
            runs += int(i)
        else:
            count = 1
            runs = int(i)
    runs_in_each_over.append(runs)
print("Total Runs:",total_runs)
print("Wickerts:",wickets)
print("Boundaries:",boundaries) 
print(runs_in_each_over)  


# 4.   Read a list of integers and print the largest and the smallest number in it, without using max() or min().

n = input().split()
maximum = 0
minimum = int(n[0])
for i in n:
    i = int(i)
    if maximum < i:
        maximum = i
    elif minimum > i:
        minimum = i
print(maximum)
print(minimum)

# 5.   Read a sentence and print its longest word. If two words have the same length, print the one that comes first.
n = input().split()
longest = n[0]
for i in n:
    if len(longest) < len(i):
        longest = i
print(longest)

