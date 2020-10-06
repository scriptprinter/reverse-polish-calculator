# Reverse polish calculator in Python
The implementation is the module `rpolish.py`, the main thing is the function `calculate()`, that
takes a reverse polish expression (using spaces to separate the tokens) and returns the top item
of the stack or the entire stack.

# Usage

Just import the file "rpolish.py"

## Examples

```python
>>> import rpolish
>>> rpolish.calculate("5 5 + 5 5 + *") # (5 + 5) * (5 + 5)
100.0
>>> rpolish.calculate("3 2 + 12 4 * +") # (3 + 2) * 12 / 4
15.0
>>> rpolish.calculate("1.5 1.5 +") # Support for floating point values
3.0
>>> rpolish.calculate("1 2 + 3 4 + 5 6 +", return_stack=True) # Returns the stack
[3.0, 7.0, 11.0]
```

The extra function `create_tokens()` get a reverse polish expression and return a list of tokens.
(the function `calculate()` uses this to iterate over the tokens)

```py
>>> rpolish.create_tokens("1 2 3 * * 5 +")
[1.0, 2.0, 3.0, '*', '*', 5.0, '+']
```

# Documentation

## calculate(expression, return_stack=False)

```
Calculates a reverse polish expression, using spaces to separate
tokens.

Operations supported:
    + Addition
    - Subtraction
    * Multiplication
    / Division
    % Modulo (remainder of division)

If return_stack is True, the stack is returned, otherwise the top item of
the stack is returned.
Invalid tokens is ignored.

Observation: This uses the create_tokens() function, every valid number in
the expression is converted to float.
```

## create_tokens(expression, /)

```
Convert a reverse polish expression in a list of tokens, using spaces
to separate tokens.

A token is converted to float if is a valid float, otherwise the token
is pushed to the list.
```

# Info

I'm not very new in Python, but very new in GitHub, and i dont know how this works in some things,
so you can say of any problem, i am reading the PEP-8 now.

# Changelog

## 05/10/2020

+ First implementation
