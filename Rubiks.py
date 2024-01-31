from Corner import Corner

CORNERS = ["Front-Right-Top", "Front-Left-Top", "Back-Left-Top", "Back-Right-Top", "Front-Right-Bottom", "Front-Left-Bottom", "Back-Left-Bottom", "Back-Right-Bottom"]
COLORS = ["W", "G", "R", "B", "O", "Y"]
FINAL_CUBE = {
    Corner(['R', 'W', 'B']), #Front-Right-Top
    Corner(['R', 'W', 'G']), #Front-Left-Top
    Corner(['O', 'W', 'G']), #Back-Left-Top
    Corner(['O', 'W', 'B']), #Back-Right-Top    
    Corner(['R', 'Y', 'B']), #Front-Right-Bottom
    Corner(['R', 'Y', 'G']), #Front-Left-Bottom
    Corner(['O', 'Y', 'G']), #Back-Left-Bottom
    Corner(['O', 'Y', 'B']) #Back-Right-Bottom
}

class Cube:
    def __init__(self):
        self.cube = self.set_initial_state()
        self.max_depth = 15

    def is_solved(self):
        for i in length(FINAL_CUBE):
            if self.cube[i].colors != FINAL_CUBE[i].colors:
                return False
        return True

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
                corner_combo = Corner(corner_colors)
                if corner_combo.is_valid_corner():
                    corners.append(Corner(corner_colors))
                    break
                else:
                    print("Invalid corner colors. Please try again.")

        return corners

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

    def solve_cube(self):
        for depth in range(1,self.max_depth):
            result = self.depth_limited_search(self.cube, depth)
            if result is not None:
                return result

    def depth_limited_search(self, cube, depth):
        if self.is_solved():
            return [] #This will be the solution path

        if depth == 0:
            return None

        for step in range(1,12):
            if step == 1:
                self.right_vertical_up()
            elif step == 2:
                self.right_vertical_down()
            elif step == 3:
                self.left_vertical_up()
            elif step == 4:
                self.left_vertical_down()
            elif step == 5:
                self.top_horizontal_right()
            elif step == 6:
                self.top_horizontal_left()
            elif step == 7:
                self.bottom_horizontal_right()
            elif step == 8:
                self.bottom_horizontal_left()
            elif step == 9:
                self.front_clockwise()
            elif step == 10:
                self.front_counter_clockwise()
            elif step == 11:
                self.back_clockwise()
            elif step == 12:
                self.back_counter_clockwise()
            
            result = self.depth_limited_search(cube, depth + 1)
            if result is not None:
                return result
    
