def my_function():
    local_variable = "I'm inside the function"
    print(local_variable)
     
# Calling the function
my_function()

#Trying to acces the local variable outside the function will raise an error
#print(local_variable) # NameError: name 'lacal_variable' is not defined