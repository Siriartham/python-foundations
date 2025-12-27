#strings in python are sequence of characters together
''' there are many string methods and functions 
     such as : find,replace,upper,lower,count
       repetition, concatenation...'''
message = input("Enter a message: ") # reading the message from the user
name = input("Enter the name: ") # reading the name from the user
new_message = "{}\n {} How do you do.".format(message,name.lower()) # using the formatting function we can make a particular format for printing. 
print(new_message)

new_name = input("Enter a new name: ")
new_one_message = f"{message}\n {new_name.upper()} Hey! How do you do." # This a another type of formatting function
print(new_one_message)
print(new_name.find('K')) # Find is used to check where the provided character is present in the string it will return the index of that character.
print(new_name.count('u')) # Count is used to check how many times the given character is repeated in the string.
