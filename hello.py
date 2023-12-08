def check_return_type(function):
    if(type(function())==int):

    
        print("The Return Value Of The Given Function IS int: ",function())
    elif(type(function())==str):
        print("The Value Of The Function Is String: ",function())

    else:
        print("OUT OF THE OPTION")

def return_any_data():
    return "10"

check_return_type(return_any_data)#OUTPUT:The Value Of The Function Is String:  10
