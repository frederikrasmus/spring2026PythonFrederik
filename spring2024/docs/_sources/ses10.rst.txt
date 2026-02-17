Session 10 - Properties
=======================
So far, in the OO world we've explored the fundamentals of Python classes, including 

1. instance variables, 
2. class variables, and 
3. methods. 
   
We have also looked at pythons datamodel and its 

4. Special methods. 
   
These components form the backbone of object-oriented programming in Python. 

Today, we're going to work with a new, yet closely related concept: 

5. property.

Properties in Python are a unique feature that blend the simplicity of accessing instance variables with the power and flexibility of methods. Think of them as a hybrid, offering the best of both worlds. They allow us to define methods that get, set, and delete values, just like instance variables, but with the added benefit of method-like behavior. This includes encapsulation, computation, and validation, all while interacting with them as if they were simple attributes.

One key aspect of properties is their role in maintaining a public interface. When we introduce properties to our classes, the way we interact with class attributes from the outside world doesn't have to change. This is crucial for the stability and maintainability of our code. We can modify the internal workings of a property without altering how it's accessed or mutated from outside the class. This means we can add logic to our getter and setter methods, or even deprecate attributes, all while keeping the public interface consistent.

In today's session, we'll explore how to define and use properties, and why they are a valuable tool for creating clean, efficient, and robust Python code. Whether you're managing public variables, ensuring data integrity, or looking for a smarter way to handle class attributes, properties offer a sophisticated solution. 

.. tip::

        **Preperation:**
      
        Before we meet in class you should have understood what a **property** is. This you can do by reading the first 3 articles. The last article is about a python naming convention. 

        * `Python's property(): Add Managed Attributes to Your Classes <https://realpython.com/python-property/>`_ (30 minutes - 1 hour)
        * `Property (Wikipidea) <https://en.wikipedia.org/wiki/Property_(programming)>`_ (skim this through 5 minutes)
        * `property documentation <https://docs.python.org/3/library/functions.html#property>`_ (10 minutes)
        * `Single and Double Underscores in Python Names <https://realpython.com/preview/python-double-underscore/>`_ (30 minutes)

        **Time in class:**
        
        * `Notebook on properties <notebooks/OOP_Encapsulation_Propeties.rst>`_
        * `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses10>`_
        **Homework:**

Learning goals
--------------
After this week you will be able to:
        
- Understand what a property is
- Understand the pythonic approach to encapsulation. 
- Use public and non-public attributes in your code
- Understand what encapsulation is and how it is achieved in OOP.
- Explain the pros and cons of properties and public attributes compared to Java´s private attributes with getters and setters. 

Materials
---------
* `Python's property(): Add Managed Attributes to Your Classes <https://realpython.com/python-property/>`_
* `Single and Double Underscores in Python Names <https://realpython.com/preview/python-double-underscore/>`_
* `property documentation <https://docs.python.org/3/library/functions.html#property>`_
.. * `Difference between _, __ and __xx__ in Python <https://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html>`_
* `Notebook on properties <notebooks/OOP_Encapsulation_Propeties.rst>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses10>`_

Exercises
---------
All following exercises should be done by using **Properties** when needed.    
The focus should be on encapsulation. 

-----------------------------
Ex: Create an imutable object
-----------------------------
Properties can be used for different things. One of the is to create a class that is imutable (its state can not be  changed) when an object is created from it.

1. Make a card class that is imutable.


Ex: Number object (logic)
*************************

1. Create a Number class that takes a value as parameter when instanciated.
2. Change your code so that at instanciation the value could be any number, but if changed at a later point it should not be lower than the present value (e.g if the value is 5, then changing it to 4 or less would raise an exeption).
3. Change your code into that the value could not be changed after instanciation (imutable)
        a. 


Ex 1:  Car object
*****************

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

Create a Car class. 

When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph). 
All 4 should be properties. 

.. note::
    | Remember! In python you would never write empty properties, 
    | so there should be a reason for Make, Model, bhp, mph properties to exist!


Ex 2. Don´t break the public interface
**************************************

Imagine you have this library code:

.. code:: python
   :linenos:

   class Square:
        def __init__(self, height, width):
                self.height = height
                self.width = width

The the public interface (or the way to use this) would be:

.. code:: python

   >>> rectangle = Square(12,12)
   >>> rectangle.height
   12
   >>> rectangle.width
   12

**Task**
Now make sure that you can not create an object like this:

.. code:: python

   >>> rectangle = Square(-12,12)


Ex 2: Bank
**********

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.  

.. code:: python
   :linenos:

   class Bank:    
        def __init__(self):
           self.accounts = []

   class Account:
        def __init__(self, no, cust):
           self.no = no
           self.cust = cust

   class Customer:
        def __init__(self, name):
           self.name = name


* The bank class should futher be change into not taking any accounts as parameters at initialization. 
* The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).      
* Somewhere you should change the code so that a customer only can create one account.     
* The Customer class should make sure that the customer is over 18 year of age.


Ex 2a: Debugging
****************

In the code below there is one mistake. What is wrong with this code?

.. code:: python
   :linenos:

        class C:
            def __init__(self, value):
                self._x = value

            @property
            def x(self):
                return self._x

            @x.setter
            def x(self, value):
                if value <= 100 and value >= 0:
                    self._x = value
                else:
                    raise ValueError('value should be between 0 and 100')






Ex 3: Machine -> printer
************************

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

* Create a Machine class that takes care of powering on and off a the machine.   
* Create a printer class that is a subclass of the Machine super class.   
* The printer should be able to print to console.  
* The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and load new paper in the tray if empty.  

Ex 4: Rectangle
***************

Write a Python class called Rectangle with width and height attributes. Add a get_area method which calculates the area of the rectangle. Then add property decorators to the width and height attributes, so that they can be accessed and set like regular public attributes, but also validate that the input values are positive. If a non-positive value is assigned to either width or height, raise a ValueError with an appropriate error message.

Your code should include:

* A class called Rectangle
* width and height attributes with property decorators
* An area property that calculates the area of the rectangle
* Appropriate error handling for non-positive width and height values


Ex 5: Color converter
**********************

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

Try creating a property :code:`hex` for the :code:`class` Color that is shown below. The property :code:`hex` should return a string that starts with # and that contains the hexadecimal value of the color.

.. code:: python
   :linenos:

   class Color:
       def __init__(self, r, g, b):
               self.r = r
               self.g = g
               self.b = b

If you get it right, you should be able to use the class Colour like so:

.. code:: python

   >>> c = Color(146, 255, 0)
   >>> c.hex
   '#92ff00'


