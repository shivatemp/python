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
#Difference between 'and' and 'or' keywords:

print("CHECK FOR AND")

print("###")

x = int(input("what is X? "))
y = int(input("what is Y? "))

print("")

if x == 1 and y == 2:
    print("---TRUE---")
    print("And checks for both the things to be true.")

else:
    print("---FALSE---")
    print("Unless both true, and tags input as falsy.")

print("")
print("")

print("CHECK FOR OR")

print("###")

a = int(input("what is A? "))
b = int(input("what is B? "))

print("")

if a == 1 or b == 2:
    print("---TRUE---")
    print("Or checks for one of the things to be true.")

else:
    print("---FALSE---")
    print("Even if one is true, or tags input as truthy.")
'''

'''
#Boolean kind of functions i created
def main():
    p = int(input("what is X? "))
    q = int(input("what is Y? "))
    if fand(p,q):
      print("---TRUE---")
      print("And checks for both the things to be true.")

    else:
      print("---FALSE---")
      print("Unless both true, and tags input as falsy.")


def fand(x, y):

    if x == 1 and y == 2:
        return True    
    else:
        return False

main()'''

#Automatic Program to understand 'and' and 'or' keywords.
print("")
print("###")
print("Automatic Program to understand 'and' and 'or' keywords.")
print("")
print("###")
print("CHECK FOR 'AND'")
print("Here 'and' expects X = 1, Y = 2.")

def fand(x, y):
    
    if x == 1 and y == 2:
      print("_________")
      print("---TRUE---")
      print(f"Received Value = Expected Value; ({x},{y}) = (1,2)")
      print("'and' checks for both the things to be true.")
      print("_________")
      print("")
    else:
      print("_________")
      print("---FALSE---")
      print(f"Received Value != Expected Value; ({x},{y}) != (1,2)")
      print("Unless both true, 'and' tags input as falsy.")
      print("_________")
      print("")

print("")
print("TEST:-1 -- X = 1, Y = 2")
fand(1,2)

print("")
print("TEST:-2 -- X = 1, Y = 3")
fand(1,3)

print("")
print("TEST:-3 -- X = 3, Y = 2")
fand(3,2)

print("")
print("Therefore, The 'and' keyword always expects the exact values, for the all the required parameters.")
#######################################################################################################################
print("")
print("###")
print("CHECK FOR 'OR'")
print("Here 'or' expects A = 1 \"OR\" B = 2.")

def fuor(a, b):
    
    if a == 1 or b == 2:
      print("_________")
      print("---TRUE---")
      print(f"Received Value = Expected Value; ({a},{b}) = (1,2)")
      print("'or' checks for one of the things to be true.")
      print("_________")
      print("")
    else:
      print("_________")
      print("---FALSE---")
      print(f"Received Value != Expected Value; ({a},{b}) != (1,2)")
      print("Even if one is true, 'or' tags input as truthy.")
      print("_________")
      print("")

print("")
print("TEST:-1 -- A = 1, B = 2")
fuor(1,2)

print("")
print("TEST:-2 -- A = 1, B = 3")
fuor(1,3)

print("")
print("TEST:-3 -- A = 3, B = 2")
fuor(3,2)

print("")
print("TEST:-4 -- A = 3, B = 3")
fuor(3,3)

print("")
print("Therefore, The 'or' keyword just expects the any one value to be exact, for the all the required parameters.")
