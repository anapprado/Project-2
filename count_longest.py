# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Ana
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
# Initialize the length variable
    len = 0
# Check if the queue is not empty
    while not q.is_empty():
        # Dequeue the first character from the queue
        current_char = q.deq()
        # Initialize variables for the current character and consecutive length
        current_len = 1
         # Count consecutive characters
        while not q.is_empty() and q.front() == current_char:
        # Dequeue the consecutive character
            q.deq()
        # Increment the consecutive length
            current_len +=1
        # Update the length if the current consecutive sequence is longer
        len = max(len, current_len)
    # Return the length of the longest consecutive subsequence
    return len

def main():
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee" ])))


# Don't run main on import
if __name__ == "__main__":
    main()

