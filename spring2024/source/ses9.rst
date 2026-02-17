Session 9 - The python datamodel
================================

Today we will look at the python datamodel. 

Python has a protocol orientated datamodel.

After this you will be able to implement code in own classes that allow you to use pythons built-in functions or top level syntax to interact with these object.

**Example:**

If you want to be able to use the build in function :code:`len()` on your object you should implement the :code:`__len__` method in your class.  

If you want to be able to use the :code:`==` operator on your object you should implement the :code:`__eq__` method in your class. 

If you want to be able to use the :code:`in` key word on your object you should implement the :code:`__contains__` method in your class. 

So in python you will always see som top level syntax or top level functions and some corosponding datamodel methods. In order for you to program in a pythonic way you will have to understand this connection. 

.. tip::
        Preperation
                Before we meet in class you should have watched:
                
                * `What Does It Take To Be An Expert At Python? <https://www.youtube.com/watch?v=cKPlPJyQrt4&t=0s>`_
                        * Todays topic is covered from the beginning to 20:50) 
                * `Python's Magic Methods: Leverage Their Power in Your Classes <https://realpython.com/python-magic-methods>`

        Time in class
                * `Notebook on Datamodel <notebooks/OOP_Encapsulation_Propeties.ipynb#Datamodel>`_
                * `The spelled-out intro to neural networks and backpropagation: building micrograd <https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ>`_ (from 19:00 he gives the example i demoed in class)
                * `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses9>`_

        Homework
                * You should finnish the `Exercises`_ 

Learning goals
--------------

    * Create your own classes, that behave like any other Python Object, and are able to interact with pythons build in functions or top level syntax. 
     
Materials
---------

* `What Does It Take To Be An Expert At Python? <https://www.youtube.com/watch?v=cKPlPJyQrt4&t=0s>`_
* `The Python Data Model <_static/The_Python_Data_Model.pdf>`_
* `Python's Magic Methods: Leverage Their Power in Your Classes <https://realpython.com/python-magic-methods>`_
* `A Guide to Python's Magic Methods <https://rszalski.github.io/magicmethods/>`_
* `Expert Python Tutorial #2 - Dunder/Magic Methods & The Python Data Model <https://www.youtube.com/watch?v=z11P9sojHuM>`_
* `Build in functions to Datamodel methods ralation table <notebooks/build_to_dunder.rst>`_
* `Notebook on Datamodel <notebooks/OOP_Encapsulation_Propeties.ipynb#Datamodel>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses9>`_
.. * `Notebook demo Value class in teachings <notebooks/oop_lecture_value_graphviz.ipynb>`_

Exercises
---------

------------------
Ex1: Deck of cards
------------------

`Solution <exercises/solution/06_datamodel/solutions.rst>`_

Continue with the deck example and implement the 

* :code:`__len__` method
* :code:`__add__` method
* :code:`__repr__` method
* :code:`__str__` method
* :code:`__setitem__` method
* :code:`__delitem__` method

We look at this together in a short while.

When you a done, take a look at the exercise below and ask your questions.

.. raw:: html
   
   <hr>

-----------------
Ex2: Number Class
-----------------

.. code:: python
   :linenos:

        class Number:
                def __init__(self, num, obj_name):
                        self.num = num
                        self.obj = obj_name
        a = Number(5, 'a')
        b = Number(-4, 'b')

Based on this class create a Number that behaves like an int class, but with the extra parameter of putting in a variable name. 
The class should at least be able to be added, substracted, multiplied and divided. 




.. raw:: html
   
   <hr>

* `Linked List <exercises/protocol_linked_list.rst>`_  
.. 
   * `Jelly Beans <exercises/JellyBeans.rst>`_ 
