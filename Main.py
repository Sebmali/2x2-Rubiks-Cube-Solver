from Corner import Corner
from Rubiks import Cube

cube = Cube()
if(cube.is_solved()):
    print("The cube is solved.")
else:
    cube.print_cube()
