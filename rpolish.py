# -*- coding: utf8 -*-

"""Simple implementation of a reverse polish calculator in Python."""

def create_tokens(expression, /):
    """Convert a reverse polish expression in a list of tokens, using spaces
    to separate tokens.
    
    A token is converted to float if is a valid float, otherwise the token
    is pushed to the list.
    """

    tokens = []
    
    for part in expression.split(" "):
        try:
            tokens.append(float(part))
        except:
            tokens.append(part)
    
    return tokens


def calculate(expression, return_stack=False):
    """Calculates a reverse polish expression, using spaces to separate
    tokens.

    Basic operations:
        + Addition
        - Subtraction
        * Multiplication
        / Division
        % Modulo (remainder of division)

    Extra operations:
        : Swaps the two top numbers

    If return_stack is True, the stack is returned, otherwise the top item of
    the stack is returned.
    Invalid tokens is ignored.

    Observation: This uses the create_tokens() function, every valid number in
    the expression is converted to float.
    """

    tokens = create_tokens(expression)
    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            number2 = stack.pop()
            stack.append(stack.pop() - number2)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            number2 = stack.pop()
            stack.append(stack.pop() / number2)
        elif token == "%":
            number2 = stack.pop()
            stack.append(stack.pop() % number2)
        elif token == ":":
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(number2)
            stack.append(number1)

    return stack if return_stack else stack.pop()
    