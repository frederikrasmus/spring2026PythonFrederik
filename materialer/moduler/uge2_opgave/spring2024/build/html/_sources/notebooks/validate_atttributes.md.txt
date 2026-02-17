
# 3 (7) Approaches to Validate Class Attributes in Python
Spot the error before it’s too late

![]()

This article is cut and paste of [7 Approaches to Validate Class Attributes in Python](https://towardsdatascience.com/6-approaches-to-validate-class-attributes-in-python-b51cffb8c4ea#8a8eu), with a few edits. I have substracted 3 of the 7 methods from this article, since it fits better the porpouse of this class.

Generally speaking, type checking and value checking are handled by Python in a flexible and implicit way. Python has introduced typing module since Python3 which provides runtime support for type hints. But for value checking, there is no unified way to validate values due to its many possibilities.    

One of the scenarios where we need value checking is when we initialize a class instance. We want to ensure valid input attributes in the first stage, for example, an email address should have the correct format xxx@xx.com, an age should not be negative, the surname should not exceed 20 characters, etc.     

In this article, I want to demonstrate 3 (7) out of many options to validate class attributes using either Python built-in modules.

## Option2: Use Python @property

The second option uses a built-in function: ````@property````. It works as a decorator that is added to an attribute. According to [Python documentation:](https://docs.python.org/3/library/functions.html#property)

> A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function.


At the first glance, it creates more code than the first option, but on the other hand, it relieves the responsibility of ````__init__````. Each attribute has 2 methods (except for id), one with ````@property````, the other one with setter. Whenever an attribute is retrieved like ````citizen.name````, the method with ````@property```` is called. When an attribute value is set during initialization or updating like ````citizen.name="xiaoxu"````, the method with setter is called.

```
import re

class Citizen:
    def __init__(self, id, name, email, age):
        self._id = id
        self.name = name
        self.email = email
        self.age = age

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, value):
            raise ValueError("It's not an email address.")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

xiaoxu = Citizen("id1", "xiaoxu gao", "xiaoxu.gao@ing.com", 27)
xiaoxu = Citizen("id1", "xiaoxu1234567890123456789", "highsmallxu@gmail.com", 27)
# ValueError: Name cannot exceed 20 characters.
xiaoxu = Citizen("id1", "xiaoxu gao", "highsmallxu@gmail.c", 27)
# ValueError: It's not an email address.
xiaoxu = Citizen("id1", "xiaoxu gao", "highsmallxu@gmail.com", -27)
# ValueError: Age cannot be negative.

```


