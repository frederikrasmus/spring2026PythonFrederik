Session 6 - Functions &  Decorators  
===================================
So far in this elective we have focused on using other peoples python code. It could be parts of the language itself, as its data structures or build in modules like `os`. It has also been 3rd party modules like `requests` or `langchain`.

Commend to all of this is that all the objects (code) has a sertain flavour to it, it has a cretain style. 

In the 2. part of this elective, starting today, we will fokus on creating our own objects that behave the same way as all other objects. Our code should have the same flavour, the same style, as all other (good) python code out there. 

We will start out by looking at one technique used for adding aditional functionallity to already existing code, **the decorator**.

Then we will look at creating classes and objects, and we will especially look at the rules that make a python object behave **pythonic**.

This will involve dealing with basic OOP concepts, looking at the python datamodel, and dealing with properties. We will in the end also look at python generators and how they can be used to creating subroutines. All aspects that can make your own python code behave like all other python code out there.

But now we go on with todays topic, decorators.

In Python, decorators allow you to add new functionality to your code, or other peoples code, by decorating functions (or classes) with additional code. This can make your code more modular and easier to maintain, as you can separate different concerns into separate decorators.

The boilerplate syntax of a decorator is like this:

.. code:: python 
   :linenos:

   def decorator(func):
       def wrapper(*args, **kwargs):
               # Do something before
               value = func(*args, **kwargs) 
               # Do something after
               return value
       
       return wrapper

And if you want to use it you will do like so:

.. code:: python
   :linenos:

   @decorator
   def add(a,b):
        return a + b


.. tip::
        Preperation:
                Before we meet in class you should have:
                
                * You should be on top with functions i python. 
                  You can du that by either reading this article `Defining your own python functions <https://realpython.com/defining-your-own-python-function/>`_ , or by using this prompt in chatgpt (1 hour):


        .. toggle::  

                .. code::

                        I want to get a score of how well my python programming is with the focus on basic function elements like defining, calling, return value and return type, parameters. The score should be from 1 to 10.

                        You should give me exercises one at a time. The exercise need to be solved with code. The exercises should match the level you think i am at.

                        You will provide the exercise and i will give you code. For each exercise write what level you think i am at

                        When you are confident of my level generate a report. The report should contain the following
                        1. The level you think i am at
                        2. Feedback on the code i wrote
                        3. Where i should focus to improve

                        Lets start with the first question


        * You should then skim these tree articles (15 minutes)
                * `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/>`_
                * `Python Inner Functions—What Are They Good For? <https://realpython.com/inner-functions-what-are-they-good-for/>`_
                * `Python args and kwargs: Demystified <https://realpython.com/python-kwargs-and-args/>`_
        
        Time in class
                * `Notebook on Decorators <notebooks/Decorators.ipynb>`_
                * `What Does It Take To Be An Expert At Python? <https://youtu.be/cKPlPJyQrt4?si=RgFuHWHpIqzUlMtE&t=2841>`_ (this video covers some of the topics shown in class today. From 47:20 to 1:06:31)
        Homework
                * Finnish all exercises



Learning goals
--------------
By reading the texts in the materials section, doing the 3 exercises, and follow the teachings, you will be able to explain what a decorator is, when to use it, and how the inner parts of a decorator function is made up, and you will be able to create your own, and use others already made decorators. 

After this week you will know about and be able to use and explain:

        - First class functions 
        - Inner functions
        - Decorator functions
                - explain how a decorator function works
                - understand what the return values and return types are of the different functions used in a decorator
                - understand why we reuse the variable names in the scope.


Materials
---------
* `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/>`_
* `Python Inner Functions—What Are They Good For? <https://realpython.com/inner-functions-what-are-they-good-for/>`_
* `Python args and kwargs: Demystified <https://realpython.com/python-kwargs-and-args/>`_
* `Defining your own python functions <https://realpython.com/defining-your-own-python-function/>`_ 
* `What Does It Take To Be An Expert At Python? <https://youtu.be/cKPlPJyQrt4?si=RgFuHWHpIqzUlMtE&t=2841>`_
* `Notebook on Decorators <notebooks/Decorators.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses6>`_

Exercises
---------

---------------------------
Warm up functions exercises
---------------------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

Think about the each of the following functions and determain what are the:

* return value
* return type
* parameter type
* parameter value

**example1**

.. code:: python
   :linenos:

   def add(num1, num2):
        return num1 + num2


**example2**

.. code:: python
   :linenos:

   def add():
        print('Hello')

**example3** 

.. code:: python
   :linenos:

   def add():
        pass


**example4**

.. code:: python
   :linenos:

   def add(*args):
        return sum(args)


**example5**

.. code:: python
   :linenos:

   def msg(x, y):
        return x(y)
        
   # what does this one return, what are the parameters??
   msg(len, 'Hello')


.. raw:: html
   
   <hr>


------------------
Ex: decorating add
------------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

With this function as a starting point

.. code:: python
   :linenos:

   def add(*args):
       return sum(args) 

1. Write a decorator that writes to a log file the time stamp of each time this function is called.
2. Change the log decorator to also printing the values of the argument together with the timestamp.
3. Print the result of the decorated function to the log file also.
4. Create a new function and call it printer(text) that takes a text as parameter and returns the text. Decorate it with your logfunction. Does it work?    

.. raw:: html
   
   <hr>

------------
Ex: Time it!
------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

If you want to messure how much time it takes to execute a piece of code you could do the followin:

.. code:: python
   :linenos:

   import time

   start = time.time()
   // do some stuff you want to meassure here
   end = time.time()
   print(end - start)

   
Instead of writing this every time you need to time something, you could write a docorator function that does the job for you. 

**Task:**

Your job is, to write a decorator function that can time any piece of code.

You can read about time by starting your interpretor and write:

.. code:: python

   > import time
   > help(time)

.. raw:: html
   
   <hr>

-------------------------------
Ex: Decorator skills evaluation
-------------------------------
Copy/paste this in "your" ChatGpt prompt.
The recursing evaluation will work best with GPT4 (the paid version) but it is also ok i with gpt3 (used by the free version)

.. code::

        I want to get a score of how well my python programming is with the focus on pythons decorator functions. The score should be from 1 to 10.
 
        You should give me exercises one at a time. The exercise need to be solved with code. The exercises should match the level you think i am at.
       
        Among other things, you should test me in both the `@decorator` annotation or the `func = decorator(func)` syntax.

        You will provide the exercise and i will give you code. For each exercise write what level you think i am at
 
        When you are confident of my level generate a report. The report should contain the following
        1. The level you think i am at
        2. Feedback on the code i wrote
        3. Where i should focus to improve
 
        Lets start with the first question 

.. raw:: html
   
   <hr>

------------------------------
Ex: Decorating Game Characters
------------------------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

**Background**
In the world of computer games, every character has a unique skill or ability that makes them special. For example, a character might have the ability to shoot accurately, move stealthily, or hack into computers.

We're going to use Python decorators to add unique skills or abilities to game characters.

**Task**
Create a Python decorator that adds a unique skill or ability to a game character. The decorator should be reusable, so that we can add multiple skills or abilities to a character.

**Example**
Here's an example of how the decorator might be used:

.. code:: python
   :linenos:
        
   @sharpshooter
   @stealthy
   def player():
       return "I'm the player character"

   print(player())

The output of the code should be:

.. code::

   I'm the player character, the sharpshooter and stealthy character.



**Steps**

1. Create a decorator function that takes a function as an argument and returns a new function that adds a unique skill or ability to the character's description.
2. Add the decorator to the player() function to add the "sharpshooter" and "stealthy" abilities to the player character.
3. Test your code to make sure it works as expected.

**Bonus**

1. Create additional decorators for other skills or abilities that might be found in a computer game.
2. Add multiple skills or abilities to a single character by stacking multiple decorators.

.. raw:: html
   
   <hr>
Ex: Menu register
-----------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

In this exercise you should create a register. 

When a new function is made you should by decorating it add it to a register (e.g a dictionary, or a list).

This functionality would be something that could be used in web application frameworks like Django or Flask. When ever a new function (a route or a page) is created and decorated this register could be used for a menu or things like this. 

Example:

.. code:: python
   :linenos:

   @register        
   def home():
        return 'I´m the home page'


You can get inspiration for this ecxercise in this document: `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/#registering-plugins>`_
