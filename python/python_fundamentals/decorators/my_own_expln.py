# decorator function
    # takes in a function to be called

# outside u want to call the decorator fn by tak

# idea is that u want to let people use your decorator function
# without them knowing what u are doing under the hood => just know the rough functionality &
# what THEY should do in their function for it to work
# then they just call their function name, but executes the decorator as a whole

def decorator(func_to_take_in):
    def wrapper():
        print("other do smt") # do smt
        func_to_take_in()
        print("other do smt") # do smt
    return wrapper

def func_to_take_in():
    print("naive code wants to do smt")

func_to_take_in = decorator(func_to_take_in)

# naive coder will call the "func_to_take_in" function
func_to_take_in()