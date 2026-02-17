
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Words exercise
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
Use str.split() (no arguments) to split on all whitespace.
Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def util(filename):
    d = {}
    f = open(filename)
    words = f.read().split()
    
    for i in words:
        i = i.lower()
        if i in d.keys(): 
            d[i] += 1
        else:
            d[i] = 1
    return d


def print_words(filename):

    x = dict(sorted(util(filename).items()))
    for i, j in x.items():
        print(f'{i}\t\t{j}')


def print_top(filename):
    
    x =  list(util(filename).items())
    x = sorted(x, reverse=True, key=lambda x: x[-1])
    x = dict(x[:20])
    
    for i, j in x.items():
        print(f'{i}\t\t{j}')


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: python words.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]      # -> --count or --topcount
  filename = sys.argv[2]    # -> the name of the file to read from

  # call the function based on which option is specified
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

main()
