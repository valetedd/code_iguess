# -*- coding: utf-8 -*-
# Copyright (c) 2023, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

# This is a fake (i.e. it fails) implementation of the 'do_move' 
# function, that does always select an invalid couple of coordinates
# as next move to run. Change the body of the function to provide 
# better instructions to play The Cracked Chess.
def do_move_wall(labyrinth, length, explorer_position, exit, notebook):
    if labyrinth not in notebook:
        walls = missing_combinations(length, labyrinth)
        next_rooms = available_rooms(explorer_position, labyrinth) 
        safe_rooms = adj_rooms(exit)  
        exit_distance = (exit[0] - explorer_position[0], exit[1] - explorer_position[1])
        if exit_distance[0] > 0:
            if exit_distance[0] > exit_distance[1]:
                if next_rooms[0] != None and next_rooms[0] not in safe_rooms:
                    labyrinth.remove(next_rooms[0])
                    walls.append(next_rooms[0])
            else:
                if next_rooms[1] != None and next_rooms[1] not in safe_rooms:
                    labyrinth.remove(next_rooms[1])
                    walls.append(next_rooms[1])
        else:
            if exit_distance[0] > exit_distance[1]:
                if next_rooms[2] != None and next_rooms[2] not in safe_rooms:
                    labyrinth.remove(next_rooms[2])
                    walls.append(next_rooms[2])
            else:
                if next_rooms[3] != None and next_rooms[3] not in safe_rooms:
                    labyrinth.remove(next_rooms[3])
                    walls.append(next_rooms[3])
        return labyrinth, notebook



def missing_combinations(int, comb):
    mis_comb = []
    n = range(int+1)
    for x in range(int+1):
        for y in n:
            if (x,y) not in comb:
                mis_comb.append((x,y))
    return mis_comb

def available_rooms(explorer_position, labyrinth):
    next_rooms = []
    explorer_x = explorer_position[0]  
    explorer_y = explorer_position[1]  
    if explorer_x + 1 in labyrinth:
        next_rooms.append((explorer_x + 1, explorer_y))
    else:
        next_rooms.append(None)
    if explorer_y + 1 in labyrinth:
        next_rooms.append((explorer_x , explorer_y + 1))
    else:
        next_rooms.append(None)
    if explorer_x - 1 in labyrinth:
        next_rooms.append((explorer_x - 1, explorer_y))
    else:
        next_rooms.append(None)
    if explorer_y - 1 in labyrinth:
        next_rooms.append((explorer_x, explorer_y - 1))
    else:
        next_rooms.append(None)
    return next_rooms

def adj_rooms(exit):
    result = []
    x = exit[0]
    y = exit[1]
    result.append((x+1,y))
    result.append((x-1,y))
    result.append((x,y+1))
    result.append((x,y-1))
    return result

lab = [
        (0,0),            (3,0),(4,0),            (7,0),
              (1,1),(2,1),      (4,1),      (6,1),(7,1),
              (1,2),                  (5,2),(6,2),(7,2),
                    (2,3),(3,3),(4,3),(5,3),(6,3),(7,3),
        (0,4),(1,4),(2,4),(3,4),            (6,4),(7,4),
        (0,5),      (2,5),
        (0,6),(1,6),(2,6),      (4,6),(5,6),(6,6),
        (0,7),(1,7),            (4,7)]

print(do_move_wall(lab, 8, (0,5), (7,3), set()))