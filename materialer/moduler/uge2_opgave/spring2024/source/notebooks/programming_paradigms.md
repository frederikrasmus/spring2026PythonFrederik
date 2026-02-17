# Programming Paradigms
There are a few ways we can make a taxonomy of programming languages:

* declarative vs. imperative
* structured vs. object oriented vs. protocol oriented vs. functional vs. function level (no variables!) vs. logic etc.

Some modern programming languages like Python, Ruby, and Swift is a mix of several of these paradigms. You will often see that pragmatic languages like Python take this approach, whereas more “puritan” languages like Java stick with one paradigm.

## Definition

A programming **paradigm** is a style, or “way,” of programming.

Some languages make it easy to write in some paradigms but not others.

## Some Common Paradigms

You should know these:

* Imperative: Programming with an explicit sequence of commands that update state.
* Declarative: Programming by specifying the result you want, not how to get it.
* Structured: Programming with clean, goto-free, nested control structures.
* Procedural: Imperative programming with procedure calls.
* Functional (Applicative): Programming with function calls that avoid any global state.
* Object-Oriented: Programming by defining objects that send messages to each other. Objects have their own internal (encapsulated) state and public interfaces. Object orientation can be:
    * Class-based: Objects get state and behavior based on membership in a class.
    * Prototype-based: Objects get behavior from a prototype object.
* Event-Driven: Programming with emitters and listeners of asynchronous actions.

## A Look At Some Major Paradigms


### Imperative 
```
x = 0
x = x + 5
x = x * 3
print(x)  
```
This code explicitly dictates the steps the program should follow, updating the state of x sequentially.

### Declarative (SQL example) 
```
SELECT name FROM students WHERE age > 20;
```
Here, we're specifying what we want (names of students older than 20) but not detailing how to obtain it.


### Structured: 
```
for i in range(3):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

The code uses structured control structures (for and if-else) without any jumps or goto statements.

### Procedural

```
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Outputs 8
```
We're breaking down the task into a procedure (add function) and calling that procedure to get our result.

### Functional (Applicative) 

```
def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(result)  # Outputs 15
```
This approach uses pure functions, without any external state, to derive the result.

### Object-Oriented 
### Class-based 

```
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} barks!"

dog = Dog("Buddy")
print(dog.bark())  
```
We define a class Dog that encapsulates state (name) and behavior (bark). Objects derive state and behavior from this class.

### Prototype-based (Javascript example) 

```
var dog = {
    bark: function() {
        return "Woof!";
    }
};

var bulldog = Object.create(dog);
bulldog.bark = function() {
    return "Loud Woof!";
};

console.log(bulldog.bark());  
```
In JavaScript, objects can inherit directly from other objects using Object.create(). The bulldog object inherits from the dog object (its prototype) and then overrides the bark method.

### Event-Driven 

```
import tkinter as tk

def on_button_click():
    label.config(text="Button was clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click me", command=on_button_click)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()
```
This code sets up an event-driven GUI where the program waits for events (like button clicks) to happen and then responds accordingly.
