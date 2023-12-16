# practice - Ana

from Stack import Stack

def stack_first():
    s = Stack()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 9):
        print("Push ", str(i) + ": ", end="")
        s.push(i)
        s.print()
    print("Peek:", s.peek())
    for i in range(3):
        print("Pop: ", s.pop(), "-- ", end="")
        s.print()
    print("Peek:", s.peek())
    print("Is empty?", s.is_empty())