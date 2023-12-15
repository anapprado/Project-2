# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Ana
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):
    s = Stack([])
    for char in str:
        if char in "([{":
            s.push(char)
        elif char in ")]}":
            if  is_matching(s.pop(), char):
                return True
    return s.is_empty()
    
def is_matching(open,close):
    return(open == "(" and close == ")") or \
          (open == "{" and close == "}") or \
          (open == "[" and close == "]") 

    

def main():
    print("matcher: ", matcher("[()]"))
    print("matcher: ",matcher("[("))
    print("matcher: ",matcher("hello"))
    #print("matcher: ",matcher(" ")) # if it is empty why is true?

# Don't run main on import
if __name__ == "__main__":
    main()

# This code uses the or operator to combine three conditions. 
# It checks if either of the following conditions is true
# The backslash \ at the end of each line is a line 
# continuation character, indicating that the line 
# continues to the next line. It allows you to break a long 
# line of code into multiple lines for better readability.