'''
# 1. Display the following addition table:            Addition Table         
#      1   2   3   4   5   6   7   8   9   
#    -------------------------------------- 
# 1 |   2   3   4   5   6   7   8   9  10 
# 2 |   3   4   5   6   7   8   9  10  11
# 3 |   4   5   6   7   8   9  10  11  12
# 4 |   5   6   7   8   9  10  11  12  13
# 5 |   6   7   8   9  10  11  12  13  14 
# 6 |   7   8   9  10  11  12  13  14  15 
# 7 |   8   9  10  11  12  13  14  15  16
# 8 |   9  10  11  12  13  14  15  16  17
# 9 |  10  11  12  13  14  15  16  17  18

n = int(input())
for i in range (1,10):
    for j in range(1,10):
        print(f"{(i+j):>3}",end=" ")
    print()
 
# 2. Parking Slot Allotment. A parking area has slots numbered from 1 to 1000. Every slot whose number is divisible by N is reserved. However, a reserved slot whose number is also divisible by 4 is kept for electric vehicle charging and is not given to staff. Display the slot numbers given to the staff. Use the continue statement with a while loop. Input: A single positive integer N. Output: The slot numbers given to the staff, separated by a single space. 
# Constraints: 1 ≤ N ≤ 1000.
# Sample Input    Sample Output 
# 250            250 750
# 333            333 666 999 
# For N = 250 the reserved slots are 250, 500, 750 and 1000, out of which 500 and 1000 are kept for charging.

n = int(input())
i = 1
while i <= 1000:
    if i % n != 0 or i % 4 == 0:
        i += 1
        continue
    else:
        print(i,end = " ")
        i += 1
        
# 3
# print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# (till uoto n)

n = int(input()) 
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end = " ")
    print()  

# print 
# **** 
# *** 
# ** 
# * 
# (till n lines)

n = int(input())
for i in range (n,0,-1):
    for j in range (1,i+1):
        print("*",end = " ")
    print()
    
# print
#     *
#    **
#   ***  
#  **** 
# (till n lines)

n = int(input())
for i in range (1,n+1):
    print(" "*(n-i),end = "")
    for j in range(1,i+1):
        print("*",end = "")
    print()

# 5
# print the secong largest among the given inputs
  
n = int(input())
lar1 = 0
lar2 = 0
for i in range (1,n+1):
    a = int(input())
    if a > lar1 and a > lar2:
        lar2 = lar1
        lar1 = a
    if a < lar1 and a > lar2:
        lar2 = a
print(lar1,lar2)

#6. Display all the Armstrong numbers between 1 and N, where the value of N is taken as input from the user.
n = int(input())
for i in range (1,n+1):   
    s = i
    a = i
    total = 0
    count = 0
    while i != 0:
        d = i % 10
        count += 1
        i = i // 10
    while s != 0:
        b = s % 10
        total += b**count
        s = s // 10
    if total == a:
        print(a,end = " ")

# 7

n = int(input())
for i in range (1,n+1):
    print(f"{i:>4}  {i**2:>4}  {i**3:>4}  {i**0.5:>4.2f}")

# 8
# print equilateral number triangle
   
n = int(input())
num = 1
for i in range (1,n+1):
    print(" "*(n-i),end = "")
    for j in range (1,i+1):
        print(num , end = " ")
    num += 1
    print()
    
# 9
#print number triangle  

n = int(input())
num = 1
for i in range (1,n+1):
    for j in range (1,i+1):
        print(num , end = " ")
        num += 1
    print()    
    
    
# 10
# print Diamond pattern
  
n = int(input())
for i in range (1,n):
    print(" "*(n-i),end = "")
    for j in range (1,i):
        print("*",end = "")
    for k in range (1,i-1):
        print("*",end = "")
    print()
for s in range (n,1,-1):
    print(" "*(n-s),end = "")
    for l in range (1,s):
        print("*",end = "")
    for m in range (1,s-1):
        print("*",end = "")
    print()'''

