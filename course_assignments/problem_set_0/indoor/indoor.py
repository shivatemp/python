# Indoor Voice
# Prompts the user for input and prints the input in all lowercase.
# Punctuation and spaces remain unchanged.
#----------------------------------------------------------------------------------------

#The return value from input function is assigned to and stored in fetchUserInput variable.
fetchUserInput = input("Please input here. ")

#The 'lower()' method of string datatype is used to convert all upper case characters into lowercase.
#The value given by 'fetchUserInput.lower()' is assigned to 'processUserInput'.
processUserInput = fetchUserInput.lower()

#The print function prints the value contained in 'processUserInput'.
print(processUserInput)

'''
#Overcomplex Hard Version - Single Responsiblity Principle
def getUserInput():
    processUserInput(input("Please input here. "))

def processUserInput(userInput):
    printUserInput(userInput.lower())

def printUserInput(userInput_Lower_Case):
    print(userInput_Lower_Case)

getUserInput()

#Or have a one liner
print(input("Please input here. ").lower())
'''