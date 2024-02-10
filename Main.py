from Corner import Corner
from Rubiks import Cube
from time import time

cube = Cube()
final_cube = Cube()
cube.print_cube()
#cube.print_percent_complete()
start = time()
#cube.solve_cube_outer(final_cube)
for depth_limit in range(1, cube.max_depth_limit + 1):
            cube.max_depth = depth_limit
            final_cube.max_depth = depth_limit
            cube.memo.clear()
            final_cube.memo.clear()
            cube.move_set = []
            final_cube.move_set = []
            #print("Depth: ", depth_limit, final_cube.max_depth)
            if cube.solve_cube(0, None, final_cube):
                #print("Forward works")
                #print("self cube")
                #cube.print_cube()
                common_keys = set(cube.memo.keys()) & set(final_cube.memo.keys())

                if common_keys:
                    print("Common keys: ", common_keys)
                else:
                    print("No common keys")
                    #print(type(self.memo))
                    print(final_cube.memo)
                break
            if final_cube.reverse_solve_cube(0, None, cube):
                print("Reverse works")
                print(final_cube.common_keys)
                print("Initial cube moveset:", cube.move_set)
                for move in final_cube.move_set:
                    cube.move_set.append(move)
                cube.apply_rem_moves(final_cube.move_set)
                break

end = time()
#cube.left_vertical_up()
#cube.percent_of_front_solved()
print("THIS IS THE INITIAL CUBE")
cube.print_cube()
print("Initial cube moveset:", cube.move_set)
print("Final cube moveset:", final_cube.move_set)
print ("Time: ", end - start)
#final_cube.right_vertical_down()
final_cube.print_cube()
#b r w
#o y g
#y r b
#b o w
#w g r
#w g o
#y r g
#o y b