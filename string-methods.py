
#? String Methods 
    # syntax: string_name.string_method(arguments)

# Formatting Methods
    # .lower() - returns the string with all lowercase latters
    # .upper() - returns the string with all uppercase letters
    # .title() - returns the string with first letter of each work capitalized

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

# Splitting Strings 
    # .split() - splits a string into substrings based on the argument. If no argument is given it will split at spaces
    # puts the sub strings into a list 

line_one = "The sky has given over"

# splits the string on spaces
line_one_words = line_one.split()
print(line_one_words)

# splits the string based on the argument given (and the argument is removed from the string)
split_on_e = line_one.split('e')
print(split_on_e)

# splitting with escape sequences
    # \n newline - allows us to split multiline strings by line breaks
    # \t horizontal tab - allows us to split multiline strings by tabs

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

# Joining Strings
    # .join()
    # Syntax: 'text'.join(string_name)
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

# Strip
featuring = "           rob thomas                 "
print(featuring.strip())

featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))

# Replace
    # .replace()
    # Syntax: string_name.replace(argument 1, argument 2)

# Find
    # .find()
print('smooth'.find('t')) # returns 4

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# Format
    # .format()
def favorite_song_statement(song, artist):
    return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))


#? String Methods
    # .split() - splits a string into substrings based on the argument. If no argument is given it will split at spaces
    # .join() - adds strings together 
    # .lower() - returns the string with all lowercase latters
    # .upper() - returns the string with all uppercase letters
    # .title() - returns the string with first letter of each work capitalized
    # .strip() - removes all whitespace characters from beginning to end or you can specifiy the character you want to remove
    # .replace() - takes two arguments and replaces all instances of the first argument with the second argument 
    # .find() - takes a string as an argument, searches the string and returns the first index value where the argument is located
    # .format() - takes variables as arguments and includes them in the string it's run on


