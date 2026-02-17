colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

# 1
[(c,s) for c in colors for s in sizes]

# 2
soled_out = [('Black', 'm'), ('White', 's')]
[c,s) for c in colors for s in sizes if (c,s) not in soled_out]
