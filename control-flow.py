
#? Relational operators 
    # compare two items and return True or False (boolean value)
print(3 == 3)
print(3 != 3)
print((4 <= 2 * 3) and (7 + 1 == 8))

#? Boolean Variables 
    # True and False are a type of variable bool

set_true = True
set_false = False
print(type(set_true))

    #! Condtional Statements

#? If Statement 
    #Syntax:
test_value = 100
if test_value > 1:
    print("This code is executed")
    
#? Else Statement 
    #Syntax
    test_value2 = 0
    if test_value2 > 1:
        print("Greater than One")
    else:
        print("Less than One")
        
#? Else If Statement 
    #Syntax:
    test_value3= 'fish'
    if test_value3 == 'dog':
        print("Test value is dog")
    elif test_value3 == 'cat':
        print('You have a cat')
    else:
        print("unknown")

#? Relational & Boolean Operators 
    '''
        == equals
        != not qeuals
        > greater than
        >= greater than or equal to
        < less than
        <= less than or equal to
    '''
    credits = 120
    gpa = 3.4
    if credits >= 120 and gpa >= 2.0:
        print("You meet the requirements to graduate!")
    
    if credits >= 120 or gpa >= 2.0:
        print('You have met at least one of the requirements')

    if not credits >= 120:
        print('You do not have enough credits to graduate.')

    if not gpa >= 2.0:
        print('Your GPA is not high enough to graduate.')

    if not (credits >= 120) and not (gpa >= 2.0):
        print('You do not meet either requirement to graduate!')