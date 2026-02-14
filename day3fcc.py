base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = True
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)
#Step 12 Now create a variable named extra_charges and set it to 0. This will represent extra charges to apply to the movie ticket on weekends.
# Then, create an if statement to check if is_weekend is truthy. Inside the body of if statement, update the extra_charges value to 2 and print Extra charges will be applied in the terminal.

extra_charges = 0
if is_weekend:
    extra_charges = 2
    print("Extra charges will be applied")

  #Now, add an else clause to your if statement and print No extra charges will be applied inside the else body. This will print the message only when the extra charges condition is false.  
  #Then, below the else clause, use the print() call to display a message that shows Extra charges: followed by the updated value of extra_charges and check the output in the terminal.
else:
    print("No extra charges will be applied") 

# display updated extra charges value
print("Extra charges:", extra_charges)


#Extra charges should also apply if the show is in the evening. Use the or operator to combine the existing condition of your if statement with a second condition checking if show_time is equal to the string Evening.
extra_charges = 0
if is_weekend or show_time  == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

#Now you will check if the user satisfies the conditions to book a movie ticket. Users with age 21 or above can always book tickets without any restrictions.
#Create an if statement to check if age is greater than or equal to 21. Inside the body of the if statement, print Ticket booking condition satisfied to the terminal.
#Then, add an else clause to your if statement and print Ticket booking failed due to restrictions inside the else body.

# example variable
age = 21

# check booking condition
if age >= 21:
    print("Ticket booking condition satisfied")
else:
    print("Ticket booking failed due to restrictions")
