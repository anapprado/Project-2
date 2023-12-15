# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Ana
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue()
    stack = Stack()

    while not q_orig.is_empty(): # entre parentese é o primeiro a acontecer
        stack.push(q_orig.deq())
    while not stack.is_empty():
        q_new.enq(stack.pop())

    return q_new

def main():
    q = Queue(list(range(1,5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()
   

# Don't run main on import
if __name__ == "__main__":
    main()
