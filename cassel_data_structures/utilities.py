"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Cassel Robson
ID:      210507000
Email:   robs7000@mylaurier.ca
__updated__ = "2022-01-31"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Stack_array import Stack
from Priority_Queue_array import Priority_Queue
from List_array import List
# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in source[::-1]:
        stack.push(i)
        source.pop()


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        target.append(stack.pop())
    target.reverse()


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    s = Stack()
    print("Stack is empty expected True: ", s.is_empty())
    s.push(3)
    array_to_stack(s, source)
    print("Empty expected False: ", s.is_empty())
    print("top value: ", s.peek())
    s.pop()
    print("stack after pop(): ", s)
    print("Empty expected False if len(source)>1: ", s.is_empty())


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        queue.insert(i)
    while len(source) != 0:
        source.remove(source[0])


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("Stack is empty expected True: ", q.is_empty())
    print()
    q.insert(3)
    array_to_queue(q, a)
    print()
    print("Empty expected False: ", q.is_empty())
    print()
    print("top value: ", q.peek())
    print()
    q.remove()
    print("stack after pop(): ", [print(i) for i in q])
    print()
    print("Empty expected False if len(source)>1: ", q.is_empty())
    print()
    q.remove()
    print()
    print("Queue should have one less value: ", [print(i) for i in q])
    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        pq.insert(i)
    while len(source) != 0:
        source.remove(source[0])


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("Stack is empty expected True: ", pq.is_empty())
    print()
    pq.insert(3)
    array_to_queue(pq, a)
    print("Empty expected False: ", pq.is_empty())
    print()
    print("top value: ", pq.peek())
    print()
    pq.remove()
    print("\nstack after remove(): ", [print(i, end='') for i in pq])
    print()
    print("\nEmpty expected False if len(source)>1: ", pq.is_empty())
    print()
    pq.remove()
    print("\nQueue should have one less value: ",
          [print(i, end='') for i in pq])
    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        llist.append(i)
    while len(source) != 0:
        source.remove(source[0])
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in llist:
        target.append(i)
    while llist.__len__() != 0:
        llist.remove(llist[0])

    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    for i in range(20):
        lst.append(i)
    print("lst object")
    for i in lst:
        print(i, end=' ')

    print('\n')
    print("testing is_empty: ")
    print(lst.is_empty())
    print()
    print("testing insert method with 3 at index 2")
    print(lst.insert(2, 3))
    for i in lst:
        print(i, end=' ')

    print('\n')
    print()
    print("Testing count function with 4...")
    print(lst.count(4))

    print()
    print("Testing index method with 7...")
    print(lst.index(7))

    print()
    print("testing find method with 4...")
    print(lst.find(4))

    print()
    print("Testing max method...")
    print(lst.max())
    print()
    print("Testing min method...")
    print(lst.min())

    print()
    print("Testing remove method with 5...")
    lst.remove(5)
    for i in lst:
        print(i, end=' ')

    print('\n')
    return
