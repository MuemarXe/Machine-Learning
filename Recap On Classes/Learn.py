#modules in python 
def making_pizza(size,*toppings):
    print("\nMaking a "+ str(size)+"-inch pizza with toppings ")
    for topping in toppings:
        print("-"+topping)