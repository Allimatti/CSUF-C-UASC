#########################################################################
#####                       MAIN_INTERFACE.PY                       #####
#########################################################################

# all names are placeholder, make good descriptive names

# example to import an entire file
import flight_controls

# example to import a specific submodule from a file
# from ground_station.py import submodule_a

def main():
    # example to call a function from another module within a main function
    output = flight_controls.flight_control_function1(argument)

# some superloop to constantly output some stuff
while True:
    some_motor = some_output
    some_pulse = some_sensor_input
    some_voltage = some_battery_output
    # etc etc...