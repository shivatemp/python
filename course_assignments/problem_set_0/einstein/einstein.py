#Einstein
#Prompts the user for mass in kilograms and calculates equivalent energy in Joules.
#Uses the formula E = mc² with c = 300000000 m/s.
#----------------------------------------------------------------------------------------

#Declaring the speed of light and storing it into a variable, 'light_c'.
light_c = 300000000

#The input function takes the user input, then the value goes to int function, which converts string input to integer.
#At last the value is stored in the mass variable.
mass = int(input("What should be the mass(in kilograms)? "))

#The value contained in the variables 'mass' and 'light' is multiplied,then, the product is stored in the variable 'energy_E'.
#The pow function is used on the value contained in the variable 'light_c', to properly calculate E = MC^2.
energy_E = mass * pow(light_c, 2)

#Finally the output is printed using the print function.
print(f"The total energy produced is {energy_E} Joules.")

'''
#Alternative:
#The float data type provides more flexibility.
light_c = 300000000
mass = float(input("What should be the mass(in kilograms)? "))
energy_E = pow(light_c, 2) * mass
print(f"The total energy produced is {energy_E:,.2f} Joules.")
'''