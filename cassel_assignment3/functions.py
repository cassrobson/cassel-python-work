"""
-------------------------------------------------------
functions for Stack Class
-------------------------------------------------------
Author:  Cassel Robson
ID:      210507000
Email:   robs7000@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """

    target = Stack()

    while source1.is_empty() == False and source2.is_empty() == False:
        target.push(source1.pop())
        target.push(source2.pop())

    if source1.is_empty() == False:
        while source1.is_empty() == False:
            target.push(source1.pop())
    if source2.is_empty() == False:
        while source2.is_empty() == False:
            target.push(source2.pop())

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    items = []
    while not source.is_empty():
        items.append(source.pop())
    for item in items:
        source.push(item)

    return source


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    new_string = string.lower()
    newer_string = ''
    for i in new_string:
        if i.isalpha() == True:
            newer_string += i

    stack = Stack()
    for i in newer_string:
        stack.push(i)

    stack = stack_reverse(stack)
    stack = stack_reverse(stack)

    reversed_string = ''
    for i in stack:
        reversed_string += i

    if reversed_string == newer_string:
        palindrome = True
    else:
        palindrome = False

    return palindrome


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    assert type(opstring) == str, "Opstring must be string type"
    s = Stack()
    values_out = []

    for i in opstring:
        if i == 'S':
            s.push(values_in[0])
            values_in.remove(values_in[0])

        if i == 'X':
            values_out.append(s.pop())

    return values_out
