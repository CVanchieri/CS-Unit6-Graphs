## linkedList: network where the nodes can have jsut one connection
## Binary Search Tree: network where can have a left and a right, 2 connections
## Graphs:
# node aka vertices (one vertex, many vertices)
# connections aka edges

# in a graph, we can have a node with no ceonnections
# in a LinkedList, we can not have a node with no connections



# Network

# LinkedList Traversal
## cur = ll.head
## while cur is nont None:
### cur = cur.next

# Binsary Search Tree Traversal
'''
def bst_traversal(node):
    print(node)
    if node == None:
        return
    bst_traversal(node.left)
    bst_traversal(node.right)
'''

## Graphs terminology, aka types of graphs
### directed vs undirected
#### one way street vs two way streets
#### Twitter: directed, Facebook/LinkedIn: undirected

## acyclic vs cyclic
### 'no circles' vs 'circles'

## weighted vs unweighted
### map with distance/traffic, a number on an 'edge'
### use Dijkstra's algorithm

### decision graph: weights? cost of purchases, or time
### sparse vs dense graphs

## Why traversals are important to other algorithms
## Graph applications
### if you can think of a coding problem as a graph, then you can apply some traversals

##
class ListNode:



        self.next = None
a_node = ListNode(1)
b_node = listNode(2)
a_node.next = b_node


class GraphNode:
    def __init__(value):
        self.value = value
        self.neighbors = []

node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node5 = GraphNode(5)

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node1.neighbors.append(node4)
node3.neighbors.append(node4)
node5.neighbors.append(node4)

## We also want to generalise traversal!
## Graph traversal will work for LinkedList and Binary Search Tree
## Learn by REPS!
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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


# DepthFirst Traversal
def dft(start_node):
    ## make a stack of nodes to visit
    stack = Stack()

    ## make a set to track visited nodes
    visited = set()
    ## while the stack isnt empty
    while stack.size() > 0:
    ### pop off top of stack, this is our current node
        current_node = stack.pop()
    ### if we have not visited, then lets:
        if current_node not in visisted:
    #### mark as visited
            visited.add(current_node)

    #### get the vertexs neighbors
            neighbors = current_node.neighbors
    #### put the current nodes neighbors on the stack
        for nieghbor in neighbors:
            stack.push(neighbor)
