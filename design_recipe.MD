# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_for_todo(string):

    """

    Parameters:  takes inputted tect as string 
    
    returns a True or False statement as a Bollean

    Side effects: prints True or False with text 
    
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# It will take the inputted string and return True if it contains #TODO or False if it does not

"""

"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE
def test_check_for_todo():
    result = check_for_todo('This contains #TODO')
    assert result is True

def test_check_for_todo_no_todo():
    result = check_for_todo('Not here') #don't put #TODO in test otherwise it will fail
    assert result is False

from lib.check_for_todo import *

"""


```

Ensure all test function names are unique, otherwise pytest will ignore them!
