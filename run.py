def SimpleMenu():
    """
    Offer a simple menu that presents two options to the user.
    """
    user_options = ("red", "blue", "green", "yellow", "purple", "orange")
        

    while True:
        print("Please choose from the following?")
        print("What is your favorite colour?")

        user_choice = input("Enter your data here:\n")

        if user_choice in user_options:
            print (f"{user_choice} is your favourite colour... well la-di-da!" ) 
            break
        else:
            print ("That is not an option you bloody idiot!!")
            break

SimpleMenu()