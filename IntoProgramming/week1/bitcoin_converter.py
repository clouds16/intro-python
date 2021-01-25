current_price = 37762.10
date = "1/13/2021"
time= "11:12 pm "

print('As of', date, "at" , time , "bitcoin is currently trading at ", str(current_price), "per bitcoin")

def conversion(price ):
    quantity = float(input( "input a bitcoin quantity: "))
    output = quantity * price
    print("That is worth:" , output , "dollars")

conversion(current_price)