# #Data Types
# char_num=len(input("Enter your name \n"))
# new=str(char_num) #Type casting
# print("Your name has "+new+" Characters.")

# a=str("123")
# a=float("23")
# b=float("123.4")
# print("$a+$b =", (a+b))

# # ** acts as the exponent function

# print(round(8/3,2))  #Rounding off a number to a deciaml place, the 2 states how many positions after decimal

# print(8 // 3) # "//" is used to get the result in integer

# #f-String  
# z=9
# print(f"Printing random {z}")

print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill ? $"))
tip=int(input("What percentage tip would you like to give? 10,12, or 15? "))
num_people=int(input("How many people to split teh bill?"))
tip_for_each=((total_bill*tip)/100)/num_people
total_amount=total_bill+(tip_for_each*num_people)
each_person=round(total_amount/num_people,2)
each="{:.2f}".format(each_person)
print(f"Each person should pay: ${each}")