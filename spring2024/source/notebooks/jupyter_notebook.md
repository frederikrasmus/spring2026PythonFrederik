# Getting started with Jupyter Notebook
Jupyter notebooks can be found in various versions, both online and as local installes. We will the rest of this semester use a [Jupyter Docker image](https://hub.docker.com/r/jupyter/datascience-notebook). 

## Starting the Jupyter Notebook Server
To start a Jupyter Notebook instance with the parent folder as root run: 

```
    $ docker run --name jupyter -p 8888:8888 -v ${PWD}:/home/jovyan/work  jupyter/base-notebook
 
```   
**Note: This image will not work on Macbooks with the M1 chip. Instead you can use an online version of the Jupyter Notebook. An option is: [CoLab](https://colab.research.google.com/notebooks/intro.ipynb)**

Copy and paste the url from your terminal window into your browser and start using Jupiter Notebook.

![](../_static/jupyter.png)   

## Stopping the Notebook
To stop Jupyter Notebook, close your browser window(s), and in terminal press "ctrl+c". 

