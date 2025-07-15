# Empty class.
class User:
    # 'pass' is a keyword necessary to create an empty class.
    pass


user_1 = User()
# Creation of an attribute outside the class.
user_1.id = "001"
user_1.username = "Luis"

print(user_1.username)


# ----------------------------------------------------------------------------------------------------------------------#
# Convenient way to create a class
class Car:
    # Constructor in Python
    def __init__(self, seats, brand):
        print("New car being created...")
        self.seats = seats
        self.brand = brand
        self.horse_power = 120
        self.kilometers = 0

    # Methods inside a class always need to have the 'self' keyword,
    # so the program knows which object called the function.
    def enter_race_mode(self, horse_power):
        self.seats = 2
        self.horse_power = horse_power


my_car = Car(5, "Mazda")
print(my_car.kilometers)
my_car.enter_race_mode(180)
print(my_car.horse_power)
