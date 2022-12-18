# String's are Imutable in Python
# matlab aap usko change nahi kar sakhta hai

# aap usko in-place change nahi kar sakta

a = "!!!!! !!!!!!! Rahul !!!!! !!!!! Rahul !!!!"
# print(len(a))
# print(a)

# yeh existing string ko change nahi karega
# yaha par hame ek nai string militi hai
# print(a.upper())
# print(a.lower())

# print(a.strip("!"))

# print(a.replace("Rahul", "John"))

# print(a.split(" "))

heading = "welcome tO Github"

# captilize function captilize first character and other in lower case
# print(heading.capitalize())
# print(heading.center(50))

# ye count karta hai kisi variable ye thing kitna baar aa raha hai. It is Case sensitive
# print(a.count("Rahul"))

print(a.endswith("!")) # return True or False

# Python me variable ko over-ride kar sakta hai
str1 = "Welcome to the Console !!!!!"
print(str1.endswith("to", 4,10))

str1 = "He's name is Rohit. He is an Honest man."
print(str1.find("iss")) # give me the first occurans index no.
print(str1.index("iss"))