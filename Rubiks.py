from Corner import Corner

CORNERS = ["Front-Right-Top", "Front-Left-Top", "Back-Left-Top", "Back-Right-Top", "Front-Right-Bottom", "Front-Left-Bottom", "Back-Left-Bottom", "Back-Right-Bottom"]
COLORS = ["W", "G", "R", "B", "O", "Y"]
FINAL_CUBE = [
    Corner(['W', 'O', 'G']), #Front-Right-Top
    Corner(('W', 'B', 'O')), #Front-Left-Top
    Corner(('W', 'R', 'B')), #Back-Left-Top
    Corner(('W', 'G', 'R')), #Back-Right-Top
    Corner(('Y', 'G', 'R')), #Front-Right-Bottom
    Corner(('Y', 'O', 'G')), #Front-Left-Bottom
    Corner(('Y', 'B', 'O')), #Back-Left-Bottom
    Corner(('Y', 'R', 'B')) #Back-Right-Bottom
]
VALID_COMBINATIONS = [
    #This will be where the valid combinations go if this is the route we take.
]

class Cube:
    def __init__(self):
        self.cube = self.set_initial_state()

    def is_solved(self):
        return all(corner.colors[0] == self.corners[0].colors[0] for corner in self.corners)

    def get_corner(self, corner):
        return self.cube[corner]

    def set_corner(self, corner, colors):
        self.cube[corner] = Corner(colors)
    
    def set_initial_state(self):
        print("Enter the colors of each corner on the cube.")
        print("Use W for White, G for Green, R for Red, B for Blue, O for Orange, and Y for Yellow.")
        print("Ensure to keep mind of the front of the cube at all points.")
        print("Enter the colors in the format: Color1 Color2 Color3")
    
        corners = []
        for corner in CORNERS:
            while True:
                corner_colors = input("Enter the colors of the " + corner + " corner: ").strip().upper().split()
                if self.is_valid_corner(corner_colors):
                    corners.append(Corner(corner_colors))
                    break
                else:
                    print("Invalid corner colors. Please try again.")

        return corners

    def is_valid_corner(self, corner_colors):
        if len(corner_colors) != 3:
            return False

        if not all(color in COLORS for color in corner_colors):
            return False

        return self.is_valid_combination(corner_colors)

    def is_valid_combination(self, corner_colors):
        # Will need to implement something to check if the combination is valid based on orientation and color comibanations
        return True


    def print_cube(self):
        for corner in self.cube:
            print(corner.colors)

#These are the 12 possible steps that are available at each step of the search. 

    def right_vertical_up(self):
        # This will be the function that rotates the right vertical up
        return True
    
    def right_vertical_down(self):
        # This will be the function that rotates the right vertical down
        return True
    
    def left_vertical_up(self):
        # This will be the function that rotates the left vertical up
        return True

    def left_vertical_down(self):
        # This will be the function that rotates the left vertical down
        return True

    def top_horizontal_right(self):
        # This will be the function that rotates the top horizontal right
        return True

    def top_horizontal_left(self):
        # This will be the function that rotates the top horizontal left
        return True

    def bottom_horizontal_right(self):
        # This will be the function that rotates the bottom horizontal right
        return True

    def bottom_horizontal_left(self):
        # This will be the function that rotates the bottom horizontal left
        return True

    def front_clockwise(self):
        # This will be the function that rotates the front clockwise
        return True    

    def front_counter_clockwise(self):
        # This will be the function that rotates the front counter clockwise
        return True

    def back_clockwise(self):
        # This will be the function that rotates the back clockwise
        return True

    def back_counter_clockwise(self):
        # This will be the function that rotates the back counter clockwise
        return True

    
