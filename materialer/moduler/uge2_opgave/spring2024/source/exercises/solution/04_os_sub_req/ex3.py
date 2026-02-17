def match_ends(words):
    return len([w for w in words if len(w) > 1 and w[0] == w[-1]])

def front_x(words):
    x = [w for w in words if w[0] == 'x'] 
    y = [w for w in words if w[0] != 'x']
    return sorted(x) + sorted(y)

def sort_last(tuples):
    # this one is not realy suitable for list comprenhensions
    
    def last_element(t):
        return t[-1]

    return sorted(tuples, key=last_element)

# the last ones are not realy suitable for list comprenhensions

def remove_adjacent(nums):
    return list(set(nums)) # sets can only have unique elements 


def linear_merge(list1, list2):
    """
    res = []
    c1 = 0
    c2 = 0

    while len(list1) != c1 and len(list2) != c2:
        if list1[c1] < list2[c2]:
            res.append(list1[c1])
            c1 = c1 + 1 
        else:
            res.append(list2[c2])
            c2 = c2 + 1
        
        if len(list1) == c1:
            res = res + list2[c2:]

        if len(list2) == c2:
            res = res + list1[c1:]
    return res
    """
    # OR JUST:

    return sorted(list1+list2)

