
#? Functions 
    # function definition syntax:
        # def function_name():
            # function code here

def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station.")
    print("Take the Northbound N, Q, R, or W train 1 stop.")
    print("Get off the Times Square 42nd Street stop.")

# call the function to invoke it
directions_to_timesSq()

# ? Parameters & Arguments 
    # parameter is variable/data passed into the function declartion and can be used in the function body
    # argument is variable/data passed intp the function invokation which is then assigned to the parameter name

def generate_trip_instructions(location):
    print('Looks like you are planning a trip to visit', location)
    print('You can use the public subway system to get to', location)

generate_trip_instructions('Grand Central Station')