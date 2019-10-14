# Module 1 - Program: Allergy Check
# 1. [ ] get user input for categories of food eaten in the last 24 hours
#    save in a variable called input_test
#    example input
#    enter somethings eaten in last 24 hours: seafood, dairy, nuts, chocolate cake
# 2. [ ] print True if "dairy" is in the input_test string
#    [ ] Test the code so far
# 3. [ ] modify the print statement to output similar to below
#       example output
#           It is True that "seafood, dairy, nuts, and chocolate cake" contains "dairy"
#    Test the code so far trying input inc;uding the string "dairy" and without
# 4. [ ] repeat the process checking the input for "nuts", challenge add "Seafood" and "chocolate"
#    [ ] Test your code
# 5. [ ] challenge: make your code work for input regardless of case, e.g. - print True for "Nuts", "NuTs", "NUTS" or "nuts"
      
# Create Allergy check code
# then PASTE THIS CODE into edX

# [ ] get input for input_test variable

input_test = input("enter somethings eaten in last 24 hours: ")

# [ ] print "True" message if "dairy" is in the input or False message if not

"dairy" in input_test.lower()

# [ ] print True message if "nuts" is in the input or False if not

print('It is', 'nuts' in input_test.lower(), 'that',input_test, 'contains "nuts"')

# [ ] Challenge: Check if "seafood" is in the input - print message

print('It is', 'seafood' in input_test.lower(), 'that',input_test, 'contains "seafood"')

# [ ] Challenge: Check if "chocolate" is in the input - print message

print('It is', 'chocolate' in input_test.lower(), 'that',input_test, 'contains "chocolate"')

# Module 2 - Program: fishstore()
# create and test fishstore()
#   fishstore() takes 2 string arguments: fish & price
#   fishstore returns a string in sentence form
#   gather input for fish_entry and price_entry to use in calling fishstore()
#   print the return value of fishstore()
#       example of output: Fish Type: Guppy costs $1

# [ ] create, call and test fishstore() function 

fish_entry = input("enter a fish type: ")
price_entry = input("enter a price: ")

def fishstore(fish_type, fish_price):
    string = "Fish type: " + fish_type + " costs " + fish_price
    return string

print(fishstore(fish_entry, price_entry))

# Module 3 Program: Cheese Order
# set values for maximum and minimum order variables
# set value for price variable
# get order_amount input and cast to a number
# check order_amount and give message checking against
#   over maximum
#   under minimum
# else within maximum and minimum give message with calculated price

# Sample input and output:
#   Enter cheese order weight (numeric value): 113
#   113.0 is more than currently available stock
#   Enter cheese order weight (numeric value): .15
#   0.15 is below minimum order amount
#   Enter cheese order weight (numeric value): 2
#   2.0 costs $15.98

# [ ] create, call and test 
# then PASTE THIS CODE into edX

order_max = 100
order_min = 10
price_variable = 7.99
order_amount = input("Enter cheese order weight (numeric value): ")
#order_amount_cast = float(order_amount)
total_cost = float(price_variable) * float(order_amount)

if float(order_amount) > order_max:
    print(order_amount + " is more than currently available stock")
elif float(order_amount) < order_min:
    print(order_amount + " is below minimum order amount")
else:
    print(order_amount + " costs $" + str(total_cost))

#Module 4 Program: str_analysis() Function
#Create the str_analysis() function that takes 1 string argument and returns a string message. 
#The message will be an analysis of a test string that is passed as an argument to str_analysis(). 
#The function should respond with messages such as:

#   "big number"
#   "small number"
#   "all alphabetic"
#   "multiple character types"
#The program will call str_analysis() with a string argument from input collected within a while loop. 
#The while loop will test if input is empty (an empty string "") and continue to loop 
# and gather input until the user submits at least 1 character (input cannot be empty).

#The program then calls the str_analysis() function and prints the return message.

#Sample input and output:
#   enter nothing (twice) then enter a word
#       enter word or integer: 
        #enter word or integer: 
#       enter word or integer: Hello
#       "Hello" is all alphabetical characters!

#   alphabetical word input
#       enter word or integer: carbonization
#       "carbonization" is all alphabetical characters!

#   numeric inputs
#       enter word or integer: 30
#       30 is a smaller number than expected

#       enter word or integer: 1024
#       1024 is a pretty big number

#loop until non-empty input is submitted
#Once the user gives input with characters use the input in calling the str_analysis() function.

#Additional Details
#In the body of the str_analysis() function:

#Check if string is digits
#   if digits: convert to int and check if greater than 99
#       if greater than 99 print a message about a "big number"
#       if not greater than 99 print message about "small number"
#check if string isalpha then (since not digits)
#   if isalpha print message about being all alpha
#if not isalpha print a message about being neither all alpha nor all digit

#call the function with a string from user input

#Run and test your code before submitting
# [ ] create, call and test the str_analysis() function  

def str_analysis(input_string):
    if input_string.isalpha():
        print('"' + input_string + '"' + ' is all alphabetical characters!')
    elif input_string.isdigit():
        if int(input_string) > 99:
            print(input_string + " is a pretty big number")
        else:
            print(input_string + " is a smaller number than expected")
    else:
        print('"' + input_string + '"' + ' is neither alpha or digits')
              
            
string_arg = ""

while string_arg == "":
    string_arg = input("enter word or integer: ")
else:        
    print(str_analysis(string_arg))  