Session 11 - Context Managers 
=============================

Today we will work with **Context Managers**. 

Context managers can in short be described as something that takes care of the related tasks of a specific task. An example of this could be when opening a file, the context manager takes care of automaticly closing the file when we are finished using it. 

You will make your own context managers and use already created ones. 

.. tip::
        Preperation

        Time in class

        Homework

Learning goals
--------------

        - Being able to use a Context Manager
        - Creating your own Context Managers
        - Using a context manager in relation to Working with JSON, Pickles and CSV files.
        - Using a context manager in relation to working with a SQlite database.

Materials
---------

* `What Does It Take To Be An Expert At Python? <https://www.youtube.com/watch?v=7lmCu8wz8ro&t=4962s>`_ *(good and advanced recap of what we covered in the teachings. Skip the Meta Classes part in the start of the video)*
* `Context Managers notebook <notebooks/Context-managers.ipynb>`_
* `JSON notebook <notebooks/JSON.ipynb>`_
* `Pickle notebook <notebooks/Pickle-Pythonobjectserialization.ipynb>`_
* `CSV notebook <notebooks/csv.ipynb>`_
* `Sqlite notebook <notebooks/Sqlite.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses11>`_

Exercises
---------
* `Solutions <exercises/solution/10_context_managers/solutions.ipynb>`_
**1. Coroutine to Compute a Running Average**
Change the function below into a coroutine (generator) that calculates a running avarage. So instead of returning an avarage based on the parameter it should calculate an avarage based on the values inserted into the coroutine with the .send() method.  

.. code:: python 
   :linenos:

   def averager(*args):
        sum = 0
        for i in args:
               sum += i
        return sum/len(args)
   
**2. Context manager class**
Create a class "Makeparagraph" that "decorates" a text with an html \<p\> tag.


**3. contextlib**
In the code example below we can se that the connect() function is a context manager. It has an \_\_enter\_\_ and an \_\_exit\_\_ method, and therefore works together with the "with" keyword.     

.. code:: python
   :linenos:

        from sqlite3 import connect

        with connect('testfiles/school.db') as conn:
            cur = conn.cursor()
            cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
            cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
            cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
            cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')

            for i in cur.execute('SELECT * FROM students'):
                print(i)

            cur.execute('DROP TABLE students')

The "CREATE TABLE" and the "DROP TABLE" has also some \_\_enter\_\_ / \_\_exit\_\_ logic behind it.    
Put this logic into its own contextmanager and use it. This should be done by using the contextmanager decorator from the contextlib library.     

**4. Context mananager for timing execution**

* `Solutions <exercises/solution/10_context_managers/solutions.ipynb>`_

In the session 6 about decorators we made a decorator that could time the execution of a function.

.. code:: python
   :linenos:

        import time

        def timeit(func):
            def wrapper(*args, **kwargs):
                start = time.time()
                value = func(*args, **kwargs)
                end = time.time()
                return value
            return wrapper

        @timeit
        def gen_large_list():
            return [x for x in range(10000000)]

        gen_large_list() 

Now we want to make a context manager that can do the same. The context manager should be able to time the execution of a code block.


* `SQlite 10 minutes exer <notebooks/Sqlite.html#10-minutes-exercise>`_
* `ConvertCSVtoJSON <notebooks/ConvertCSVtoJSON.ipynb>`_ ( `Solution <exercises/solution/10_context_managers/SolutionConvertCSVtoJSON.ipynb>`_)
* `Decorator / Context Manager <notebooks/Assignment_Decorator_Context_Manager.ipynb>`_  (`Solution <exercises/solution/10_context_managers/Assignment_Decorator_Context_Manager.ipynb>`_) 

