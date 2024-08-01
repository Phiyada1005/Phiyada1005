input_string = input("enter a string: ")

modified_striing = ""

voeels = "aeiouAEIOU"

for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_string = "*"
    else:
        modified_string = upper_char
print("modified string:", modified_string)