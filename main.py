from functions12 import*
# Import all functions from functions12 
import datetime
#Import date and time
x = datetime.datetime.now()
#Have the current date and time
print("       ",x)
#Display date and time

print ("""*** Welcome to our online car dealer ship ***
   * we open from monday to saturday *
       * Schedule: 7h AM to  5h PM *\n
    * Here is the list of cars *\n""")
# Display a welcome message



continue_prog = True

while (continue_prog) :
 # Loop continues as long as continue_prog is True   
    print_cars = print_car_list()
    # It Calls function to display the list of cars
    print("\n")
    selected = show_car_details()
    #It Calls function to display the  car details and return selected car
    next_action(selected)
    # It calls the nex_action function to ask the user his name and return the invoice.
    continue_prog = continue_program()
    # It calls the continue_program function to ask if you want to restart the program
    # or to end it.





