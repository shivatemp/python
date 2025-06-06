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
