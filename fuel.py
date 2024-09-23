def main(): 
    
    promp = "Fraction: "
    x_y = input(promp)
    percent_fuel = convert(x_y)
    text = gauge(percent_fuel)
    print(text)

def convert(x_y : str):
    
        # try to separete x and y, imagine there is a '/'
        x_y = x_y.split(sep= '/')

        if len(x_y) != 2:
            raise ValueError

        # try to get values from splited
        x = int(x_y[0])
        y = int(x_y[1])

            # check if the x is greater then y
        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError
            
        # try to divide x to y\
        fuel = round((x/y*100))
        return str(fuel)
        
    

def gauge(fuel:int):
    if fuel >= 99:
        text_to_print = 'F'
    elif fuel > 1:
        text_to_print = f'{fuel}'
    else:
        text_to_print =  'E' 
    return text_to_print   

if __name__ == "__main__":
    main()    