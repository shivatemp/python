'''
#Nested functions
#print("Hello,", input("whats your name? "))
#print("Hello, Shiva")

#print("Hello, " + x)
#print("Hello,", x, sep=" chicken ", end=".\n\n")
#print("yo")

#escape character
#print("Hello, \"friend\"")

#one more way
#print("yo, 'friend'")
x = input("What's your name? ")

#Remove whitespace
x = x.strip()

#Capitalize first lertter
#x=x.capitalize()

#capitalize all the letters
x=x.title()

print(f"Hello, {x}")
'''
'''
nesting various functions and ITS NESTING + CHAINING: Chaining the functions together
#x=input("What is your name? ").title().strip()
print("Hello, ", input("What's your name? ").title().strip())

'''
#split user name
#x = input("What's your name?" ).split()
#print(x)

#x = input("What's your name? ")
#first, second=x.split(" ")
#print(f"Hello {first}")

'''x=input("X? ")
y=input("y? ")
z=int(x)+int(y)
print(z)
'''

'''
#nesting functions
x=int(input("X? "))
y=int(input("y? "))
z=x+y
print(z)
'''

#bad code style
#print(int(input("X? "))+int(input("y? ")))

'''
x = input("What is X? ")
y = input("What is Y? ")

x = float(x)
y = float(y)

z = x + y

#round function
#z = round(z, 1)

#numeric formatting and locale[it is a python library which controls the formats] style formatting standard numeric formatting
print(f"The answer is {round(z,2):,}.")
print(f"The better answer is {z:,.2f}.")
'''
'''
def greet():
    print("Hello, World")

greet()
'''
'''
def greet(name):
    print("Hello," + str(name))

greet(5)
'''
'''
#long version - more flexible
def greet(name="world"):
    print(f"Hello, {name}")
# 'name' is a parameter of the 'greet' function.
# It works like a local variable that stores the value passed to the function (or the default, if nothing is passed).
# This lets us reuse 'name' inside the function — in this case, to print a greeting.

greet()

user_name=input("What is your name? ")

greet(user_name)
'''
'''
#small version
def greet():
    name=input("What's your name? ")
    print(f"Hello, {name}")

greet()
#but here the problem is that it has no default value as a parameter and cant give a flexible perssonality like the previous example.
'''

'''
def main():
    name = input("What's your name? ")
    hello()

def hello():
    print(f"Hello, {name}.")
main()

#this code will not work because the name variable is local to main function
'''

'''
def main():
    name = input("What's your name? ")
    hello(name)

def hello(user_name = "World"):
    print(f"Hello, {user_name}.")
#Here if I just tried to do, name = user_name, then again all variables would be localized.
#But we need to give the return value of main() function as the argument to hello() function.
#To do this we are actually making a parameter for hello() function and this allows us to now use the return value of main() ---
# --- to use as an argument.

# 'user_name' is a parameter of the 'greet' function.
# It works like a local variable that stores the value passed to the function (or the default, if nothing is passed).
# This lets us reuse 'user_name' inside the function as a variable — in this case, to print a greeting.
main()
'''

'''
def pat():
    return 3

x=pat()

print(x)
'''

'''
def main():
    x=int(input("Whats X? "))
    print("X squared is:", square(x))

def square(n):
#    return n * n
#    return n ** 2 # basically in this if we put 2 ** then it means number on left - raise to the power of - anything on the right
    return pow(n,2)

main()

'''

'''
y=7.64
x=3**y
v=round(x, 4)
print(f"{round(x, 4):,}")

##############################

def greet():
    return 3+4

print(greet())
'''

'''
def area(a, b):
    print(str(a*b) + " is the area.")

def main():
    area(10, 20)

main()
'''

'''
def area(a, b):
    print(str(a*b) + " is the area.")

def main():
    area(10, 20)
    area(20, 20)

main()
'''

'''
def area(a, b):
    m = a * b
    print(str(m) + " is the individual area.")
    return m

def main():
    x = area(10, 20)
    y = area(30, 40)
    z = x + y
    print(f"Total area is: {z}")

main()
'''

