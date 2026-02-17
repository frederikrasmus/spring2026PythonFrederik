import sys

def main(argv):
    if argv[1] != '-it':
        print('Usage: python script.py [-it]{--rm}')
    if len(argv) == 3 and argv[2] != '--rm':
        print('Usage: python script.py [-it]{--rm}')
    elif len(argv) == 3 and argv[2] == '--rm':
        print('Goodby')
    else:
        input()

    sys.exit()

main(sys.argv)



