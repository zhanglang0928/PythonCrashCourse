# Pizza Toppings
prompt = "\nWhat topping would you like on you pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("I'll add " + topping + " to your pizza.")
    else:
        break