'''
def area():
    # tells user to input
    print("Yo give em numbers")
    # takes input
    a = int(input("whats breadth? "))
    b = int(input("whats length? "))
    # does calculation
    m = a * b
    # for neatness
    print("")
    print(f"{m} is the individual area.")
    # for neatness
    print("")
    # returns the value of the operation conducted
    return m

def main():
    x = area()
    y = area()
    z = x + y
    # prints the individual area
    print(f"{x} is the individual area.")
    print(f"{y} is the individual area.")
    # prints the total area
    print(f"Total area is: {z}")
# calls the main() function.
main()
'''

'''
# takes input
def tellem():
    # tells user to input
    print("Yo give em numbers")
    # takes input
    a = int(input("whats breadth? "))
    b = int(input("whats length? "))
    return a, b
# calculates
def area():
    a,b = tellem()
    # does calculation
    m = a * b
    # for neatness
    print("")
    print(f"{m} is the individual area.")
    # for neatness
    print("")
    # returns the value of the operation conducted
    return m
# does final calc and gives result
def main():
    x = area()
    y = area()
    z = x + y
    # prints the individual area
    print(f"{x} is the individual area.")
    print(f"{y} is the individual area.")
    # prints the total area
    print(f"Total area is: {z}")
# calls the main() function.
main()
'''

'''
emoticon = "v.v"

def main():
    say("Is anyone there?")
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)

main()
'''

'''
x="yo"

def main():
    print(x)

main()
'''

'''
def outer():
    x = 20  # enclosing scope
    def inner():
        print(x)
    inner()

outer()
'''

'''
var=3

def main():
    var = 2
    blah(var)

def blah(get):
    print(f"Yo {get}")

main()
'''

'''
y=7.64
x=3**y
v=round(x, 4)
print(f"{round(x, 4):,}")
'''

'''
def greet():
    return 3+4

print(greet())
'''

'''
def main():
    x=int(input("Whats X? "))
    print("X squared is:", square(x))

def square(n):
#    return n * n
#    return n ** 2 # basically in this if we put 2 ** then it means number on left - raise to the power of - anything on the right
    return pow(n,2)

main()
'''

'''
x=2

def main():
    global x
    print(x)
    x=x+3
    print(x)

main()

print(x)
'''

'''
x = int(input("What's X? "))
y = int(input("What's Y? "))

if x>y:
    print("x>y")

if x<y:
    print("x<y")

if x==y:
    print("x=y")

'''

'''
#Control Flow
x = int(input("What's X? "))
y = int(input("What's Y? "))

if x>y:
    print("x>y")

elif x<y:
    print("x<y")

elif x==y:
    print("x=y")
'''

'''

'''

'''
#Control Flow - even more
x = int(input("What's X? "))
y = int(input("What's Y? "))

if x>y:
    print("x>y")

elif x<y:
    print("x<y")

else:
    print("x=y")
'''

'''
grade = int(input("Grade? "))

if grade >= 90 and grade <= 100:
    print("A")

elif grade >=80 and grade < 90:
    print("B")

elif grade >=70 and grade < 80:
    print("C")

elif grade >=60 and grade < 70:
    print("D")

else:
    print("F")'''

'''#Nesting and chaining operations
grade = int(input("Grade? "))

if 90 <= grade <= 100:
    print("A")

elif 80 <= grade < 90:
    print("B")

elif 70 <= grade < 80:
    print("C")

elif 60 <= grade < 70:
    print("D")

else:
    print("F")'''

'''# More concise - Just asking more questions
grade = int(input("Grade? "))

if 90 <= grade:
    print("A")

elif 80 <= grade:
    print("B")

elif 70 <= grade:
    print("C")

elif 60 <= grade:
    print("D")

else:
    print("F")
'''

'''
# yup logic faileure cause now all conditions run
grade = int(input("Grade? "))

if 90 <= grade:
    print("A")

if 80 <= grade:
    print("B")

if 70 <= grade:
    print("C")

if 60 <= grade:
    print("D")

if 0<= grade:
    print("F")'''

'''
#Boolean check
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print ("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
'''

'''
#Just checking if 2 return values can be passed while in a if else conditional.
def main():
    x = int(input("What's X? "))
    if is_even(x) == "yup":
        print("Even")
    else:
        print ("Odd")

def is_even(n):
    if n % 2 == 0:
        return "yup"
    else:
        return "nope"

main()
'''

'''
#Yeah multiple inputs through if conditional work. Dope!!
def main():
    x = int(input("What's X? "))
    print(is_even(x))

def is_even(n):
    if n % 2 == 0:
        return "yup_even"
    else:
        return "nope_uneven"

main()
'''