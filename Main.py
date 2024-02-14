from Corner import Corner
from Rubiks import Cube
from time import time

cube = Cube()
final_cube = Cube()
cube.print_cube()
start = time()
for depth_limit in range(1, cube.max_depth_limit + 1):
            cube.max_depth = depth_limit
            final_cube.max_depth = depth_limit
            cube.memo.clear()
            final_cube.memo.clear()
            cube.move_set = []
            final_cube.move_set = []
            if cube.solve_cube(0, None, final_cube):
                cube.move_set.reverse()
                for move in final_cube.final_move_set:
                    revised_move = cube.convert_move(move)
                    cube.apply_move(revised_move)
                    cube.move_set.append(revised_move)
                break
            if final_cube.reverse_solve_cube(0, None, cube):
                for moves in final_cube.move_set:
                    final_cube.undo_move(moves)
                final_cube.print_cube()
                final_cube.memo.clear()
                final_cube.move_set = []
                if final_cube.reverse_solve_cube_v2(0, None):
                    final_cube.final_move_set = final_cube.move_set

end = time()
cube.print_cube()
print("cube moveset:", cube.move_set)
print ("Time: ", end - start)