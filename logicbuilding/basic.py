"""
#1
num=int(input("Enter a number: "))
if num%2==0:
    print(num," is even")
else:
    print(num," is odd")

#2

num=int(input("Enter a number: "))
if(num>0):
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")
"""
#3
"""
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a>=b and a>=c:
    print(f"{a} is greatest") 
elif b>=a and b>=c:
    print(f"{b} is greatest") 
else:
    print(f"{c} is greatest") 
#4

year=int(input("Enter the year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#5
for i in range(1,11):
    if(i%2==0):
        print(i)
"""
"""
#6
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#7
n=int(input("Enter a number: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
"""
"""
#8
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%2!=0):
        print(i)
"""
"""
#9
n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):  
    if i%2==0:
        count=count+1
print(count)
"""

#10
n=int(input("Enter a number: "))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
       