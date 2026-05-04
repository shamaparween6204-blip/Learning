"""
#1
str=input("Enter your name: ")
l=len(str)
print("Length of your name is: ",l)

#2
str=input("Enter your name: ")
ch=str.count('a')
print(ch)

#3
num=int(input("Enter first number"))
if(num%2==0):
    print("Even number")
else:
    print("Odd Number")

#4
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")

#5
num=int(input("Enter first number: "))
if(num%7==0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")

#6
movies=[]
m1=input("1st movie: ")
m2=input("2nd movie: ")
m3=input("3rd movie: ")
movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)


#7.
list=[]
l=int(input("1st: "))
list.append(l)
l=int(input("2nd: "))
list.append(l)
l=int(input("3rd: "))
list.append(l)
l=int(input("4th: "))
list.append(l)
l1=list.copy()
l2=l1.reverse()
if(list==l1):
    print("Palindrome")
else:
    print("Not palindrome")
"""
#8
tuple=("C","D","A","A","B","A")
print(tuple.count("A"))

