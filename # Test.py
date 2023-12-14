# Practice_problem1 - Write a function flip that takes a stack 
# as a parameter and returns a new stack in reverse order.
# by Ana

from Queue import Queue
from Stack import Stack

def flip(stack):
    new_stack = Stack()
    while not stack.is_empty():
        new_stack.push(stack.pop())
    return new_stack


# FUNCTION CALL
flip(Stack([1,2,3,4,5,6,7])).print()
# OR
flip(Stack(list(range(1,8)))).print()
