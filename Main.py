"""
Main.py 
Purpose: This file initiates the solving of the Rubiks Cube by setting up a initial cube
and a final cube for the purpose of bidirectional search algorithm. The input from the 
user may be in the format of a text file input, or a manual input. 
Authors: Sebastian Maliczewski, Shayne Prakash
"""
from Corner import Corner
from Rubiks import Cube
from time import time

def clear(cube):
    cube.memo.clear()
    cube.move_set = []

def solve_cube(initial_cube, final_cube):
    for depth_limit in range(1, initial_cube.max_depth_limit + 1):
        initial_cube.max_depth = depth_limit
        final_cube.max_depth = depth_limit
        clear(initial_cube)
        clear(final_cube)
        if initial_cube.solve_cube(0, None, final_cube):
            initial_cube.move_set.reverse()
            initial_cube.apply_rem_moves(final_cube.final_move_set)  
            break
        if final_cube.reverse_solve_cube(0, None, initial_cube):
            for moves in final_cube.move_set:
                final_cube.undo_move(moves)
            clear(final_cube)
            if final_cube.reverse_solve_cube_v2(0, None):
                final_cube.final_move_set = final_cube.move_set
    return initial_cube.move_set

cube = Cube()
final_cube = Cube(True)
start = time()
move_set = solve_cube(cube, final_cube)
end = time()
print("cube moveset:", move_set)
print ("Time: ", end - start)