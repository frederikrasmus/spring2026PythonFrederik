def sort_cons(s):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        s = s.lower().replace(i,'')
    
    return sorted(s)

print(sort_cons('Hello world'))
