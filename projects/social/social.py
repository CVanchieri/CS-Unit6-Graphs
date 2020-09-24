import random, itertools

### Standard Queue class ###
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

### User class ###
class User:
    def __init__(self, name):
        self.name = name

### SocialGraph class ###
class SocialGraph:
    def __init__(self): # initializor method
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id): # add_friendship method
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name): # add_user method
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates(self, arr):
        copy_arr = list(arr)
        for idx in range(len(copy_arr)):
            rand_index = random.randint(0, len(copy_arr) -1)
            copry_arr[idx], copy_arr[rand_index] = copy_arr[rand_index], copy_arr[idx]
        return copy_arr


    def populate_graph(self, num_users, avg_friendships): # populate_graph method
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # your code
        # Add users
        for i in range(num_users): # loop through num_users and add to friendships
            self.add_user(str(i+1))

        connections = int((num_users * avg_friendships) / 2) # set true connections 
        possibles = list(itertools.combinations(self.users, 2)) # set possible connetions 
        randoms = random.sample(possibles, connections) # set random connections 

        for i in randoms: # loop through randoms and use add_friendship method to find for connections.
            self.add_friendship(i[0], i[1])
        '''
        #### class solution ###
        for i in range(num_users):
            self.add_user(i)

        # create friendships 
        # you could create a list with all possible friendship combinations 
        all_friend_combos = []
        for person in range(1, num_users):
            for friend in range(person + 1, num_users + 1):
                all_friend_combos.append((person, friend))

        # shuffle the list 
        shuffled_combos = self.fisher_yates(all_friend_combos)
 
        total_friendships = num_users * avg_friendships 
        elements_needed = total_friendships // 2 
        combos_to_make = shuffled_combos[:elements_needed]

        for friendship in combos_to_make:
            self.add_friendship(friendship[0], friendship[1])
        '''

    def bfs(self, start, end): # breath-first seach method, 'shortest path'
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # your code
        visited = set() # create an empty 'set' to store visisted vertex, set sorts 

        q = Queue() # create an empty Queue
        q.enqueue([start]) # set the start with enqueue 

        while q.size() > 0:
            path = q.dequeue() # dequeue and store first path
            v = path[-1] # store the element from the end of path 

            if v == end: # if v is equal to the end
                return path # return the path 

            if v not in visited: # if v has not been visited yet 
                visited.add(v) # add v to the vistied set 

                for neighbor in self.friendships[v]: # loop through the neighbors 
                    path_copy = list(path) # make a copy of the path 
                    path_copy.append(neighbor) # append each neighbor to the back of the path copy 
                    q.enqueue(path_copy) # enqueue the path copy to the queue 
    '''
    def get_all_social_paths(self, user_id): # get_all_social_paths method
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # your code
        for i in self.users: # loop through self.users
            if i != user_id and self.bfs(user_id, i) != None: # if i does not equal user_id and self.bfs does not eqaul to None
                visited[i] = self.bfs(user_id, i) # add the user_id with self.bfs to visited 
        return visited

    '''

    def linear_populate_graph(self, num_users, avg_friendships):
        
    ### class solution ###
    # breath first traversal 
    def get_all_social_paths(self, user_id):
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
    
        # your code
        q.enqueue([user_id])

        while q.size() > 0:
            current_path = q.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:
                visited[current_user] = current_path

                friends = self.friendships[current_user]

                for friend in friends:
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited

# 3 from Kevin Bacon, 1 from Junior Bacon 
        
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 2)
    print('--- friendships ---')
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('--- connections ---')
    print(connections)

    ## connections dict holds everyone in 1's extended social network 
    print(f'percent of users in extended social network: {len(connections) / 1000 * 100}%') # percent of users in extended social network

    ## how could you improve this model?
    # chaining 
    # skew numbers towards a few individuals