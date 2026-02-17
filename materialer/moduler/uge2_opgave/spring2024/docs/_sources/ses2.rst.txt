Session 2 - Data Structures: List, Tuple, Set & Dict
====================================================

Today we will work with data structures in python. You will by the end of these sessions be able to use List, Tuple, Set and Dictionary and you will have a basic understanding of the differense and the difference in use of them all. 


.. tip::
        Preperation:
                Before we meet in class you should have:

                * Skimmed the article: `Lists and Tuples in Python <https://realpython.com/python-lists-tuples/>`_ (15 min)
                * Skimmed the article: `Sets in Python <https://realpython.com/python-sets/>`_ (15 min)
                * Skimmed the article: `Dictionaries in Python <https://realpython.com/python-dicts/>`_ (15 min)

                In order to check if you have the right understading of todays topics, you should

                * Do this `Python Dictionaries Quiz <https://realpython.com/quizzes/python-dicts/>`_ (15 min)
                * Do this `Python Sets Quiz <https://realpython.com/quizzes/python-sets/>`_ (15 min)
                * Do this `Python Lists and Tuples Quiz <https://realpython.com/quizzes/python-lists-tuples/>`_ (15 min) 

        Time in class
                * `Notebook list/tuples (teachings notes from today) <notebooks/noterlists_tuples.ipynb>`_
                * `Notebook sets/dicts (teachings notes from today) <notebooks/notes_set_dicts.ipynb>`_
                * `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses2>`_

        Homework
                * You should finnish the `Exercises`_

Learning goals
--------------

After this week you will be able to:
        
        - Work with lists, tuples, sets and dictionaries. 
        - Sort sequences using the build in sorted function and use its key parameter to perform custom sorting.  
        - Read from files and write to files using the build in "open" function. 

Materials
---------

* `Lists and Tuples in Python <https://realpython.com/python-lists-tuples/>`_
* `Sets in Python <https://realpython.com/python-sets/>`_ 
* `Dictionaries in Python <https://realpython.com/python-dicts/>`_ 
* `How to Use sorted() and .sort() in Python <https://realpython.com/python-sort/>`_
* `Notebook list/tuples (teachings notes from today) <notebooks/noterlists_tuples.ipynb>`_
* `Notebook sets/dicts (teachings notes from today) <notebooks/notes_set_dicts.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses2>`_


Exercises
---------
---------------
Ex 0.1: Slicing
---------------


`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

By using the slicing syntax change the following collections.

After slicing:

.. code:: Python
        :linenos:

        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
        ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
        'Hello World Huston we are here' -> 'World Huston we'

Figure out more on your own and practice this a lot!    

.. raw:: html
   
   <hr>

--------------------------------
Ex 1.1: Is it a tuple or a list?
--------------------------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

| The following data should be presented as either a list or a tuple, or as a combination of both.    
| Your job is to choose the right one. 
| Hint: A list is a collection of the same type of data, a tuple is a record (e.g. in a database a **record** is called a **row**)

1. Claus, 51, male, clbo@kea.dk, 31011970-1313
2. Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo
3. Claus, Henning, Torben, Carl, Tine
4. 'Hello', 'World', 'Huston', 'we', 'are', 'here'
5. Rolling Stones, Goats Head Soup, 31 August 1973, 46:56
6. 40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;


.. raw:: html
   
   <hr>


---------------
Ex 6: Storebælt
---------------

We have been asked to build a system for Storebæltsbroen. They want to build a system that can keep track of all the cars that cross the bridge. They have built some software for recognising numberplates, car color, number of passengers and length. 

The information they want to save for a car is the following:

* Car color
* Number of passengers
* Car length

It is important for Storebæltsbroen that they can quickly find information about a particular car (using the numberplate).

What data structure should we choose and why? 

Write the code showing how you would save some data for a new car.

Continued
*********

Storebæltsbroen (the company) owns more bridges and they would like to know how many of the cars has been crossing all of the bridges. From each bridge they register the numberplate using the above mentioned system. The system should be fast. What data structure can help us achieve this and why? Please write some pseudo code of how you would get how many of the cars has crossed all the bridges

.. raw:: html
   
   <hr>

List & Tuples, Set, Dict exercises
----------------------------------
`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

* `List & tuple exercises <exercises/lists/lists.rst>`_
* `Set exercises <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/blob/master/ses2/exercises/sets.py>`_
* `Dict exercises <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/blob/master/ses2/exercises/dict.py>`_

------
quizes
------
* `Lists and Tuples Quiz <https://realpython.com/quizzes/python-lists-tuples/>`_
* `"while" Loops Quiz <https://realpython.com/quizzes/python-while-loop/>`_
