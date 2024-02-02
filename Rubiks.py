from Corner import Corner
import Constants

class Cube:
    def __init__(self):
        self.cube = self.set_initial_state()
        self.max_depth_limit = 10
        self.max_depth = 0
        self.move_set = []

    def is_solved(self):
        #Create 6 functions that check if each side is solved
        if self.front_side_solved() and self.back_side_solved() and self.top_side_solved() and self.bottom_side_solved() and self.right_side_solved() and self.left_side_solved():
            return True
        return False

    def front_side_solved(self):
        # This will be the function that checks if the front side is solved
        if self.cube[0].colors[0] == self.cube[1].colors[0] == self.cube[4].colors[0] == self.cube[5].colors[0]:
            return True
        return False
    
    def back_side_solved(self):
        # This will be the function that checks if the back side is solved
        if self.cube[2].colors[0] == self.cube[3].colors[0] == self.cube[6].colors[0] == self.cube[7].colors[0]:
            return True
        return False
    
    def top_side_solved(self):
        # This will be the function that checks if the top side is solved
        if self.cube[0].colors[1] == self.cube[1].colors[1] == self.cube[2].colors[1] == self.cube[3].colors[1]:
            return True
        return False
    
    def bottom_side_solved(self):
        # This will be the function that checks if the bottom side is solved
        if self.cube[4].colors[1] == self.cube[5].colors[1] == self.cube[6].colors[1] == self.cube[7].colors[1]:
            return True
        return False
    
    def right_side_solved(self):
        if self.cube[0].colors[2] == self.cube[3].colors[2] == self.cube[4].colors[2] == self.cube[7].colors[2]:
            return True  
        return False
    
    def left_side_solved(self):
        if self.cube[1].colors[2] == self.cube[2].colors[2] == self.cube[5].colors[2] == self.cube[6].colors[2]:
            return True
        return False

    def get_corner(self, corner):
        return self.cube[corner]

    def set_corner(self, corner, colors):
        self.cube[corner] = Corner(colors)
    
    def set_initial_state(self):
        print("Would you like to input a file ? (Y/N)")
        corners = []

        choice = input().strip().upper()

        if choice == "Y":
            print("Enter the file name: ")
            file_name = input().strip()
            with open(file_name, "r") as file:
                for line in file:
                    corner_colors = line.strip().upper().split()
                    corner_combo = Corner(corner_colors)
                    if corner_combo.is_valid_corner():
                        corners.append(Corner(corner_colors))
                    else:
                        print("Invalid corner colors. Please try again.")
                        break
            return corners
        else:
        
            print("Enter the colors of each corner on the cube.")
            print("Use W for White, G for Green, R for Red, B for Blue, O for Orange, and Y for Yellow.")
            print("Ensure to keep mind of the front of the cube at all points.")
            print("Enter the colors in the format: Color1 Color2 Color3")
    

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

    def right_vertical_up(self):
        # This will be the function that rotates the right vertical up
        # FBR -> FTR, FTR -> BTR, BBR -> FBR and BTR -> BBR with each corners first two elements swaping, so [R, G, B] -> [G, R, B]

        #temp for a single corner in order to swap 
        temp_FTR = self.cube[0]
        temp_BTR = self.cube[3]
        temp_FBR = self.cube[4]
        temp_BBR = self.cube[7]

        # I want to first swap the appropriate corners then swap the necessary colors
        #create a swap function for corner that swaps the colors and returns a new corner
        self.cube[0] = self.swap_first_two(temp_FBR) # we would send self.cube[4] through the swap function 
        self.cube[3] = self.swap_first_two(temp_FTR) # swap
        self.cube[4] = self.swap_first_two(temp_BBR) # swap
        self.cube[7] = self.swap_first_two(temp_BTR) # swap
  
    def right_vertical_down(self):
        # This will be the function that rotates the right vertical down
        
        temp_FTR = self.cube[0]
        temp_BTR = self.cube[3]
        temp_FBR = self.cube[4]
        temp_BBR = self.cube[7]

        self.cube[0] = self.swap_first_two(temp_BTR) 
        self.cube[3] = self.swap_first_two(temp_BBR) 
        self.cube[4] = self.swap_first_two(temp_FTR)
        self.cube[7] = self.swap_first_two(temp_FBR)
 
    def left_vertical_up(self):
        # This will be the function that rotates the left vertical up
        
        temp_FTL = self.cube[1]
        temp_BTL = self.cube[2]
        temp_FBL = self.cube[5]
        temp_BBL = self.cube[6]

        self.cube[1] = self.swap_first_two(temp_FBL) 
        self.cube[2] = self.swap_first_two(temp_FTL)
        self.cube[5] = self.swap_first_two(temp_BBL)
        self.cube[6] = self.swap_first_two(temp_BTL)

    def left_vertical_down(self):
        # This will be the function that rotates the left vertical down
        
        temp_FTL = self.cube[1]
        temp_BTL = self.cube[2]
        temp_FBL = self.cube[5]
        temp_BBL = self.cube[6]

        self.cube[1] = self.swap_first_two(temp_BTL)
        self.cube[2] = self.swap_first_two(temp_BBL)
        self.cube[5] = self.swap_first_two(temp_FTL)
        self.cube[6] = self.swap_first_two(temp_FBL)

    def top_horizontal_right(self):
        # This will be the function that rotates the top horizontal right
        
        temp_FTR = self.cube[0]
        temp_FTL = self.cube[1]
        temp_BTL = self.cube[2]
        temp_BTR = self.cube[3]

        self.cube[0] = self.swap_first_last(temp_FTL) 
        self.cube[1] = self.swap_first_last(temp_BTL)
        self.cube[2] = self.swap_first_last(temp_BTR)
        self.cube[3] = self.swap_first_last(temp_FTR)
    
    def top_horizontal_left(self):
        # This will be the function that rotates the top horizontal left
        
        temp_FTR = self.cube[0]
        temp_FTL = self.cube[1]
        temp_BTL = self.cube[2]
        temp_BTR = self.cube[3]

        self.cube[0] = self.swap_first_last(temp_BTR) 
        self.cube[1] = self.swap_first_last(temp_FTR)
        self.cube[2] = self.swap_first_last(temp_FTL)
        self.cube[3] = self.swap_first_last(temp_BTL)

    def bottom_horizontal_right(self):
        # This will be the function that rotates the bottom horizontal right
        
        temp_FBR = self.cube[4]
        temp_FBL = self.cube[5]
        temp_BBL = self.cube[6]
        temp_BBR = self.cube[7]

        self.cube[4] = self.swap_first_last(temp_FBL) 
        self.cube[5] = self.swap_first_last(temp_BBL)
        self.cube[6] = self.swap_first_last(temp_BBR)
        self.cube[7] = self.swap_first_last(temp_FBR)

    def bottom_horizontal_left(self):
        # This will be the function that rotates the bottom horizontal left
        
        temp_FBR = self.cube[4]
        temp_FBL = self.cube[5]
        temp_BBL = self.cube[6]
        temp_BBR = self.cube[7]
        

        self.cube[4] = self.swap_first_last(temp_BBR)
        self.cube[5] = self.swap_first_last(temp_FBR)
        self.cube[6] = self.swap_first_last(temp_FBL)
        self.cube[7] = self.swap_first_last(temp_BBL)

    def front_clockwise(self):
        # This will be the function that rotates the front clockwise
        
        temp_FTR = self.cube[0]
        temp_FTL = self.cube[1]
        temp_FBL = self.cube[5]
        temp_FBR = self.cube[4]

        self.cube[0] = self.swap_last_two(temp_FTL)
        self.cube[1] = self.swap_last_two(temp_FBL)
        self.cube[4] = self.swap_last_two(temp_FTR)
        self.cube[5] = self.swap_last_two(temp_FBR)

    def front_counter_clockwise(self):
        # This will be the function that rotates the front counter clockwise
        
        temp_FTR = self.cube[0]
        temp_FTL = self.cube[1]
        temp_FBL = self.cube[5]
        temp_FBR = self.cube[4]

        self.cube[0] = self.swap_last_two(temp_FBR)
        self.cube[1] = self.swap_last_two(temp_FTR)
        self.cube[4] = self.swap_last_two(temp_FBL)
        self.cube[5] = self.swap_last_two(temp_FTL)

    def back_clockwise(self):
        # This will be the function that rotates the back clockwise
        
        temp_BTL = self.cube[2]
        temp_BTR = self.cube[3]
        temp_BBR = self.cube[7]
        temp_BBL = self.cube[6]

        self.cube[2] = self.swap_last_two(temp_BBL)
        self.cube[3] = self.swap_last_two(temp_BTL)
        self.cube[6] = self.swap_last_two(temp_BBR)
        self.cube[7] = self.swap_last_two(temp_BTR)

    def back_counter_clockwise(self):
        # This will be the function that rotates the back counter clockwise
        
        temp_BTL = self.cube[2]
        temp_BTR = self.cube[3]
        temp_BBR = self.cube[7]
        temp_BBL = self.cube[6]

        self.cube[2] = self.swap_last_two(temp_BTR)
        self.cube[3] = self.swap_last_two(temp_BBR)
        self.cube[6] = self.swap_last_two(temp_BTL)
        self.cube[7] = self.swap_last_two(temp_BBL)

    def swap_first_two(self, corner):
        temp = corner.colors[0]
        corner.colors[0] = corner.colors[1]
        corner.colors[1] = temp

        return corner

    def swap_last_two(self, corner):
        temp = corner.colors[2]
        corner.colors[2] = corner.colors[1]
        corner.colors[1] = temp

        return corner
    
    def swap_first_last(self, corner):
        temp = corner.colors[0]
        corner.colors[0] = corner.colors[2]
        corner.colors[2] = temp

        return corner

    def solve_cube_outer(self):
        for depth_limit in range(1, self.max_depth_limit + 1):
            self.max_depth = depth_limit
            self.move_set = []
            if self.solve_cube(0):
                return True
        return False

    def solve_cube(self, depth = 0, last_move = None):
        if self.is_solved():
            return True
        
        if depth >= self.max_depth:
            return False

        for move in self.possible_moves(last_move):
            self.apply_move(move)
            print("Depth: ", depth)
            if self.solve_cube(depth + 1, move):
                self.move_set.append(move)
                return True
            self.undo_move(move)
        
        return False

    def apply_move(self, move):
        match move:
            case Constants.RVU: self.right_vertical_up()
            case Constants.RVD: self.right_vertical_down()
            case Constants.LVU: self.left_vertical_up()
            case Constants.LVD: self.left_vertical_down()
            case Constants.THR: self.top_horizontal_right()
            case Constants.THL: self.top_horizontal_left()
            case Constants.BHR: self.bottom_horizontal_right()
            case Constants.BHL: self.bottom_horizontal_left()
            case Constants.FC: self.front_clockwise()
            case Constants.FCC: self.front_counter_clockwise()
            case Constants.BC: self.back_clockwise()
            case Constants.BCC: self.back_counter_clockwise()
            case _: print("Invalid move")

    def undo_move(self, move):
        match move:
            case Constants.RVU: self.right_vertical_down()
            case Constants.RVD: self.right_vertical_up()
            case Constants.LVU: self.left_vertical_down()
            case Constants.LVD: self.left_vertical_up()
            case Constants.THR: self.top_horizontal_left()
            case Constants.THL: self.top_horizontal_right()
            case Constants.BHR: self.bottom_horizontal_left()
            case Constants.BHL: self.bottom_horizontal_right()
            case Constants.FC: self.front_counter_clockwise()
            case Constants.FCC: self.front_clockwise()
            case Constants.BC: self.back_counter_clockwise()
            case Constants.BCC: self.back_clockwise()
            case _: print("Invalid move")

    def possible_moves(self, last_move=None):
        if last_move:
            return self.prune_moves(last_move)
        return Constants.MOVES

    def prune_moves(self, last_move):
        match last_move:
            case Constants.RVU: return Constants.RVU_MOVES
            case Constants.RVD: return Constants.RVD_MOVES
            case Constants.LVU: return Constants.LVU_MOVES
            case Constants.LVD: return Constants.LVD_MOVES
            case Constants.THR: return Constants.THR_MOVES
            case Constants.THL: return Constants.THL_MOVES
            case Constants.BHR: return Constants.BHR_MOVES
            case Constants.BHL: return Constants.BHL_MOVES
            case Constants.FC: return Constants.FC_MOVES
            case Constants.FCC: return Constants.FCC_MOVES
            case Constants.BC: return Constants.BC_MOVES
            case Constants.BCC: return Constants.BCC_MOVES
            case _: return []
    

