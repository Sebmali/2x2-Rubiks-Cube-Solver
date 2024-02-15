from Corner import Corner
from Rubiks import Cube
from time import time

def clear(cube):
    cube.memo.clear()
    cube.move_set = []

cube = Cube()
final_cube = Cube(True)
cube.print_cube()
print("---------------------------------")
start = time()
for depth_limit in range(1, cube.max_depth_limit + 1):
    cube.max_depth = depth_limit
    final_cube.max_depth = depth_limit
    clear(cube)
    clear(final_cube)
    if cube.solve_cube(0, None, final_cube):
        cube.move_set.reverse()
        cube.apply_rem_moves(final_cube.final_move_set)
        break
    if final_cube.reverse_solve_cube(0, None, cube):
        for moves in final_cube.move_set:
            final_cube.undo_move(moves)
        clear(final_cube)
        if final_cube.reverse_solve_cube_v2(0, None):
            final_cube.final_move_set = final_cube.move_set

end = time()
cube.print_cube()
print("cube moveset:", cube.move_set)
print ("Time: ", end - start)