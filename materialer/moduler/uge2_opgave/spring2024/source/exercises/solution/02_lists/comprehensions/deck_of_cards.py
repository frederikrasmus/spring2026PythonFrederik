# deck_of_cards.py

numbers = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

x = [(i,chr(j)) for i in numbers for j in range(9824, 9828)]
