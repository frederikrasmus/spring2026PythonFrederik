Session 4 -  Mandatory 1: Files, Modules & LLM 
==============================================

.. note::
   
   `Fill out this questionary and hand it in latest friday the 23rd of February 16.00. <https://kea-fronter.itslearning.com/LearningToolElement/ViewLearningToolElement.aspx?LearningToolElementId=1214815>`_

Todays reading materials, exercises and hand-in is your first **mandatory assignment**. You should study the topics on your own, or in groups if you prefere. In the end you should fill out a questionary which should be handed in on Fronter. The hand-in is the formal submission of the mandatory, and will be evaluated as "passed" or "non-passed". 

The topics today will be about modules in Python. You will create your own modules, learn how to use Python's built-in modules and work with 3rd party modules.
You will also work with files in different formats like text, json and sqllite files.
As a last thing you will work with a LLM (Large Language Model, like the model behinde ChatGpt) installed on you own computer through a docker image.

Learning goals
--------------
After this week you will be able to:
       
        - Working with files (txt, json, sql)
        - Use Python's built-in modules. (OS, Subprocesses)
        - Find and use 3rd party modules. (requests, langchain ...)
        - Interact with LLM using python
        - Have worked in a docker container locally on your computer. 


The Assignment
--------------

Follow this list of combined reading materials and exercises:

---------------------------------
1. Reading and writing from files
---------------------------------
        
* `Working with files in Python <notebooks/files.ipynb>`_ 

*******************
Ex: Files in Python
*******************
1. Create a file called numbers.dat
2. Write the numbers from 1-100 to the file.
3. open the file for reading, and print all even numbers to the screen.

.. raw:: html
   
   <hr>

-----------------------
2. Modules and packages
-----------------------

* `Python import: Advanced Techniques and Tips <https://realpython.com/python-import/>`_ (only the 'Basic Python import' section for now)
* `Python´s OS Module <notebooks/os_module.md>`_

**********************
Ex: OS Module exercise
**********************

.. literalinclude:: exercises/util_modules/os_exercise.py
        :linenos:

.. raw:: html
   
   <hr>


* `sqlite3 — DB-API 2.0 interface for SQLite databases <https://docs.python.org/3/library/sqlite3.html>`_

********************
Ex: Sqlite in Python
********************
1. Create a Database called Zoo, with an Animal Table.
2. Insert 3 animals
3. Read from the database and print the animals to the screen.

.. raw:: html
   
   <hr>

* `The subprocess Module: Wrapping Programs With Python <https://realpython.com/python-subprocess/>`_

**************
Ex: subprocess
**************

1. Clone this respository :code:`https://github.com/python-elective-kea/spring2024.git`
2. open the index.html file from the docs folder in your browser.

.. raw:: html
   
   <hr>

* `Python’s Requests Library <https://realpython.com/python-requests/>`_
* `HTTP Requests With the "requests" Library Quiz <https://realpython.com/quizzes/python-requests/>`_

.. raw:: html
   
   <hr>
   
* `Working With JSON Data in Python <https://realpython.com/python-json/>`_

******************
Ex: JSON in Python
******************
1. From this api https://api.github.com/orgs/python-elective-kea/repos get all clone_urls of the repos and write them to an appropiate datastructure.
2. Create a folder inside the one you are currently in.
3. Clone all repos into this folder.  

.. raw:: html
   
   <hr>

*******************
Ex: Ollama tutorial
*******************

* `Installing Ollama <notebooks/installing_ollama.md>`_ 
* `Using LangChain with Ollama in Python <https://github.com/jmorganca/ollama/blob/main/docs/tutorials/langchainpy.md>`_

.. tip:: This you will have to do on your local computer, not in github codespaces.

In order to make this work you should have installed Docker desktop, the ollama docker image, python and an editor on your local computer  which you can read about howto in this document: `Installing Ollama <notebooks/installing_ollama.md>`_  


.. raw:: html
   
   <hr>

***************************
Ex: Play a game against LLM
***************************
Create a simple two player game of your own choise.
An example could be tic, tac, toe, or it could be chess.

.. code::

   __________
   |  |  |  |
   ----------
   |  |  |  |
   ----------
   |  |  |  |
   ----------

The game should be played against a LLM, running on your own computer (Ollama) (or if you like OpenAi´s api or other online LLM apis).
If you use the Ollama api you have most of the steps and concepts covered in the tutorial you just did. If you want to use OpenAi, you should look at the documentation online. 

.. raw:: html
   
   <hr>

Hand-in your mandatory assignment
---------------------------------


.. note::
   
   `Fill out this questionary and hand it in latest friday the 23rd of February 16.00. <https://kea-fronter.itslearning.com/LearningToolElement/ViewLearningToolElement.aspx?LearningToolElementId=1214815>`_



Materials (collection of the above materials)
---------------------------------------------
* `Working with files in Python <notebooks/files.ipynb>`_ 
* `Python import: Advanced Techniques and Tips <https://realpython.com/python-import/>`_
* `Python´s OS Mudule <notebooks/os_module.md>`_
* `The subprocess Module: Wrapping Programs With Python <https://realpython.com/python-subprocess/>`_
* `Python’s Requests Library <https://realpython.com/python-requests/>`_
* `Installing Ollama <notebooks/installing_ollama.md>`_ 
* `Working with SqlLite <notebooks/Sqlite.ipynb>`_ 
* `Working with JSON <notebooks/JSON.ipynb>`_ 
* `Langchain and Ollama <notebooks/langchain_ollama.md>`_
* `Notebook <notebooks/Notes-Contextmanager-ListComp-modules.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2024-code-examples-from-teachings/tree/master/ses3>`_

