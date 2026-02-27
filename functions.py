def input_name():
    Name = str(input("May I have your name please?  "))
    return Name;

car_list = ["FORD","TOYOTA","MAZDA"]

def print_car_list(car_list):
    for i in car_list:
       print("-",i)
       return print_car_list