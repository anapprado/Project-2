# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Ana
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(input_str):
    s = Stack([])
    brace_pairs = { ')' : '(', ']' : '[', '}' : '{' }

    for char in input_str:

        if char in "([{":
            s.push(char)
        elif char in ")]}":
            if s.is_empty() or s.pop() != brace_pairs[char]: #Here, brace_pairs[char] retrieves the value associated with the key char in the dictionary brace_pairs
                return False
        
    return s.is_empty()
    

def main():
    print("matcher: ",matcher("[()]"))
    print("matcher: ",matcher("[("))
    print("matcher: ",matcher("hello"))
    print("matcher: ",matcher("(45 + 36) - 5"))
    print("matcher: ",matcher("[()]"))
    print("matcher: ",matcher("{[()]}"))
    print("matcher: ",matcher("{ () [ [] ( {} ) ] }"))
    print("matcher: ",matcher("{[()]} [ ] ( ) ([{}]) { () [ [] ( {} ) ] } ( {[()] [] } {} )"))
    print("matcher: ",matcher("map{key[a(4)]}{b([v])}"))
    print("matcher: ",matcher("map(ke(a(4)))(b((v)))"))
    print("matcher: ",matcher("((a)"))
    print("matcher: ",matcher("({)}"))

# Don't run main on import
if __name__ == "__main__":
    main()

# Dictionary explanation:
# ')': '(', '}': '{', ']': '[': This part of the dictionary 
#consists of key-value pairs. The keys are the closing braces (), }, 
# and ]), and the values are their corresponding opening braces ((, {, and [).
