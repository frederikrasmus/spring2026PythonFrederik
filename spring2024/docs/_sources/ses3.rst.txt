Session 3 - Python one-liners 
=============================
Today everything we do will be expressed throgh code that fits on one line. We will also have our focus on programming logic.

So this:

.. code:: python
   :linenos:

   def donuts(count):
    output = 'Number of donuts: '
    if count >= 10:
        output += 'many' 
    else:
        output += str(count)
    return output

Becomes:

.. code:: python
   :linenos:

   def donuts(count): 
    return f'Number of donuts: {count if count < 10 else 'many'}' 

.. raw:: html
   
   <hr>

And this:

.. code:: python
   :linenos:

   def create():
    l = []
    for i in range(10):
      l.append(i)
    return l

Becomes:

.. code:: python
   :linenos:

   def create():
    return [i for i in range(10)]

The tendencies for python programmers to write code in this short and concise way has severel benifits:

* It condenses complex logic into a single line, making the code more readable and elegant.
* These compact expressions can often perform tasks more quickly, reducing the execution time.
* With less code, there's less to debug and maintain, simplifying updates and revisions.
* For those familiar with Python, one-liners can be more straightforward than multi-line code.
* They are perfect for small scripts and on-the-fly coding, providing fast solutions.

.. tip::
        Preperation
                Before we meet in class you should have watched this video about sorting:

                * `Python google class on sorting <https://youtu.be/EPYupizJYQI?si=P99QZxtQ_CVHA7H3&t=840>`_ (20 min)       
                * `List comprehensions 101 <https://mathspp.com/blog/pydonts/list-comprehensions-101>`_ (30 min)
                * `When to Use a List Comprehension in Python <https://realpython.com/list-comprehension-python/>`_ (30m - 1h)
        
        Time in class
                * `Teachers notes <notebooks/one_liners.ipynb>`_
        Homework
                * Finnish the exercises

Learning goals
--------------
After this week you will be able to work with:

* logic in programming situations
* list comprehensions
* ternary operators
* lambda expressions
* Chainined Comparison Operators 
* Sorting of a iterble including custorm sorting 



Materials
---------
* `List comprehensions 101 <https://mathspp.com/blog/pydonts/list-comprehensions-101>`_
* `When to Use a List Comprehension in Python <https://realpython.com/list-comprehension-python/>`_
* `Listcomprehensions for map, filter, reduce <notebooks/listcomprehensions_map_filter.rst>`_
* `Python google class on sorting <https://youtu.be/EPYupizJYQI?si=P99QZxtQ_CVHA7H3&t=840>`_ 
* `sorted() build-in function <https://docs.python.org/3/library/functions.html#sorted>`_
* `Teachers notes <notebooks/one_liners.ipynb>`_

Intro: Watson Test
------------------

| Wason-test (Peter Cathcart Wason, 1966).
| Consider 4 cards, where you can only see one side. 
| On each card there is a number on one side and a letter on the other.
| Suppose you see the following 4 cards:

.. image:: _static/card_chal.png

| Which cards do you need to turn over to determine if the following rule is correct?
| If there is a vowel on one side, then there is an even number on the other side.

You get 5 minutes to thinks this through, and then we make some statistics at the black board, about your solutions.
Afterwards you have to create a script that takes 4 cards as input and checks in the shortest/fastests way if is 'valid' cards or not.

Exercises
---------

--------------------------------
Ex: Alphabet List Comprehensions
--------------------------------
`Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-1-alphabet-list-comprehensions>`_

1. Create a list of capital letters in the english alphabet
2. Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
3. Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

.. raw:: html
   
   <hr>
------------------------------
Ex: Clothes List Comprehension
------------------------------

`Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-2-clothes-list-comprehension>`_

1. From 2 lists, using a list comprehension, create a list containing:


        [('Black', 's'),
        ('Black', 'm'),
        ('Black', 'l'),
        ('Black', 'xl'),
        ('White', 's'),
        ('White', 'm'),
        ('White', 'l'),
        ('White', 'xl')]


.. code::
   :linenos:

        colors = ['Black', 'White']
        sizes = ['s', 'm', 'l', 'xl']

2. If the tuple pair is in the following list, it should not be added to the comprehension generated list. 

.. code::
   :linenos:

        soled_out = [('Black', 'm'), ('White', 's')]

.. raw:: html
   
   <hr>
  
