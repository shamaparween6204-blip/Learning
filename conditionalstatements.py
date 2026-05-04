#if staement

age=21
if(age>=18):
    print("Eligible to vote")

#elif

light="yellow"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("wait")

#else
light="black" 
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("wait")
else:
    print("Light is broken")


#nesting
age=105
if(age>=18):
    if(age>=80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("cannot drive")