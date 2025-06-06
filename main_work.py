'''
def hello():
  print("Hello, ", end="")


x = input("What's your name? ")
hello()
print(x)

'''
'''
def hello(to):
  print("Hello, ", to)


name = input("What's your name? ")
hello(name)

'''
'''
def hello(to="World"):
  print("Hello,", to)


hello()

name = input("Yo! What's your name? ")

hello(name)
'''
'''
def main():
  name = input("What's your name? ")
  hello(name)


def hello(to="World"):
  print("Hello,", to)


main()
'''
'''
def main(name):
  print("Hello,", name)


main(input("What's your name? "))

#So basically this is my experiment and here the function main has a parameter 'name' and we are passing the input function to the main function's parameter 'name', as an argument.
#So basically, the input function is returning a string the value and that value is passed to the main function's parameter 'name'. It is the setting of nested functions.

'''
'''
def main():
  x = int(input("What should X be? "))
  print("X should be:", square(x))


def square(n):
  return n * n

#Only n * n: This will not work as expected because the function square is not returning anything. It is just multiplying the value of n with itself and then discarding the result.

main()
'''
'''
def inpt():
  n = int(input("What should X be? "))
  return n


def main():
  y = inpt()**2
  print("X squared should be:", y)


main()
'''
'''
def side_effect():
  y = input("What is your first name? ")
  z = input("What is your second name? ")
  print("Hello,", operation(y, z))


def operation(m, n):
  x = m + " " + n
  return x


side_effect()
'''

'''
x = int(input("x? "))
y = int(input("y? "))

if x<y or x>y:
    print("x and y are not equal.")
  
else:
    print("x and y are equal.")

'''
'''
x = int(input("x? "))
y = int(input("y? "))

#it can also be vice a versa
if x != y:
    print("x and y are not equal.")

else:
    print("x and y are equal.")
'''

'''
x = int(input("what is the year? "))

if x%100 == 0:
    if x%400 == 0:
        print("its leap")
    else:
        print("its not leap")
elif x%100 != 0:
    if x%4 == 0:
        print("its leap")
    else:
        print("its not leap")
'''

'''
x = int(input("what is the year? "))

if x%100 == 0:
    if x%400 == 0:
        print("its leap")
    else:
        print("its not leap")
else:
    if x%4 == 0:
        print("its leap")
    else:
        print("its not leap")
'''

'''
#Better Version
x = int(input("what is the year? "))

if x%4 == 0:
    if x%100 != 0:
        print("its leap")
    elif x%400 == 0:
        print("its leap")
    else:
        print("its not leap")
else:
    print("its not leap")
'''


'''
#Boolean check - condensed statement
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print ("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()
'''

'''
#Boolean check - ultra condensed statement
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print ("Odd")

def is_even(n):
# n%2 is returns a int  but n%2 == 0 will always return a boolean value, i.e., true or false.
    return n % 2 == 0
    #return (n % 2 == 0)    #one more way-just a bit more clear

main()
'''

'''
x = input("a or b or c or d only---- ")

if x == "a":
    print(1)

elif x == "b":
    print(1)

elif x == "c":
    print(1)

elif x == "d":
    print(2)

else:
    print(0)
'''

'''
#Tightened Version
x = input("a or b or c or d only---- ")

if x == "a" or x == "b" or x == "c":
    print(1)

elif x == "d":
    print(2)

else:
    print(0)
'''

'''
#yup this is how 'and' function can give the value
x1,x2,x3 = input("a or b or c or d only---- ").split(" ", maxsplit=-1)

if x1 == "a" and x2 == "b" and x3 == "c":
    print(1)
else:
    print(0)
'''

'''
#Same thing using match function - we regressed

x = input("a or b or c or d only---- ")

match x:
    case "a":
        print(1)
    case "b":
        print(1)
    case "c":
        print(1)
    case "d":
        print(2)
    case _:
        print(0)
'''

'''
#ok  just use'|' this instead of 'or' which cant be used here.

x = input("a or b or c or d only---- ")

match x:
    case "a" | "b" | "c":
        print(1)
    case "d":
        print(2)
    case _:
        print(0)
'''

'''
print("So you get 2 alphabet and 2 numbers; a,b; 1,2.")
print("")

def main():
        x = input("enter char---")
        y = input("enter num.---")

        if x == "a":
            if y == "1":
                print("Matched a1")
            elif y == "2":
                print("matched a2")
            else:
                print("nothing matches yolo")
        elif x == "b":
            if y == "1":
                print("b1")
            elif y == "2":
                print("b2")
            else:
                print("nothing matches yolo")
        else:
            print("You dumb or something bro??")

main()
'''
'''
#Using Match control-flow keyword
def main():
    x = input("enter char: ")
    y = input("enter num: ")

    match x:
        case "a":
            match y:
                case "1":
                    print("Matched a1")
                case "2":
                    print("Matched a2")
                case _:
                    print("nothing matches yolo")
        case "b":
            match y:
                case "1":
                    print("b1")
                case "2":
                    print("b2")
                case _:
                    print("nothing matches yolo")
        case _:
            print("You dumb or something bro??")
'''

'''
#Tuple Matching
def main():
    x = input("char? ")
    y = input("num? ")

    match (x, y):
        case ("a", "1"):
            print("a1")
        case ("a", "2"):
            print("a2")
        case ("b", "1"):
            print("b1")
        case ("b", "2"):
            print("b2")
        case _:
            print("nah bro, nothing matches yolo")

main()
'''

'''
Both if and match are Python keywords, not functions — they are core control-flow tools baked into the language syntax.
They parsed directly by Python, and cannot be used like objects or functions.
'''

'''
print("So you get 2 alphabet and 2 numbers; a,b; 1,2.")
print("")

def main():

        x = input("enter char---")
        if not (x == "a" or x == "b"):
            print("Yo you tryna be smart with chars...")
            return None

        y = input("enter num.---")
        if not (y == "1" or y == "2"):
            print("Yo you tryna be smart with numbers...")
            return None

        if x == "a" and y == "1":
                print("Matched a1")

        if x == "a" and y == "2":
                print("matched a2")

        if x == "b" and y == "1":
                print("Matched b1")

        if x == "b" and y == "2":
                print("matched b2")

main()
'''

'''
#This also works but then, the code does not stoop even after detecting the falut... return only works inside a function.

print("So you get 2 alphabet and 2 numbers; a,b; 1,2.")
print("")

x = input("enter char---")
if not (x == "a" or x == "b"):
    print("Yo you tryna be smart with chars...")
            

y = input("enter num.---")
if not (y == "1" or y == "2"):
    print("Yo you tryna be smart with numbers...")

if x == "a" and y == "1":
    print("Matched a1")

if x == "a" and y == "2":
    print("matched a2")

if x == "b" and y == "1":
    print("Matched b1")

if x == "b" and y == "2":
    print("matched b2")
'''

