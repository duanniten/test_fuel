def main(): 
    
    promp = "Fraction: "
    percent_fuel = convert(promp)
    text = gauge(percent_fuel)
    print(text)

def convert(promp : str):
    while True:
        try:
            x_y = input(promp)

            # try to separete x and y, imagine there is a '/'
            x_y = x_y.split(sep= '/')
            if len(x_y) != 2:
                raise SeparatorError

            # try to get values from splited
            x = int(x_y[0])
            y = int(x_y[1])

            # check if the x is greater then y
            if x > y:
                raise YOrXValueError
            
            # try to divide x to y\
            fuel = round((x/y*100))
            return fuel
        except SeparatorError:
            pass
        except YOrXValueError:
            pass
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

def gauge(fuel:int):
    if fuel >= 99:
        text_to_print = 'F'
    elif fuel > 1:
        text_to_print = f'{fuel}%'
    else:
        text_to_print =  'E' 
    return text_to_print   

class SeparatorError(Exception):
    """Exceção levantada para indicar um problema com um separador."""
    pass

class YOrXValueError(Exception):
    """Exceção levantada para indicar um problema com um separador."""
    pass


if __name__ == "__main__":
    main()    