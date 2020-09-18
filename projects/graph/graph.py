"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy

class Queue(): # basic Queue structure 
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

class Stack(): # basic Stack structure
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

### Graph ####
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id): # O(1) time complexity
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() 

        # additional options (class)
        '''
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = {}

            else:
                return "Vertex is already in Graph"
        '''

    def delete_vertex(self, vertex_id): # O(n) time complexity
        pass
        # delete the key value pair 
        
        # find all references to this vertex 

    def delete_edge(self, v1, v2): 
        pass
        # access v1, remove v2
        # access v2, remove v1

    def add_edge(self, v1, v2): # O(1) time complexity
        """
        Add a directed edge to the graph. from V1-> to V2 
        """
        if v1 in self.vertices and v2 in self.vertices: # check to see if v1 & v2 exists already
            self.vertices[v1].add(v2) # # add connection from v1 to v2 
        else: # else 
            print("That vertex does not exist")

        # additional options (class)
        """
        if (v1 or v2) not in self.vertices:
            return "vertex does exist"
            self.vertices[v1].add(v2)
        ###
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices{v1}.add(v2)
        else:
            print("One of these vertices does not exist)
        """
            
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        q = Queue() # create an empty Queue 
        q.enqueue(starting_vertex) # set enqueue with the starting vertex

        while q.size() > 0: # loop if the size is greater than 0
            v = q.dequeue() # dequeue and store 

            if v not in visited: # if v has not in the set 
                visited.add(v) # add v to the set 
                print(v) 
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]: # loop through neighbors 
                    q.enqueue(neighbor) # add each neighbor to the end of the que 

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        s = Stack() # create an empty Stack 
        s.push(starting_vertex) # push the starting_vertex to the top of the stack

        while s.size() > 0: # loop if the size is greater than 0
            v = s.pop() # pop off first element and store 

            if v not in visited: # if v has not been visited yet
                visited.add(v) # add to the set 
                print(v)
                for neighbor in self.vertices[v]: # loop through neighbors 
                    s.push(neighbor) # add each neighbor to the bottom of the stack

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None: # if visited is not empty
            visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        if starting_vertex not in visited: # if starting_vertex has not been visited yet
            print(starting_vertex)
            visited.add(starting_vertex) # add to the set 

            for neighbor in self.vertices[starting_vertex]: # loop through each neighbor 
                self.dft_recursive(neighbor, visited) # call the dft_recursive method on each neighbor 

    def bfs(self, starting_vertex, destination_vertex): # great if you know to result is somewhere close to the root/start 
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        q = Queue() # create an empty Queue
        q.enqueue([starting_vertex]) # set the starting_vertex with enqueue 

        while q.size() > 0:
            path = q.dequeue() # dequeue and store first path
            v = path[-1] # store the vertex from the end of path 

            if v == destination_vertex: # if v is equal to the destination_vertex
                return path # return the path 

            if v not in visited: # if v has not been visited yet 
                visited.add(v) # add v to the vistied set 

                for neighbor in self.vertices[v]: # loop through the neighbors 
                    path_copy = list(path) # make a copy of the path 
                    path_copy.append(neighbor) # append each neighbor to the back of the path copy 
                    q.enqueue(path_copy) # enqueue the path copy to the queue 

    def dfs(self, starting_vertex, destination_vertex): # great for if you know the start and end, like a maze with 1 entry/1 exit
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        s = Stack() # create an empty Stack
        s.push([starting_vertex]) # push the starting vertex to the top of the stack 

        while s.size() > 0: # loop if the size is greater than 0
            path = s.pop() # pop off the top element of the stack and store 
            v = path[-1] # store the vertex from the end of path

            if v == destination_vertex: # if v is equal to the destination_vertex
                return path # return the path 
            if v not in visited: # if v has not been visited yet 
                visited.add(v) # add v to the vistied set 

                for neighbor in self.vertices[v]: # loop through the neighbors
                    path_copy = list(path) # make a copy of the path 
                    path_copy.append(neighbor) # append each neighbor to the back of the path copy 
                    s.push(path_copy) # push the path copy to the Stack

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None: # if visited is not empty
            visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        if path is None: # if the path is empty 
            path = [] # create an empty list 
        visited.add(starting_vertex) # add the starting_vertex to the set 
        path = path + [starting_vertex] # set the path 

        if starting_vertex == destination_vertex: # if the starting_vertex is equal to the destination_vertex
            return path # return the path 

        for neighbor in self.vertices[starting_vertex]: # loop through neighbors 
            if neighbor not in visited: # if the neighbor has not been visited 
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path) # create a new path using the dfs_recursive method

                if new_path: # if there is a new_path 
                    return new_path # return the new path 

        return None # return None 

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('-- Vertices --')
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('-- BFT --')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('-- DFT --')
    graph.dft(1)
    print('-- DFT Recursive--')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('-- BFS --')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('-- DFS --')
    print(graph.dfs(1, 6))
    print('-- DFS Recursive --')
    print(graph.dfs_recursive(1, 6))

"""
If you can make a function to return the neighbors of this thing, you can treat the problem as a graphs problem 

If you can figure out when this teim is and is not "related" to other items, graphs problem --> graphs algorithms

How to Solve (Almost) Any Graphs Prblem

1. Describle the probme using graphs terminology
- What are your nodes? 
- What are your edges? aka when is a node connected to another node? 
- Are there connected components?

2. Build your graph Or write your getNeighbors() function 

3. Choose your algorithm 
- BFT, DFT, BFS, DFS

Given two words (begin_word and end_word), and a dictionary's word list, 
return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.

Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
return None if it can't be done
all words are lowercase (or you can make them lowercase)


return None if it cant be done 
all words are lowercase (or yo ucan make them lowercase)


1. Graphs terminology
- Nodes: words!
- Edges: a word is connected to another world if they share all letters except one 

2. getNeighbors - graph optional 

3. Choose algoritm: BFS 


"""
import string
def find_neighbors(word, wordList):
    # for every letter in the word. substitute a ltter of the alphabet: O(len(word) * 26)
    # check if this new word is in our giant word list: O(1)
    # if so, its a neighbor!
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in wordList:

    """
def find_neighbors_alt(something):
    same_length = [word for word in all_the_words if len(word) == len(something)]
    matches = []

    # count how many letters are the same to see if each word is an edge 
    for word in same_length:
        chars = split(word)
        match = split(something)
        count = 0
        for i in range(0, len(chars)):
            if chars[i] == match[i]:
                count += 1
        if count == len(something) - 1:
            matches.append(word)
    return matches
    """
def bfs(self, start_word, end_word): # great if you know to result is somewhere close to the root/start 
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        q = Queue() # create an empty Queue
        q.enqueue([start_word]) # set the starting_vertex with enqueue 

        while q.size() > 0:
            path = q.dequeue() # dequeue and store first path
            v = path[-1] # store the vertex from the end of path 

            if v == end_word: # if v is equal to the destination_vertex
                return path # return the path 

            if v not in visited: # if v has not been visited yet 
                visited.add(v) # add v to the vistied set 

                for neighbor in self.vertices[v]: # loop through the neighbors 
                    path_copy = list(path) # make a copy of the path 
                    path_copy.append(neighbor) # append each neighbor to the back of the path copy 
                    q.enqueue(path_copy) # enqueue the path copy to the queue 
