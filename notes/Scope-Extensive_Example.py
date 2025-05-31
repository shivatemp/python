'''
# prints simply the global varriable to local scope.
#This means local variable can access the global variable.
emoji="😭"

def prints():
    print(f"yoo!! {emoji}.")

prints()
'''

'''
#Again, the same. Prints the global variable to local scope.
#But this time we also have a parameter for prints() function for printing different things. No Problem.
emoji="😭"

def main():
    prints("Me sad")

def prints(x):
    print(f"yoo!! {x} {emoji}.")

main()
'''

'''
#So if we look here, we will see that we just called prints() function again in the main().
#But this time we are able to see that there is no technical error but we would want a change.
#We would want the '😭' emoji to change as we say "Me Happy".
emoji="😭"

def main():
    prints("Me sad")
    prints("Me Happy!!")

def prints(x):
    print(f"yoo!! {x} {emoji}.")

main()
'''

'''
#so we tried doing this.
#We changed the global emoji successfully but it changes for "Me sad" too, which is wrong.
#But what did we even do?
#We are here overiding the global variable here inside the prints() function only, by using the same name as the global variable.
emoji="😭"

def main():
    prints("Me sad")
    prints("Me Happy!!")

def prints(x):
    emoji="🤣"
    print(f"yoo!! {x} {emoji}.")

main()
'''

'''
#We can check here that our global variable has not changed at all in a global context its still the same.
#The overide is happening only in the prints() function.
#See the last print statement.
emoji="😭"

def main():
    prints("Me sad")
    prints("Me Happy!!")

def prints(x):
    emoji="🤣"
    print(f"yoo!! {x} {emoji}.")

main()
print(f"But wait I am still crying, {emoji}")
'''

'''
#Now, because the preevious stuff did not yeild results, we put the 'emoji="🤣"' in the main function.
#We put it just above 'prints("Me Happy!!")' because that's when we want to change the emoji.
#But we see the 'emoji="🤣"' greyed. This is because it's declared but not used anywhere inside the function.
#But even if we use it, it will not grey, but it will still be useless cause its scope will be local.
#It will not be shown in the print statement of the prints() function at all.
emoji="😭"

def main():
    prints("Me sad")
    emoji="🤣"
    prints("Me Happy!!")

def prints(x):
    print(f"yoo!! {x} {emoji}.")

main()
'''

'''
#To use this declared variable in the main() function, we will need to actually do this:
#But doing so will make the usage of prints() function totally useless.
emoji="😭"

def main():
    prints("Me sad")
    emoji="🤣"
    print(f"Me Happy!!, {emoji}")

def prints(x):
    print(f"yoo!! {x} {emoji}.")

main()
'''

'''
#So what should we do now?
#What we actually need to do?
#Somehow we need to change the global variable just before running the 'prints("Me Happy!!")' line in the 'main()' function.
#For that somehow we need to change the global variable when it comes to main, thats how we can do it.
#But we cahnge the global variable only after executing 'prints("Me sad")' otherwise, we end up at same place, only 1 emoji.
#So how to do it in python?

#For changing the global variable inside a function, we use the keyword 'global'.

#The global keyword in Python is used to modify a global variable from within a function.
#Without it, if you try to assign a value to a variable with the same name as a global variable inside a function,
#Python will create a new local variable instead.
#Using global allows you to explicitly indicate that you are referring to the global variable. 

#So here, we are now able to modify the global variable 'emoji' and that too after the statement, 'prints("Me sad")'
emoji="😭"

def main():
    global emoji
    prints("Me sad")
    emoji="🤣"
    prints("Me Happy!!")

def prints(x):
    print(f"yoo!! {x} {emoji}.")

main()

'''

'''
#But here we also need to keep in mind, that function main is now giving a side effect.

#A side effect in Python occurs when a function or expression modifies something outside its local scope.
#This results in a change that persists beyond the function's execution.
#These effects can include modifying global variables, changing mutable objects passed as arguments.
#It can slso be performing I/O operations like printing to the console or writing to a file.

#Therefore we can see here below, that after the main() function is called, the value of global emoji variable changes.
#The change is permanant.

emoji="😭"

def main():
    global emoji
    prints("Me sad")
    emoji="🤣"
    prints("Me Happy!!")

def prints(x):
    print(f"yoo!! {x} {emoji}.")

print(f"Ok.... I am still crying, {emoji}")
print()
main()
print()
print(f"But wait, Yooo!!...I am permanantly happy now, {emoji}")
'''