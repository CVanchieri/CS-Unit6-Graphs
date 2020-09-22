""" Video Tutorial """
# https://www.youtube.com/watch?v=j0IYCyBdzfA

class Graph: # graph class 
    def __init__(self, edges): # method to initialize the class 
        self.edges = edges
        self.graph_dict = {}
        # change from tuple to a dictionary
        for start, end in self.edges:

            if start in self.graph_dict:
                self.graph_dict[start].append(end)

            else: 
                self.graph_dict[start] = [end]

        print("------")
        print("Graph dict:", self.graph_dict)
    
    def get_paths(self, start, end, path = []): # method to get paths between nodes 
        path = path + [start]
        # recursive method, simplest case first
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:

            if node not in path:
                new_paths = self.get_paths(node, end, path)

                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path =[]): # method to get shortest between nodes 
        path = path +[start]
        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None 
        for node in self.graph_dict[start]:

            if node not in path:
                sp = self.get_shortest_path(node, end, path)

                if sp:
                    if shortest_path is None or len(shortest_path):
                        shortest_path = sp
        return shortest_path

if __name__ == '__main__':
    # tuple is slower going through each one 
    routes = [ 
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),

    ]

route_graph = Graph(routes)

# dictionary is easier/better 
'''
d = {
    "Mumbai": ["Paris", "Dubai"],
    "Paris": ["Dubai", "New York"],
    "Dubai": ["New York"], 
    "New York": ["Toronto"],
}
'''

### driver ###
start = "Mumbai"
end = "New York"
print("------")
print(f"All Paths between {start} and {end}: ", route_graph.get_paths(start, end))
print("------")
print(f"Shortest Path between {start} and {end}: ", route_graph.get_shortest_path(start, end))


### Search for conected componenets ###

# loop each node in the graph
## has it been explored? 
### if no perform BFS, start here
#### loop intil all the nodes you reach are connected 

### if yes, skip and go to next

