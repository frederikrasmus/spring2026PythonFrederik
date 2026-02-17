# sort a list

# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
 names = [‘Claus’, ‘Ib’, ‘Per’]

# Sort this list by using the sorted() build in function.
sorted_names = sorted(names)

#  Sort the list in reversed order.
sorted_names_reversed = sorted(names, reverse=True)

# Sort the list on the lenght of the name.
length = sorted(names, key=len)

# Sort the list based on the last letter in the name.
def last(s):
    return s[-1]

sorted(names, key=last)

#  Sort the list with the names where the letter ‘a’ is in the name first.
def a_in(s):
    if 'a' in s.lower():
        return True
    return False

sorted(names, key=a_in)
