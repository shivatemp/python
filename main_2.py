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
