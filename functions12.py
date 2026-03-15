import random

def print_car_list():
    car_list = ["FORD","TOYOTA","MAZDA"]
    # store a list of cars in a variable
    for i in car_list:
       #Loops  each car brand in the list
       print("-",i)
     #Prints the list of available cars.

          

def show_car_details():
    ford = {"Name" : "FORD","Model": "mustang","Year" : 2025,"Color" : "red","Price": "$ 40 000"}
    toyota = {"Name" : "TOYOTA","Model": "Camry","Year" : 2025,"Color" : "white","Price": "$ 50 000"}
    mazda = {"Name" : "MAZDA","Model": "Explorer","Year" : 2025,"Color" : "black","Price": "$ 30 000"}
    car_details = {"ford" : ford,"toyota" : toyota,"mazda" : mazda } 
    #Dictionaries containing details for each car  
    choice_car = str(input(" Choose a car: 1 = Ford, 2 = Toyota, 3 = Mazda :  "))
    # Ask the user to choose a car
    print("\n")

    if choice_car == "1":
        selected = car_details["ford"]
        # If the user enter 1, it displays the ford details
    elif choice_car == "2":
        selected = car_details["toyota"]
        #  otherwise If the user enter 1, it displays the toyota details
    elif choice_car == "3":
        selected = car_details["mazda"]
        #  otherwise If the user enter 1, it displays the mazda details
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        #Otherwise it displays this message
        return show_car_details();#return the function if input is invalid
    for key, value in selected.items():
         print(key, ":", value)
    return selected; # Return the selected car

def next_action(selected):
    choice = input("Do you want to buy this car? (Y/N): ")
    #Asks the user if they want to buy the selected car

    if choice.upper() == "Y":
        print("Great choice! We will prepare the purchase.")
        invoice(selected)
        #If the user enter Y , it will call the invoice function
    elif choice.upper() == "N":
        print("No problem, choose another car.")
        return show_car_details()
    #If the user enter Y , it will call the show_car_details function
    else:
        print("Invalid answer. Please enter Y or N.")
        return next_action(selected) 
    #Otherwise  it will display  this message and return the next function

def invoice(selected):
    buyer = (str(input("Enter your full name ")))
    # Ask the user to enter his name
    code = "CP" + str(random.randint(1000, 9999))
    # Generate a random purchase order number
    
    print("\n ---------- INVOICE ----------")
    print("Customer Name :", buyer)
    print("PO Number :", code)
    print("Car Purchased :", selected["Name"])
    print("Model : ", selected["Model"])
    print("Year : ", selected["Year"])
    print("Color : ", selected["Color"])
    print("Price : ", selected["Price"])
    print("------------------------------------")
    # Display invoice details

def continue_program():
  buy_a_car = input("Do you wish buy another car? enter Y for yes: ")
# Enter Y if you want to buy another car
  if buy_a_car .upper() == "Y":
    return True
  # If you enter Y, the program will continue
  else :
    print("Thank you for your purchase")
    # Otherwise it displays this message.    
    
    
