'''
light_c = 300000000
mass = float(input("What should be the mass(in kilograms)? "))
energy_E = pow(light_c, 2) * mass
print(f"The total energy produced is {energy_E:,.2f} Joules.")
'''
light_c = 300000000
mass = int(input("What should be the mass(in kilograms)? "))
energy_E = mass * pow(light_c, 2)
print(f"The total energy produced is {energy_E} Joules.")
