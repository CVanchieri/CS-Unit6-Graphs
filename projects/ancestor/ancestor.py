"""
### Depth First Search ###
# we want to go the end of each path to find the longest path, 'earliest' ancestor
"""

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node): # depth first search (stack) 
    stack = Stack() # create an empty stack
    stack.push([starting_node]) # push the starting_node to the stack
    # visited = set()

    longest_path = [starting_node] # create a list with the starting_node
    earliest_ancestor = starting_node # set the earliest_ancestor initially as the starting_node
    has_parent = False # set has_parent initially to Flase

    while stack.size() > 0: # loop if the stack size is greater than 0 
        path = stack.pop() # pop element off stack and store path 

        if (len(path) > len(longest_path)) or (path[0] < longest_path[0]): # if the length of longest_path is greater than the length of longest_path or if the initial path elemnt is less than the initial longest element
            longest_path = path.copy() # copy the path and store it as the new longest_path 
            earliest_ancestor = path[0] # set the initial path element to the earliest_ancestor 

        for t in ancestors: # loop through ancestors 
            if t[-1] == earliest_ancestor: # if the last element of t is equal to the earliest_ancestor
                path_copy = path.copy() # copy the path and store it 
                path_copy.insert(0, t[0]) # insert elements into path_copy
                stack.push(path_copy) # push the path_copy to the stack
                has_parent = True # set has_parent to True 

        if has_parent == False: # if has_parent is Flase
            earliest_ancestor = -1 # remove 1 from the earliest_ancestor 

    return earliest_ancestor # return the earliest ancestor 