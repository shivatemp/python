# Playback Speed
# Prompts the user for input and prints it with each space replaced by '...'.
# Simulates slowing down speech by adding pauses between words.
#----------------------------------------------------------------------------------------

#The return value from input function is assigned to and stored in fetchUserInput variable.
fetchUserInput = input("Please input here. ")

#The main operation of splitting the string contained in fetchUserInput happens here, using split method.
#The 'list' produced as the the result of the operation are then stored in the variable list_store.
list_store = fetchUserInput.split(sep = " ", maxsplit = -1)

#At last, we print all the strings sequentially, and change the value of sep parameter to "...".
#The unpacking operator, '*' does Positional argument unpacking
#The '*' asterisk symbol is used to print all the values contained in any list, tuple or dictionary.
#When you use * in front of an iterable (like a list, tuple, or set), it unpacks its elements and passes them as individual positional arguments to the function.
print(*list_store, sep='...')
