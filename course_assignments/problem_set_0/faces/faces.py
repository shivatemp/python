# Making Faces
# Defines a convert function that replaces :) with 🙂 and :( with 🙁 in user input.
# The main function prompts the user, calls 'convert()', and prints the result.
#----------------------------------------------------------------------------------------

#convert() function processes the argument from the user input in the main() function.
#It gets that through the parameter fetchUserInput.
#-------------#
#The replace method of string data type runs 2 times on the value stored in fetchUserInput variable, to replace both the emoticons to emojis
#The value is then stored into the variable processUserInput and then at the end returned.
def convert(fetchUserInput):
    processUserInput = fetchUserInput.replace(":)", "🙂", count = -1).replace(":(", "🙁", count = -1)
    return processUserInput

##The return value from input function is assigned to and stored in getUserInput variable.
#The convert() function is called with the keyword argument getUserInput variable.
#The value returned by the convert() function is assigned to and stored into the print_result variable.
#The print function prints the value stored in the print_result variable.
def main():
    getUserInput = input("Please type here. ")
    print_result = convert(getUserInput)
    print(print_result)

#The main() function is called.
main()
