# (Solution) Decorator / Context Manager

Create a simple function that prints the paramenters value to console.


```python
def quotes(*args):
    for _ in args:
        print(_)

quotes(('Honey Im home!', 'A car is a car until ...'))
```

    ('Honey Im home!', 'A car is a car until ...')


> You should decorate this function so it can get its quotes from:

> 1. a text file
> 2. a csv file
> 3. a json file
> 4. a SQlite databs

### Solution text file


```python
!cat testfiles/bohr.txt
# The content of bohr.txt
```

    An expert is a person who has made all the mistakes that can be made in a very narrow field.
    Prediction is very difficult, especially about the future.
    Those who are not shocked when they first come across quantum theory cannot possibly have understood it.


```python
def text_file_decorator(func):
    def inner(*args):
        with open('testfiles/bohr.txt', 'r') as f:
            func(''.join(f.readlines())) # or *list -> list unpacking
    return inner

```

### Solution csv file


```python
!cat testfiles/bohr.csv
# The content of bohr.csv
```

    id, quote, author
    1, An expert is a person who has made all the mistakes that can be made in a very narrow field., bohr
    2, Prediction is very difficult, especially about the future., bohr
    3, Those who are not shocked when they first come across quantum theory cannot possibly have understood it., bohr


```python
import csv
def csv_decorator(func):
    def inner(*args):
        with open('testfiles/bohr.csv', 'r') as f:
            csv_r = csv.reader(f, delimiter=',')
            next(csv_r)                            # skip first row
            func(*[row[1] for row in csv_r])       # get content column, and unpack list
    return inner
```

### Solution JSON


```python
!cat testfiles/bohr.json
# The content of bohr.json
```

    [{"quote": "An expert is a person who has made all the mistakes that can be made in a very narrow field."}, {"quote": "Prediction is very difficult, especially about the future."}, {"quote": "Those who are not shocked when they first come across quantum theory cannot possibly have understood it."}]


```python
import json

def json_decorator(func):
    def inner(*args):
        with open('testfiles/bohr.json', 'r') as f:
            txt = f.read()
            js = json.loads(txt) 
        func(*[i['quote'] for i in js])
    return inner

```

## Solution SQlite 


```python
from sqlite3 import connect
# create db 
def conn():
    with connect('testfiles/bohr.db') as conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS quotes')
        cur.execute('CREATE TABLE quotes(id int PRIMARY KEY, quote text, author text)')
        cur.execute('INSERT INTO quotes(id, quote, author) VALUES (1, "An expert is a person who has made all the mistakes that can be made in a very narrow field.", "bohr")')
        cur.execute('INSERT INTO quotes(id, quote, author) VALUES (2, "Prediction is very difficult, especially about the future.", "bohr")')
        cur.execute('INSERT INTO quotes(id, quote, author) VALUES(3, "Those who are not shocked when they first come across quantum theory cannot possibly have understood it.", "bohr")')
        return cur
# conn()
```


```python
def sqlite_decorator(func):
    def inner(*args):
        with connect('testfiles/bohr.db') as conn:
            cur = conn.cursor()
            func(*(i[0] for i in cur.execute('SELECT quote FROM quotes'))) # result from db is return as rows of tuples. i[0] gives the first element of the tuple
    return inner
```

### Original function (now decorated)


```python
#@text_file_decorator
#@csv_decorator
#@json_decorator
@sqlite_decorator
def quotes(*args):
    for _ in args:
        print(_)
        
quotes('Honey Im home!', 'A car is a car until ...')
```

    An expert is a person who has made all the mistakes that can be made in a very narrow field.
    Prediction is very difficult, especially about the future.
    Those who are not shocked when they first come across quantum theory cannot possibly have understood it.



```python

```
