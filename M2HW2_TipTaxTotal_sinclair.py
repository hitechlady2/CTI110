#Meal total amount
# 06/06/17
# CTI-110 M2HW2- Tip Tax Total
# Benescha Sinclair

#Get the price of the meal.
Food_Charge = float(input('How much did the food cost? '))

#Calculate the 18% tip
Tip = Food_Charge * 0.18

#Display the amount that includes the 18% tip
print ('A 18% tip totals $', format(Tip, ',.2f'))

#Calculate the 7% sales tax
Sales_tax = Food_Charge * 0.07

#Display the amount which includes the 7% sales tax
print ('A 7% sales tax totals $', format(Sales_tax, ',.2f'))

#Calculate the total cost of meal, which includes 18% tip and 7 % sales tax
Total_Meal = Food_Charge + Tip + Sales_tax

#Display the total amounts.
print ('Your total meal cost is $', format(Total_Meal, ',.2f'))
