from anytree import Node
from collections import deque


### Ex. 2 ###

def test_labyrinth(paths, entrance, exit, last_move, expected):
    result = solve_labyrinth(paths, entrance, exit, last_move)
    if expected == result.name["next"]:
        return True
    else:
        return False 
   
def valid_directions(paths, entrance):
    result = list()
    x = entrance[0]
    y = entrance[1]
    if (x-1, y) in paths:
        result.append(Node({"previous": entrance, "next" : (x - 1, y)}))
    if (x+1, y) in paths:
        result.append(Node({"previous": entrance, "next" : (x + 1, y)}))
    if (x, y-1) in paths:
        result.append(Node({"previous": entrance, "next" : (x, y - 1)}))
    if (x, y+1) in paths:
        result.append(Node({"previous": entrance, "next" : (x, y + 1)}))
    return result

def step(node, paths):
    coords = node.name
    prev_pos = coords.get("previous")
    new_pos = coords.get("next")
    
    paths.discard(prev_pos)
    paths.add(new_pos)
    

def undo_movement(node, paths):
    coords = node.name
    prev_pos = coords.get("next")
    new_pos = coords.get("previous")
    
    paths.add(prev_pos)
    paths.discard(new_pos)
    
def solve_labyrinth(paths, entrance, exit, last_move):
    result = None
    if entrance == exit:
        return last_move
    else:
        last_move.children = valid_directions(paths, entrance)
        print(last_move.children)
        if len(last_move.children) == 0: # dead-end base case
            undo_movement(last_move, paths) # backtracking
        else: # recursive step
            possible_moves = deque(last_move.children)
            while result is None and len(possible_moves) > 0:
                current_move = possible_moves.pop()
                step(current_move, paths)
                curr_position = current_move.name.get("next")
                result = solve_labyrinth(paths, curr_position, exit, current_move)
            if result is None:
                undo_movement(last_move, paths) # backtracking
    return result

def create_board():       
    paths = set([
            (1,0),       (3,0), (4,0), (5,0),
        (0,1), (1,1),(2,1), (3,1),        (5,1),
        (0,2),       (2,2),        (4,2), (5,2),
        (0,3),       (2,3), (3,3),        (5,3),
        (0,4),                     (4,4),
        (0,5), (1,5),(2,5), (3,5), (4,5)
        ])
    entrance = (1, 0)
    exit = (5, 3)

    return paths, entrance, exit

paths, entrance, exit = create_board()

##Test cases

test_labyrinth(paths, entrance, exit, Node("start"), (5, 3))
#print(test_labyrinth(paths, (4, 4), (4,2), Node("start"), (4,2)))
#print(test_labyrinth(paths, (3, 3), (4,4), Node("start"), (4,4)))
#print(test_labyrinth(paths, (0, 5), (1,0), Node("start"), (1,0)))
