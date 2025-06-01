# Tip Calculator
# Completes a tip calculator by implementing two functions to convert dollar and percent strings to float values.
# Calculates and prints the tip amount based on user input.
#----------------------------------------------------------------------------------------

#The main() function calls the dollars_to_float() and percent_to_float() functions.
#Both the functions get their value from the input function as the argument for the parameters, 'd' and 'p' respectively.
#Their return value gets stored into the variables named 'dollars' and 'percent' respectively.
#After this, the product of values stored in dollars and percent is stored in the variable tip, and then later printed.
#The print function uses f-string ':.2f' to print float values to 2 decimal point only. 
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#The dollars_to_float(d) function processes the string input came from the user from the input function.
#First the function is stripped off of the '$' symbol using the strip method of string data type and stored in variable strip_d.
#Next, the value of variable 'strip_d' is converted to float using the float function and stored in the variable dollars, then returned.
def dollars_to_float(d):
    strip_d = d.strip("$")
    dollars = float(strip_d)
    return dollars

#percent_to_float(p) function does the similar job as dollars_to_float(d) function, just focuses on stripping away the '%' symbol.
def percent_to_float(p):
    strip_p = p.strip("%")
    percent = float(strip_p)/100
    return percent

#main() function is called
main()

'''
#Simple way to write
def dollars_to_float(d):
    dollars = float(d.strip("$"))
    return dollars


def percent_to_float(p):
    percent = float(p.strip("%"))/100
    return percent
'''

'''
#This is the alternative which uses lstrip and rstrip instead of strip method.
#Can be used if we want to be more specific.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    strip_d = d.lstrip("$")
    dollars = float(strip_d)
    return dollars


def percent_to_float(p):
    strip_p = p.rstrip("%")
    percent = float(strip_p)/100
    return percent


main()
'''