--------------------------------
Ex: list Comprehension exercises
--------------------------------

1. Create a list of even numbers from 0 to 20.
2. Create a list of squares of numbers from 1 to 10.
3. Create a list of all the vowels in a given string.
4. Create a list of common elements in two given lists. (could this be done with the use of another datastructure?) 
5. Create a list of words from a given string that have more than 4 and less than 8 letters.

.. raw:: html
   
   <hr>

------------------
Ex: Flatten a list
------------------
Flatten this list (using a list comprehension):

.. code::

        list_of_lists = [
            [1, 2, 3],
            [4, 5],
            [6],
            [7, 8, 9],
        ]

So it becomes like this:

.. code::

        [1, 2, 3, 4, 5, 6, 7, 8, 9]


.. raw:: html
   
   <hr>

---------------
Ex: Sort a Text
---------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Create a function that takes a string as a parameter and returns a list.
2. The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.


.. raw:: html
   
   <hr>

---------------
Ex: Sort a list
---------------
`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Create a list of strings with names in it. (l = ['Claus', 'Ib', 'Per'])
2. Sort this list by using the sorted() build in function.
3. Sort the list in reversed order. 
4. Sort the list on the lenght of the name.
5. Sort the list based on the last letter in the name.
6. Sort the list in a way that the names that has an 'a' in it should be sorted first (still alphabetically).

.. raw:: html
   
   <hr>
---------------------------------
Ex: Text editor plugin simulation 
---------------------------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

.. code::

   s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

1. Count the number of characters **including** blank spaces.
2. Count the number of characters **excluding** blank spaces. 
3. Count the number of words.

.. raw:: html
   
   <hr>

-------------------------
Ex: Sort a list of tuples
-------------------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Based on this list of tuples:     
:code:`[(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]`    

2. Sort the list so the result looks like this:  
:code:`[(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]`   

.. note:: 
        
        | This is first sorted by the last element in the tuple and then the first element in the tuple.
        | You should do this in 1 step, but it might help you to try it out in 2 steps first. 

.. raw:: html
   
   <hr>

-------------------
Ex: Logic if / else
-------------------

You are creating a simple grade evaluation system for a class. The system should take an integer input, which represents a student's score, and then return a grade according to the following criteria:

* If the score is 90 or higher, the grade should be "A".
* If the score is between 80 and 89 (inclusive), the grade should be "B".
* If the score is between 70 and 79 (inclusive), the grade should be "C".
* If the score is between 60 and 69 (inclusive), the grade should be "D".
* If the score is below 60, the grade should be "F".
* Additionally, if the score is outside the range of 0 to 100, the system should return "Invalid score".

Your task is to write a Python function that takes a score as an input and returns the corresponding grade.
You are welcome to write this in a straight forward if/else approch, but you should also write it in a one-liner using a ternary operator.

Solution: When you are done, copy/paste this exercise description + your solution into ChatGpt, asking it for feed back on how you solved the problem and where you could improve your solution. 

.. raw:: html
   
   <hr>
------------------
Ex: And / or logic
------------------

You are programming a room reservation system for a hotel. The system should check if a room can be reserved based on the following criteria:

* The room can be reserved if it is not already booked and the number of guests does not exceed the room's capacity.
* There are two types of rooms: standard and deluxe.
* A standard room can accommodate up to 2 guests, while a deluxe room can accommodate up to 4 guests.
* The reservation request will provide the room type (either "standard" or "deluxe") and the number of guests.
* The system should return True if the reservation can be made and False otherwise.

Your task is to write a Python function that takes the room number and the number of guests as inputs and returns whether the reservation can be made.

You should have some kind of datastructure for storing if the room is awaliable or not.

Again, you should write this in a straight forward approach, and in a python one-liner aaproach.

Solution: When you are done, copy/paste this exercise description + your solution into ChatGpt, asking it for feed back on how you solved the problem and where you could improve your solution. 

.. raw:: html
   
   <hr>
------------------------------
Ex: list and strings exercises
------------------------------

Based on the exercises from earlier this semester, solve the problems, but do it with one-liners instead of the solution we did earlier.
So all functions (if possible) should have a: return f'xxx' where all code is in this one line.

* `Exercise 1: Strings1 & Strings2 <exercises/strings/strings.rst>`_ 
* `List & tuple exercises <exercises/lists/lists.rst>`_
