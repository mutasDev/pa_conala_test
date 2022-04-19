#reverse a priority queue `q` in python without using classes
.

def reverse(q): 
    stack = [] 
    while(q.empty() == False): 
        stack.append(q.queue[0]) 
        q.get() 
    while(len(stack) != 0 ): 
        q.put(stack[-1]) 
        stack.pop()