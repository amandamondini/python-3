
#? Strings
    # A string is a sequence of charaters contained within a pair of '' or "". Can be any length and contain letters, number, symbols and spaces
    # Each character of a string has an index
    # strings are immutable (cannot change once it's created)

# Indexing & Strings 
my_name = 'Amanda'
first_initial = my_name[0]
print(first_initial)

# Slicing Strings
    #Syntax:
        # name[:5] - starts at 0 index and continues to 5th index
        # name[5:] - starts at 5th index and continues to end of string
        # range of letters: name[2:5] (will print starting frm index 2 and go to index 5 but won't print index 5)
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
last_letters = last_name[5:]
print('Index Example:')
print(new_account)
print(last_letters)

# Concatenate Strings

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
    account_name = first_name[:3] + last_name[:3]
    return account_name

new_account = account_generator(first_name, last_name)
print('Concatenate Example:')
print(new_account)

# Accessing last character(s) of a string 
favorite_fruit = 'pineapple'
last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char)

# gets last 4 characters
length = len(favorite_fruit)
print(length)
last_chars = favorite_fruit[length-4:]
last_chars2 = favorite_fruit[5:]
print(last_chars)
print(last_chars2)

#! Easier way to access ends of strings is using negavtive indices
    # string_name[-1] -> gets you last character of string
    # string_name[-2] -> gets you second last character of string
    # string_name[-3:] -> gets you last three characters of string


# Iterating through Strings
def get_length(string):
    count = 0
    for letter in string:
        count += 1
    return count

print(get_length('Amanda'))

# Strings & Conditionals 
def letter_check(word, letter):
    for char in word:
        if letter == char:
            return True
        else: 
            return False

print(letter_check('apple', 'e'))

#! easier way to iterate through strings using in
    # using in will return a boolean expression 

print("e" in "blueberry" and "e" in "carrot")

def contains(big_string, little_string):
    return little_string in big_string

# returns a list with all letters string one and string two have in common
def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common


#creates a username using the first three letters of the first name and the first 4 letters of the last name 
def username_generator(first_name, last_name):
    if len(first_name) < 3 and len(last_name) < 4:
        user_name = first_name + last_name
    elif len(first_name) < 3 and len(last_name) >= 4:
        user_name = first_name + last_name[:4]
    elif len(first_name) >= 3 and len(last_name) < 4:
        user_name = first_name[:3] + last_name
    else:
        user_name = first_name[:3] + last_name[:4]
    return user_name

print(username_generator('Amanda', 'Mondini'))


def password_generator(username):
    length = len(username)
    password = username[-1] + username[0:length-1]
    return password

print(password_generator('AbeSimp'))

print('________________')
