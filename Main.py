from Corner import Corner
from Rubiks import Cube

cube = Cube()
cube.print_cube()
cube.solve_cube_outer()
cube.print_cube()
print(cube.move_set)

#b r w
#o y g
#y r b
#b o w
#w g r
#w g o
#y r g
#o y b