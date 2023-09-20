
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

# Examples:

# converts farenheit to celsius
def f_to_c(f_temp):
    c_temp = (f_temp-32)*(5/9)
    return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#converts celsius to fahrenheit
def c_to_f(c_temp):
    f_temp = (c_temp)*(9/5) +32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


# another example calculating force 
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
    return mass*acceleration

train_force = get_force(train_mass, train_acceleration)
print('The GE train supplies', train_force, 'Newtons of force')


#?Function with default parameter/argument 
    # will use default parameter if no argument is passed. If an argument is passed it will override the default parameter

def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth

print('Default Parameter Example:')
findvolume(2,1)

#?Functions with keyword arguments
    # Allows for arguments to be passed in any order 
    
def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth

print('keyword argument example:')
findvolume(length=5, depth=2, width=4) # overrides the default parameter and is given in a different order than the parameters of the function
