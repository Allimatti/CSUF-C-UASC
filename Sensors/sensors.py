#########################################################################
#####                          SENSORS.PY                           #####
#########################################################################

# all names are placeholder, make good descriptive names

# from sensors_submodule_a import submodule_x
# from sensors_submodule_b import submodule_y
# from sensors_submodule_c import submodule_z

# definition for some sensor function
# define as many functions as needed to use submodules

# placeholder library for SR-04 sensors
# placeholder GPIO pin that will be replaced once we actually assemble the electronics
from usedgpiopin import DistanceSensor

sensor = DistanceSensor(pin1, pin2)

# while loop for printing real-time distance data to the terminal
while True:
    print("Distance to object/payload: ", sensor.distance, " m")

def sensor_function1(parameters):
    dummy_variable = parameters
    # insert code here
    return dummy_variable

# empty list (array) for data manipulation if needed
some_list = []

# a for loop to do whatever if needed
for dummy in some_list:
    logic_stuff = dummy
    # insert more code here

# call a function to do stuff
sensor_function1(logic_stuff)
