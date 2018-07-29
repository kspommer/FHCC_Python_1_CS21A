###########################################################
# Course:  CS 21A Python Programming: Lab #2
# Name:  Susan Pommer
# Description:  Based on user input of their grocery bill
#   amount, this program calculates a discount coupon amount.
#   A loop to allow a tester to control the number of test
#   run is included.  
# File name:  SusanPommerLab2.py
# Date:  July 16, 2017
###########################################################

# Provide loop to allow tester to control number of test runs
# Initialize sentinel value
test_again = 'y'

while test_again == 'y' or test_again == 'Y': 

    # Initialize the grocery_bill variable
    grocery_bill = 0.0

    # Ask user to input price of groceries
    grocery_bill = float(input("\nPlease enter the cost of your groceries ($): "))

    # if-elif-else loop:  Identify coupon percentage to apply
    if grocery_bill < 10.0:
        coupon_percentage = 0.0
    elif grocery_bill >= 10.0 and grocery_bill < 60.0:
        coupon_percentage = 0.08
    elif grocery_bill >= 60.0 and grocery_bill < 150.0:
        coupon_percentage = 0.10
    elif grocery_bill >= 150.0 and grocery_bill < 210.0:
        coupon_percentage = 0.12
    else: 
        coupon_percentage = 0.14

    # Initialize coupon value
    coupon_value = 0.0

    # Calculate coupon amount
    coupon_value = coupon_percentage * grocery_bill

    # Display formated user output if coupon available
    if coupon_percentage != 0.0:    
        print("You win a discounted coupon of $", \
            format(coupon_value, ',.2f'), \
            ". (", format(coupon_percentage, ',.0%'), \
            " of your purchase)\n", sep='')
    # provide user confirmation of no coupon 
    else: 
        print("Sorry, you did not earn a discount coupon today.\n")
        
    # Ask program tester if they want to run another test
    test_again = input("Do you want to run another test? (y/n)\n")

        
################## SAMPLE RUNS ########################       
#Please enter the cost of your groceries ($): 0
#Sorry, you did not earn a discount coupon today.

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 5.54
#Sorry, you did not earn a discount coupon today.

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 9.99
#Sorry, you did not earn a discount coupon today.

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 10
#You win a discounted coupon of $0.80. (8% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 44.56
#You win a discounted coupon of $3.56. (8% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 59.99
#You win a discounted coupon of $4.80. (8% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 60
#You win a discounted coupon of $6.00. (10% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 122.34
#You win a discounted coupon of $12.23. (10% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 149.99
#You win a discounted coupon of $15.00. (10% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 150.00
#You win a discounted coupon of $18.00. (12% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 198.64
#You win a discounted coupon of $23.84. (12% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 209.99
#You win a discounted coupon of $25.20. (12% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 210
#You win a discounted coupon of $29.40. (14% of your purchase)

#Do you want to run another test? (y/n)
#y

#Please enter the cost of your groceries ($): 1200.54
#You win a discounted coupon of $168.08. (14% of your purchase)

#Do you want to run another test? (y/n)
#n
#>>> 
################## SAMPLE RUNS ######################## 
          
