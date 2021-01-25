

class Temp:
    def __init__(self, scale, temp):
        
        if scale == 'f':
            t = (9/5)* temp + 32
            print("The temperature in Farenheight is ", t , "degrees\n Press Ctrol+C to exit or continue\n")
    

           
        elif scale == 'c':
            t = (5/9)*(temp-32)
            print("The temperature in Celcius is ", t , "degrees\nPress Control+C to exit or continue\n")


        # else: 
        #     print("please input either 'c' for celcisu or 'f' for farenheight")
        

if __name__ == "__main__":
    
    while True:
        print('Do you want to conver to Celcius (c) or Farenheight (f) ?')
        t_type = str(input())
        if t_type == "c" :
            print("What is the temperature in Fareheight you wish to convert?")
            convert_temp = float(input())
            
            temp= Temp(t_type, convert_temp)

        elif t_type == "f" :
            print("What is the temperature in Celcius you wish to convert?")
            convert_temp = float(input())
            
            temp= Temp(t_type, convert_temp)

        else: 
            print('that is not an acceptable temperature type')
    
    
        
        # exitcheck()
