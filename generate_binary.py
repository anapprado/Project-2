# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Ana
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
# Create 2 empty Q
    numbers = Queue([])
    t = Queue([])
# Enqueue the first binary number "1" to the t Queue
    t.enq("1") 
# if N is too small return an empty Q
    if N < 1:
        return Queue([])
       
    for i in range(N):
        x = t.deq() # deq tQ & add it to numbQ
        numbers.enq(x)
        t.enq(x + "0")
        t.enq(x + "1")

    return numbers

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()
   

# Don't run main on import
if __name__ == "__main__":
    main()

