# printer.py (solution)

"""
    3. Machine -> printer
    Create a Machine class that takes care of powering on and off a the machine.   
    Create a printer class that is a subclass of the Machine super class.   
    The printer should be able to print to console.  
    The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.  
"""

class Machine:
    """ takes care of turning on and off  """

    def __init__(self):
        self._is_on = False  # one _ = protected (to be used only in subclasses) 
    
    def power(self):
        self._is_on = not self._is_on

class Printer(Machine):
    def __init__(self):
        Machine.__init__(self)
        self._pt = Papertray()

    def print(self, text):
        if self._pt.paper == 0:
            print('Papertray is empty')
        else:
            if self._is_on:
                print(text)
                self._pt.paper = self._pt.paper - 1
            else:
                print('Printer is off')

    @property
    def load(self):
        return self._pt.paper

    @load.setter
    def load(self, no):
        self._pt.paper = no

class Papertray:
    def __init__(self):
        self.paper = 2

    @property
    def paper(self):
        return self._paper

    @paper.setter
    def paper(self, paper):
        self._paper = paper









