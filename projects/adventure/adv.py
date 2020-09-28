"""
### Sprint Challenge Description ###

You are provided with a pre-generated graph consisting of 500 rooms. You are responsible for filling `traversal_path` with 
directions that, when walked in order, will visit every room on the map at least once.

Open `adv.py`. There are four parts to the provided code:
* World generation code. Do not modify this!
* An incomplete list of directions. Your task is to fill this with valid traversal directions.
* Test code. Run the tests by typing `python3 adv.py` in your terminal.
* REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.

You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. 
Your starting graph should look something like this:
```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```
Try moving south and you will find yourself in room `5` which contains exits `['n', 's', 'e']`. You can now fill in some entries in your graph:
```
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
```
You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will 
need to write a traversal algorithm that logs the path into `traversal_path` as it walks.

Your solution **must** generate the solution by using graph traversal algorithms. Hardcoding a solution is not acceptable.

## Hints

There are a few smaller graphs in the file which you can test your traversal method on before committing to the large graph. You may find 
these easier to debug.

Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. 
This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the 
nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code 
from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it 
in your BFS queue like normal.
2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.
### If all paths have been explored, you're done! ###
"""
# necessary imports
from room import Room
from player import Player
from world import World
from queue import *
from ast import literal_eval

# Load world
world = World()
# You may uncomment the smaller graphs for development and testing purposes.
'''
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
'''
# map_file = "/Users/cvanchieri/Documents/CS/GitHub/Repos/CS-Unit6-Graphs/projects/adventure/maps/test_line.txt"
# map_file = "/Users/cvanchieri/Documents/CS/GitHub/Repos/CS-Unit6-Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "/Users/cvanchieri/Documents/CS/GitHub/Repos/CS-Unit6-Graphs/projects/adventure/maps/test_loop.txt"
# map_file = "/Users/cvanchieri/Documents/CS/GitHub/Repos/CS-Unit6-Graphs/projects/adventure/maps/test_loop_fork.txt"
map_file = "/Users/cvanchieri/Documents/CS/GitHub/Repos/CS-Unit6-Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

### FILL THIS IN ###
traversal_path = [] # create an empty list for the traversal path

def inverted(move): # function to invert directions on move
    if move == 'n':
        return 's'
    if move == 's':
        return 'n'
    if move == 'e':
        return 'w'
    if move == 'w':
        return 'e'

explored = {} # create an empty dict for the explored rooms 
explored[player.current_room.id] = {x: '?' for x in player.current_room.get_exits()} # find any exists from the current room
print('explored:', explored) # print the explored rooms 

explored[player.current_room.id] = {x: '?' for x in player.current_room.get_exits()} # find any exists from the current room
unexplored = set() # create an empty set for the unexplored exits
for exit in player.current_room.get_exits(): # loop through exits of current room 
    unexplored.add(f"Room {player.current_room.id}: {exit}") # add each exit to the unexplored exists set 
print('unexplored:', unexplored) # print the unexplored exits 

### DFS: search for a dead end ###
while unexplored: # loop while unexplored exits set is not empty

    move = None # set the starting move to None
    current_room = player.current_room.id # set the current room as the players current room 
    if '?' in explored[player.current_room.id].values():  # loop if there is a '?' in the current room dict 

        if 'n' in explored[current_room] and explored[current_room]['n'] == '?': # if 'n' is unexplored
            move = 'n'
        elif 'e' in explored[current_room] and explored[current_room]['e'] == '?': # if 'e' is unexplored
            move = 'e'
        elif 's' in explored[current_room] and explored[current_room]['s'] == '?': # if 's' is unexplored
            move = 's'
        elif 'w' in explored[current_room] and explored[current_room]['w'] == '?': # if 'w' is unexplored
            move = 'w'

        unexplored.remove(f"Room {player.current_room.id}: {move}") # remove the visited room from the unexplored exists set 
        player.travel(move) # move the player 
        traversal_path.append(move) # append the move to the traversal path list 
        new = player.current_room.id # set the new as the players current room 

        if new not in explored: # if the new room is not in the explored rooms dict 
            explored[new] = {x: '?' for x in player.current_room.get_exits()} # find any exists from the current room 

        explored[current_room][move] = new # set the current room in explored rooms dict to the new room 
        explored[new][inverted(move)] = current_room # set the explored dict with the current room 

        for exit, direction in explored[new].items(): # loop through the new room in the explored rooms dict items

            if direction == '?': # if there is a '?' for a direction
                unexplored.add(f'Room {new}: {exit}') # add the new rooms exit direction to the unexplored exits set 

        if f'Room {new}: {inverted(move)}' in unexplored: # if the new room invereted move is in the unexplored exits set 
            unexplored.remove(f'Room {new}: {inverted(move)}') # remove the new room from the unexplored exists set

### BFS: search for the nearest unexplored room ###
    else:
        current = player.current_room.id # set the current room 
        q = Queue() # set the empty queue

        for exit, room in explored[current].items(): # loop through explored rooms current room items

            q.put([[exit, room]]) # put the exit direction and room in the queue

        while not q.empty(): # loop while the queue is not empty 
            path = q.get() # get the value from the queue and store it
            v = path[-1] # store the path without last element 

            if '?' in [room for exit, room in explored[v[1]].items()]: # if there is a '?' unexplored exit in the current room

                for exit, room in path: # loop through paths room exit direction
                    player.travel(exit) # move the player 
                    traversal_path.append(exit) # append the exit direction to the traversal path list 
                break # must break or infinate
  
            else: # else if no unexplored exists 
                for exit, room in explored[v[1]].items(): # loop through the explored rooms set items
                    if room != current and room not in [room for exit, room in path]: # if the room is not equal to the current room, and not in room in exit direction or path
                        q.put(list(path) + [[exit, room]]) # put the path list and exit direction room in the queue 

#print(explored)

### TRAVERSAL TEST ###
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

'''
###### UNCOMMENT TO WALK AROUND ######

 player.current_room.printRoomDescription(player)
 while True:
     cmds = input("-> ").lower().split(" ")
     if cmds[0] in ["n", "s", "e", "w"]:
         player.travel(cmds[0], True)
     else:
         print("I did not understand that command.")
'''