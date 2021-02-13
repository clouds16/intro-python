import math

def calculations(man_total, Outside_diameter, core_vol):

    radius = Outside_diameter/2
    sphere_vol= (4/3)* math.pi* math.pow(radius,3)
    calc_total = man_total* (sphere_vol - core_vol)
    print("you will need ", calc_total, "inches cubed of filler")

def main():
    manufacturing_total_input= float(input("How many bowling balls will be manufactured? " ))
    od_input= float(input("what is the diameter of each ball in inches? " ))
    corevinput = float(input("what is the core volume in inches cubed? " ))
    calculations(manufacturing_total_input, od_input, corevinput)

if __name__ == '__main__':
    main()
 
   