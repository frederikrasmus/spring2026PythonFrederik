Solutions for os, subprocess, requests exercises
================================================

Ex 3: Create and run a ‘Hello world’ C application
--------------------------------------------------

In your folder you should have this:

.. code::

   .
   ├── hello
   └── main.c

The main.c has the code snippet inside. The hello is the compilede object.

The docker command you should run looks like this:

.. code::

   $ docker run -it --rm -v ${PWD}:/docs gcc bash


And the commands to compile and run the c code lookes like this. 

.. code::

   # gcc -o hello main.c
   # ./hello   

Ex 4: Ex 5: Build a Web Scraper With Python 
-------------------------------------------

`Build a Web Scraper With Requests and Beautiful Soup <https://github.com/realpython/materials/tree/master/web-scraping-bs4>`_


Ex 6: Simple scraber with requests (and BS)
-------------------------------------------
.. literalinclude:: 
   :language: python
   :linenos:


Ex 7: From Html to Markdown
----------------------------
.. literalinclude:: ex7.py
   :language: python
   :linenos:
