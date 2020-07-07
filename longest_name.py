#  Have a list of names
#  #  Get names from user
#  #  #  Prompt the user
#  #  #  #  Don't accept empty names
#  #  #  Know when the list is done
#  #  Put them in list
#  Find the length of each one
#  #  Loop through the list
#  #  Use len() to get the length
#  #  Keep track of the longest
#  Print the result


def get_list_of_names():
    result = []
    name = 'none yet'
    while True:
        name = input('Enter a name (enter "done" to stop):')
        if name == 'done':
            break
        result.append(name)
    return result


names = get_list_of_names()

longest = ''
for name in names:
    if len(name) > len(longest):
        longest = name

print(longest, 'had the longest name.')
