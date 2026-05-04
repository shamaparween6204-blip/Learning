marks1=97.2
marks2=98.5
marks3=88.2
marks4=78.5
marks5=67.3


marks=[97.2,88.3,90.3,65.9,99]
print(marks)
print(type(marks))
print(marks[3])

student=["Ram",23,98,"Mumbai"]
print(student)
print(student[0])
student[0]="Aryan"
print(student)

#list slicing

marks=[97.2,88.3,90.3,65.9,99]
print(marks[1:4])

#list methods

#append
list=[1,2,3]
list.append(4)
print(list)

#sorting(ascending)
list=[2,1,3]
list.sort()
print(list)

list=['a','d','b','c']
list.sort()
print(list)

#sorting(descending)
list=[1,2,3]
list.sort(reverse=True)
print(list)

list=['a','d','b','c']
list.sort(reverse=True)
print(list)

#reverse
list=[1,2,3,4]
list.reverse()
print(list)

#insert list.insert(index,element)
list=['a','d','b','c']
list.insert(4,'e')
print(list)

#remove list.remove(element)
list=['a','d','b','c','a']
list.remove('a')
print(list)

#pop list.pop(index)
list=['a','d','b','c']
list.pop(2)
print(list)