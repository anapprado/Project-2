

from Queue import Queue
from Stack import Stack

# 1 Flip

def flip(stack):
    new_s = Stack([])
    
    while not stack.is_empty():
        x = stack.pop()
        new_s.push(x)
       
    return new_s

    
flip(Stack([1,2,3,4])).print()
flip(Stack([10,11,23,45,56])).print()  

# Or

# print(" New stack in reverse order: ", flip((Stack([1,2,3,4]))) )

print()    
#1.1 TEST

def stack_first():
    s = Stack()
    s.print()
    print("Is empty? ", s.is_empty())

    for i in range(1,5):
        s.push(i)
        s.print()
        print("Push: ", str(i), ":", end="")
    print("Peek :", s.peek())

        #print("peek: ", s.peek()) # peek of each stack

Stack()
        
print()
#2 count_uniq

def count_uniq(q):
    count = 0 # to keep track of the number of uniq items
    next = None # none means variables are uninitialized or don't have a value initially. After can be any data type.
    last = None # next = store the next item
    while not q.is_empty():
        next = q.deq()
        if next != last:
            count += 1
            last = next
    return count

print("Sum of uniq numbers are : ",count_uniq(Queue([1, 1, 1, 2, 2, 4, 4, 4, 6])))
print("Sum of uniq numbers are : ",count_uniq(Queue( [3,0,4,4,4,7,7,5,5,5,5] ))) 
print("Sum of uniq numbers are : ",count_uniq(Queue([])))

print()
# Problem 2: Brace matcher


def matcher(input_s):
    s = Stack([])
    braces = { ')' : '(', ']' : '[', '}' : '{' }

    for i in input_s:

        if i in "([{":
            s.push(i)
        elif i in ")]}":
            if s.is_empty() or s.pop() != braces[i]:
                return False
            
    return s.is_empty()

print(matcher("[()]"))
print(matcher("[("))
print(matcher("hello"))

print()
#3 Postfix

from Stack import Stack
from Queue import Queue

def postfix_2_infix(q):
    s = Stack([])
    while not q.is_empty():
        c = str(q.deq()) # here the str handle both operators and operands uniformly (str and int)
        if str(c) in "+-*/":
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 + c + op2) # pops  operands from the stack concatenate with operator c, and pushes the result to stack
        else:
            print("ERROR: unknown operation", op)


# PRACTICE: What do you think the output &
# ADT looks like after every line?
def main():
    # print("=" * 10, "Problem Queue 1", "=" * 10)
    # queue_first()
    print("=" * 10, "Problem Stack 1", "=" * 10)
    stack_first()
    # print("=" * 10, "Problem Queue 2", "=" * 10)
    # queue_test("hello there", "ieedfeefdeeeifeeddeefdddi")
    # print("=" * 10, "Problem Stack 2", "=" * 10)
    # stack_test("hello!", "iuuokuukouuuikuuoouukoooi")
    # print("=" * 10, "Problem Queue 3", "=" * 10)
    # # queue_test("hello!", "ieedfeefdeeeifeeddeefdddi")
    # # print("=" * 10, "Problem Stack 3", "=" * 10)
    # stack_test("hello there", "iuuokuukouuuikuuoouukoooi")


if __name__ == "__main__":
    main()
