# Software needed this semester 
There are several IDE´s or editors you can use when programming in python. 

In this elective your are free to choose whichever you like, but the best and easiest choise is to use Github codespaces. You can custormize this in several ways, but as default you will have a browser version of VSCode. 

## Github Codepsaces
In order for this to work, you will need to have access to [github codespaces](https://github.com/codespaces).    
If you do not allready have that you can get it through [GitHub Student Developer Pack](https://education.github.com/pack#offers) 

### Working with the "Introduction to python" github repository
* Browse to [Introduction to python github repository](https://github.com/python-elective-kea/spring2024-code-examples-from-teachings)
* Click on the green "<> Code" button and then click on "Create codespace on master"

![](../_static/codespace.png)

This will open a codespace like this:

![](../_static/codespace2.png)

This will be your editor in this elective.    


### Important: Working on branches
* You should before doing anything else always create a new branch. (I exspect that you know how to do that).    
* The master branch is where all updates to the course material during the semester will happen.
If you work directly on the master branch, you will have your files overwritten before every session starts (or at least have a lot of merge conflicts you have to solve).    

**So important!! Keep the master branch clean!** 
* Never edit the files directly on the master!
* Always create a new branch when you want to do something to the files. 

### Pull before every session
* Before every session (every class) you should swich to the master branch and pull in the changes.
* Then create a new branch (e.g ses2, ses3) and code along or do the exercises.

### Save your work
* You should remember to commit and push the changes you make in your branches.
* This will make a "Fork" on your own account. 


<!--
## Install python
Go to [www.python.org](https://www.python.org) and find the download button, and install python.   

**On Mac** its recomended to install python (and other software) through brew. 

```
   $ brew install python
```
When done open you Terminal (mac) and Gitbash (win) and type

```
	$ python3 --version
	Python 3.11.4
``` 
you should see something like this. 
If not, python is not installed, or maybe something else went wrong (ask Claus). 

## Install VS Code
Go to [code.visualstudio.com](https://code.visualstudio.com/) and find the download button for your operating system. Download and install VS Code. 

**Mac**

```
   $ brew install --cask visual-studio-code
```

### Working with Code and Exercises for the Semester:

* Always pull the master branch for new files added to the repository.
* Create a new branch for:
   * Playing with files.
   * Completing exercises.
* Never merge your branches into the master branch.

#### Important Note:

* Do not edit files directly in the master branch.
* Keep the master branch clean to avoid merge errors.



---

## Setup the development environment for the Data Analasis and Visualization part of this elective
(Note: you will do this later this semester)

### Add the python and jupyter extension in VS Code
1. Open VS Code.
1. Click on the "Extensions" icon in the left sidebar.
1. Search for "python" and install the Python extension from Microsoft.
1. Search for "jupyter" and install the Jupyter extension pack (4) from Microsoft.

### Setting Up the Class Repository in VS Code:

#### 1. Clone the Repository:

* Open VS Code.
* Click the “Source Control” icon on the left (square with a branch).
* Click “Clone Repository”.
* Enter the URL: https://github.com/python-elective-kea/fall2023-code-examples-from-teachings.git
* Choose a local folder to clone to and click “Clone”.

#### 2 .Navigate to the Cloned Repository:

* Click the “Explorer” icon on the left.
* Go to the cloned folder (e.g., fall2023-code-examples-from-teachings).

#### 3. Set Up Git:

* If the Git status bar isn't visible at the bottom-left, click the “Source Control” icon.
* Click the displayed branch name (e.g., “main” or “master”).
* Type “playground” to create a new branch or click “+” and name it “playground”.
* The status bar should now show “playground” as the active branch.

#### 4. Open the File:

* Locate playground.ipynb in the “Explorer” panel.
* Double-click to open it.

#### 5. Set Up Python Environment:

* On the top right corner.
* Select Kernel.
* Choose Python environments.
* Click on Create Python Environment.
* Opt for Venv Create a '.venv' in the current workspace.
* Select your Python version (e.g., 3.11.3).
* This process establishes a ‘.venv’ virtual environment for the playground.ipynb file.

#### 6. Note: 
* Always choose the .venv environment when running code in this repository in the future.

-->

