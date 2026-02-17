Session 8 - Pythonic OOP
========================
Today we are going to cover a lot of ground reagrding creating your own objects in python.. 

.. tip:: 
  
   **Preperation** (1,5 hours)

   Before this class you should have read and understood this text: `Python Classes: The Power of Object-Oriented Programming <https://realpython.com/python-classes/>`_ . These are partly basic OOP concepts and some more specific python OOP concepts. 

   In order to check if you got the sufficient understanding of the topics you should also do these exercises. 

   If you have chatGpt 4 you can use this prompt:

        .. toggle::

                Based on this article: https://realpython.com/python-classes/
                Give me 10 exercises one at a time where you give the exercises and i give the solution back.
                Then give me feedback on my solution with suggestions for potential improvements and a evaluation from 1-10.

   If you do not have Gpt4 you can do these exercises instead:

        .. toggle:: 

                1.   Define a Simple Class: Create a class named Animal. Add two instance attributes: name and species, and initialize them through the constructor (__init__ method).

                2. Method Creation: Add a method make_sound to the Animal class that prints a sound string passed to it.

                3. Class Attributes: Define a class attribute kingdom for the Animal class and set its value to "Animalia".

                4. Inheritance: Create a Dog class that inherits from Animal and overrides the make_sound method to print "Woof!".

                5. Abstract Classes: Define an abstract class called Shape with an abstract method area. Then, create a subclass called Circle implementing the area method.

                6. Instance Representation: Add a __str__ method to the Dog class that returns a string with the dog’s name and species.

                7. Encapsulation: Modify the Animal class to make the species attribute private and provide a getter method to access it.

                8. Static Methods: Add a static method to the Animal class that takes a temperature in Fahrenheit and returns it converted to Celsius.

                9. Property Decorators: Use a property decorator in the Animal class to create a getter and setter for a new attribute called age that must be a non-negative integer.

                10. Composition: Create a Person class that has an Animal as a pet attribute, and add a method to the Person class that delegates the call to the pet’s make_sound method.

   **Time in class**
   
        * `Notebook on classes <notebooks/class_notes.ipynb>`_
        * `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses8>`_
   **Homework**

Learning goals
--------------
After having worked with these topics you will be able to:
      
   - create Classes, Objects, instance and class variables, methods and initializer methods.   
   - explain when and why to use classes and objects instead of procedural style.  

Materials
---------
* `Python Classes: The Power of Object-Oriented Programming <https://realpython.com/python-classes/>`_
* `Notebook on classes <notebooks/class_notes.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses8>`_


Exercises
---------


.. raw:: html
   
   <hr>


-------------------
EX 1: Bank Exercise 
-------------------

`Solution <exercises/solution/04_oop/solution.rst>`_

Create a Bank, an Account, and a Customer class.

* All classes should be in a single file. 
* The bank class should be able to hold many accounts.
* You should be able to add new accounts.
* The Account class should have relevant details.
* The Customer class Should also have relevant details.

Remeber to make your code "pythonic" it should be simple, easy to read, to the point, and no unnessesary code.
Stick to the techniques we have covered so far.

* Add the abillity for your __init__ method to handle different inputs (parameters).


.. raw:: html
   
   <hr>

-------------------------------
Ex 1a: Python skills Evaluation
-------------------------------

Copy/paste this in "your" ChatGpt prompt.
The recursing evaluation will work best with GPT4 (the paid version) but it is also ok i with gpt3 (used by the free version)


.. code::

        I want to get a score of how well my python programming with the focus on pythonic OOP is. The score should be from 1 to 10.
 
        You should give me exercises one at a time. The exercise need to be solved with code. The exercises should match the level you think i am at.
 
        You will provide the exercise and i will give you code. For each exercise write what level you think i am at
 
        When you are confident of my level generate a report. The report should contain the following
        1. The level you think i am at
        2. Feedback on the code i wrote
        3. Where i should focus to improve
 
        Lets start with the first question 

.. note::
   Remember your skills in Pythonic OOP might not be like an "expert" yet. But in a few weeks you can try it again and should get a better result.


---------------------------
EX 2: Sorting the Customers
---------------------------

Use the code created in ex 1 above.  

* Sort the accounts in the bank based on Customer names
* Sort based on amount of money the Customer has on the account 
* Sort based on Customer and then on the amount. (hint: return a tuple)

.. raw:: html
   
   <hr>

----------------
Ex 2: Angry Bird
----------------

`Solution <exercises/solution/04_oop/solution.rst>`_

        In this exercises you are going to create a simple terminal version of this `Angry Bird online coding teaching tool for kids <https://studio.code.org/hoc/1>`_ .

.. image:: _static/angry_bird.png

You should make this as an OOP application, and your classes could be like this. 

**Bird**

Should know its *current position*, and should know in what *direction* it is moving. It should be able to *move forward*, *turn left*, and *turn right*.
It should also have an action invoked when it looses the game, and one when it wins. 


**Pig**

Should know its *position*. 
It should also have an action invoked when it looses the game, and one when it wins. 

**Board**

Should initialize a Bird and a Pig object. It should *display* the board with the bird and the pig in starting positions. It should have a *run method*

.. code::

        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  B  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  P  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *


**Workspace**

Should have a display method printing out instructions on what to do. It should have a method being responsible of creating a collection of commands from user input. 


**Game**

This class is responsible of running the application. It should create objects of Board and Workspace and call their display methods. It should also be responsible for deciding if the bird hit the pig or not. 

**********
Screencast
**********

You can see a prototype of this exercise here. You are of cause welcome to improve the game, but this could be a solution. 

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/n9Ths1CSCkU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

