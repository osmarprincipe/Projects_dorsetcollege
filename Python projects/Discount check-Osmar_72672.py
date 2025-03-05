# Defining a range for age and price

age = (0 , 101)
price = (0 , 10000)

# Starting the loop

costumerleft = ('yes')
while costumerleft == ('yes') :
    age = int(input('Please enter your age: '))
    total_price = int(input('Please enter the price of the product (Euro): '))
    if age < 18 and (total_price) * 0.9 >= 100  :
        print (' The final price is:', int(((total_price/100) * 90)) - 10 )
        print ('You have earned: 10% discount and €10 promotion discount. ')
    elif age < 18 and (total_price) * 0.9 <= 100 :
        print (' The final price is: ' , int((total_price/100)* 90))
        print ('You have earned: 10% discount.')
    elif age > 18 and total_price >= 100 :
        print (' The final price is:', total_price - 10)
        print ('You have earned €10 promotion discount.')
    else :
       print ('The final price is :', total_price)
       print ('you have no discount')
    costumerleft = (input('Would you like to enter another customer? (yes/no)'))  
print ('Thanks so much , bye')
    
         



