Str = "Welcome to Python"

# string to Upper case
print("Upper case Converted String:","\n",Str.upper())

#string to Lower case
print("Lower case Converted String:","\n",Str.lower())

# Title converts the first character to upper case and rest to lower case
print("Title case Converted String:","\n",Str.title())

#swaps the case of all characters in the string upper case character to lowercase and viceversa
print("Swap case Converted String","\n",Str.swapcase())

# convert the first character of a string to uppercase
print("Capitalize case Converted String","\n",Str.capitalize())

# Strings as Array
print("The String index","\n",Str[1])

# original string never changes
print("The Original String","\n",Str)

#Length of the string
print("The length of the string is ",len(Str))

# Check string
if "Python" in Str:
  print("Yes, 'Python' is present in the string.")

# Check if not in string
if "Code" not in Str:
  print("No, 'Code' is NOT present in the string.")


# String  Slicing 

print("Start at Oth index to end \n",Str[0:]) 
print("Starts at 1th index to 4th index \n",Str[1:5])  
print("Starts at 2nd index to 3rd index ",Str[2:4])  
print("Starts at 0th to 2nd index  ",Str[:3])

#String looping
for s in Str:
    print(s)

# Replace anything from string
R = "Hello, World!"
print(R.replace("H", "J"))

# Escape Character

string = "I Like the \"Apples\" from the north."
print(string)
