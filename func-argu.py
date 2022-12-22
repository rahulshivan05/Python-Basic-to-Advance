# def average(a,b):
#     print("The Average is: ",(a+b)/2)

# def name(fname, mname="Kumar", lname = "Gupta"):
#     print("Hello,",fname, mname, lname)


# when you use (*) in any function then make as a tuple

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:", sum/len(numbers))
    return sum/len(numbers)


a = 5
b = 6
c = average(a, b, 55, 45) # you pass many argument in it
print(c)


# (**) means dictionary

def _name(**name):
    # print(type(name))
    print("Hello", name["fname"], name["mname"], name['lname'])

# _name(mname = "Buchanan", lname = "Barnes", fname = "James")

# name(fname="Rahul")

