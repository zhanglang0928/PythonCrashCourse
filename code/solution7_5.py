# Movie Tickets
prompt = 'How old are you?'
prompt = '\nEnter "quit" when you are finished. '

while True:
    age = input(prompt)
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("The ticket is free!")
    elif age > 12:
        print("The ticket is 15 dollars.")
    else:
        print("The ticket is 10 dollars.")

