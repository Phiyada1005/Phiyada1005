counter = 0
def increment():
    global counter
    count += 1

# Calling the function
increment ()
increment()

# Accesing the modified global variable
print (counter) # Output: 2