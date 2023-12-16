

from Queue import Queue
from Stack import Stack

def flip(stack):
    new_s = Stack([])
    
    while not stack.is_empty():
        x = stack.pop()
        new_s.push(x)
       
    return new_s

    
flip(Stack([1,2,3,4])).print()
flip(Stack([10,11,23,45,56])).print()  

# Or

#print(" New stack in reverse order: ", flip((Stack([1,2,3,4]))) )
    
