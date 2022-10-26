# class Robot:
#     def __init__(self, name, version_number):
#     #we initialize the attributes of the class into initialize attributes
#     ## for each method of the class, we are going to have first the self parameter
#         # create new variables
#         # so when you self this actually refers to the object
#         self.name = name
#         self.version_number = version_number
#         self.internal_temperature = 25.0
#
#     def say_hi(self):
#         print("Hello, my name is " + self.name +
#               ", ready to help!")
#
#     def init_hardware(self):
#         print("Init hardware")
#
#     def print_info(self):
#         self.say_hi()
#         print("Version number: " + str(self.version_number))
#         print("Temperature: " + str(self.internal_temperature))
#
# class RoboticArm(Robot):
#     def __init__(self, name, version_number, reach):
#         super().__init__(name, version_number)
#         self.reach = reach
#
#     def pick_object(selfself, x, y):
#         print("Pick object on (" + str(x) + ", " + str(y) + ")")
#
#     def place_object(self, x, y):
#         print("Place object on (" + str(x) + ", " + str(y) + ")")
#
# class PackagingSolution:
#     def __init__(self, robot_right, robot_left):
#         self.robot_right = robot_right
#         self.robot_left = robot_left
#
#     def package(self, pick_x, pick_y, middle_x, middle_y, place_x, place_y):
#         self.robot_right.pick_object(pick_x, pick_y)
#         self.robot_right.place_object(middle_x, middle_y)
#         self.robot_left.pick_object(middle_x, middle_y)
#         self.robot_left.place_object(place_x, place_y)

# print("test")
# my_robot = Robot("R2D2", 2)
# my_robot2 = Robot("C3P0", 1)
# my_robotic_arm = Robot("Qush", 4, 300)

#my_robotic_arm = RoboticArm("Bob", 4, 300)
# robotic_arm_right = RoboticArm("Bob", 4, 300)
# robotic_arm_left = RoboticArm("John", 2, 300)
# packaging_solution = PackagingSolution(robotic_arm_right, robotic_arm_left)
#
# packaging_solution.package(1, 2, 3, 4, 5, 6)

# my_robot.say_hi()
# my_robot2.say_hi()
# my_robot.init_hardware()

# my_robot.print_info()
# my_robot2.print_info()
#
# my_robotic_arm.print_info()
# my_robotic_arm.pick_object(3, 4)
# my_robotic_arm.place_object(5, 6)

# print(my_robot.name)
# print(my_robot2.name)


#-----------Example-3-------------------#
# #def say_hello(user_name):
# def say_hello(user_name, user_age):
#     # print("Hello " + user_name)
#     print("Hello " + user_name + ", you are " + str(user_age) + " years old.")
#
# def double_number(number):
#     # result = number * 2
#     # return result
#     return number * 2
#
# def print_double_number(number):
#     result = double_number(number)
#     print("Double of " + str(number) + " is " + str(result))

#-----------Example-2-------------------#
# say_hello("Adam", 32)
# say_hello("Atiqah", 27)
# number = double_number(3) #
# print(number)
# print_double_number(3)
# print(result) #will produce error since result is inside a variable def loop not outside

#-----------Example-1-------------------#
# # Ask the user's name
user_name = input("What is your name? ")
# Ask the user age
user_age = input("How old are you? ")

# Print user's name and age
print("Hello " + user_name + ", you are " + user_age + " years old.")

# # This is a comment. It will not be executed.
# To comment all: highlight and press Ctrl /