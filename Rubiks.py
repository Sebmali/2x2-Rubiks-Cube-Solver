from Corner import Corner
import Constants
from Constants import SOLVED_CUBE

class Cube:
    def __init__(self):
        self.cube = self.set_initial_state()
        self.max_depth_limit = 15
        self.max_depth = 0
        self.move_set = []
        self.memo = {}
        self.common_keys = False


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

    def print_final_cube(self):
        for corner in self.final_cube:
            print(corner)
   
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
    
        self.swap_first_two(self.cube[0])
        self.swap_first_two(self.cube[3])
        self.swap_first_two(self.cube[4])
        self.swap_first_two(self.cube[7])

        temp_cube0 = self.cube[0]

        self.cube[0] = self.cube[4]
        self.cube[4] = self.cube[7]
        self.cube[7] = self.cube[3]
        self.cube[3] = temp_cube0

  
    def right_vertical_down(self):

        self.swap_first_two(self.cube[0])
        self.swap_first_two(self.cube[3])
        self.swap_first_two(self.cube[4])
        self.swap_first_two(self.cube[7])

        temp_cube0 = self.cube[0]

        self.cube[0] = self.cube[3]
        self.cube[3] = self.cube[7]
        self.cube[7] = self.cube[4]
        self.cube[4] = temp_cube0

 
    def left_vertical_up(self):

        self.swap_first_two(self.cube[1])
        self.swap_first_two(self.cube[2])
        self.swap_first_two(self.cube[5])
        self.swap_first_two(self.cube[6])

        temp_cube0 = self.cube[1]

        self.cube[1] = self.cube[5]
        self.cube[5] = self.cube[6]
        self.cube[6] = self.cube[2]
        self.cube[2] = temp_cube0

    def left_vertical_down(self):

        self.swap_first_two(self.cube[1])
        self.swap_first_two(self.cube[2])
        self.swap_first_two(self.cube[5])
        self.swap_first_two(self.cube[6])

        temp_cube0 = self.cube[1]

        self.cube[1] = self.cube[2]
        self.cube[2] = self.cube[6]
        self.cube[6] = self.cube[5]
        self.cube[5] = temp_cube0

    def top_horizontal_right(self):

        self.swap_first_last(self.cube[0])
        self.swap_first_last(self.cube[1])
        self.swap_first_last(self.cube[2])
        self.swap_first_last(self.cube[3])

        temp_cube0 = self.cube[0]

        self.cube[0] = self.cube[1]
        self.cube[1] = self.cube[2]
        self.cube[2] = self.cube[3]
        self.cube[3] = temp_cube0
    
    def top_horizontal_left(self):

        self.swap_first_last(self.cube[0])
        self.swap_first_last(self.cube[1])
        self.swap_first_last(self.cube[2])
        self.swap_first_last(self.cube[3])

        temp_cube0 = self.cube[0]

        self.cube[0] = self.cube[3]
        self.cube[3] = self.cube[2]
        self.cube[2] = self.cube[1]
        self.cube[1] = temp_cube0

    def bottom_horizontal_right(self):

        self.swap_first_last(self.cube[4])
        self.swap_first_last(self.cube[5])
        self.swap_first_last(self.cube[6])
        self.swap_first_last(self.cube[7])

        temp_cube0 = self.cube[4]

        self.cube[4] = self.cube[5]
        self.cube[5] = self.cube[6]
        self.cube[6] = self.cube[7]
        self.cube[7] = temp_cube0

    def bottom_horizontal_left(self):

        self.swap_first_last(self.cube[4])
        self.swap_first_last(self.cube[5])
        self.swap_first_last(self.cube[6])
        self.swap_first_last(self.cube[7])

        temp_cube0 = self.cube[4]

        self.cube[4] = self.cube[7]
        self.cube[7] = self.cube[6]
        self.cube[6] = self.cube[5]
        self.cube[5] = temp_cube0

    def front_clockwise(self):

        self.swap_last_two(self.cube[0])
        self.swap_last_two(self.cube[1])
        self.swap_last_two(self.cube[4])
        self.swap_last_two(self.cube[5])

        temp_cube0 = self.cube[0]

        self.cube[0] = self.cube[1]
        self.cube[1] = self.cube[5]
        self.cube[5] = self.cube[4]
        self.cube[4] = temp_cube0

    def front_counter_clockwise(self):

        self.swap_last_two(self.cube[0])
        self.swap_last_two(self.cube[1])
        self.swap_last_two(self.cube[4])
        self.swap_last_two(self.cube[5])

        temp_cube0 = self.cube[0]

        self.cube[0] = self.cube[4]
        self.cube[4] = self.cube[5]
        self.cube[5] = self.cube[1]
        self.cube[1] = temp_cube0

    def back_clockwise(self):

        self.swap_last_two(self.cube[2])
        self.swap_last_two(self.cube[3])
        self.swap_last_two(self.cube[6])
        self.swap_last_two(self.cube[7])

        temp_cube0 = self.cube[2]

        self.cube[2] = self.cube[3]
        self.cube[3] = self.cube[7]
        self.cube[7] = self.cube[6]
        self.cube[6] = temp_cube0

    def back_counter_clockwise(self):

        self.swap_last_two(self.cube[2])
        self.swap_last_two(self.cube[3])
        self.swap_last_two(self.cube[6])
        self.swap_last_two(self.cube[7])

        temp_cube0 = self.cube[2]

        self.cube[2] = self.cube[6]
        self.cube[6] = self.cube[7]
        self.cube[7] = self.cube[3]
        self.cube[3] = temp_cube0


    def swap_first_two(self, corner):
        temp = corner.colors[0]
        corner.colors[0] = corner.colors[1]
        corner.colors[1] = temp

    def swap_last_two(self, corner):
        temp = corner.colors[2]
        corner.colors[2] = corner.colors[1]
        corner.colors[1] = temp
    
    def swap_first_last(self, corner):
        temp = corner.colors[0]
        corner.colors[0] = corner.colors[2]
        corner.colors[2] = temp

    def solve_cube_outer(self, final_cube):
        for depth_limit in range(1, self.max_depth_limit + 1):
            self.max_depth = depth_limit
            self.memo.clear()
            self.move_set = []
            if self.solve_cube(0, None):
                #print("Forward works")
                #print("self cube")
                #self.print_cube()
                common_keys = set(self.memo.keys()) & set(final_cube.memo.keys())

                if common_keys:
                    print("Common keys: ", common_keys)
                else:
                    print("No common keys")
                    #print(type(self.memo))
                    print(final_cube.memo)
                return True
            if self.reverse_solve_cube(0, None, final_cube):
                print("Reverse works")
                self.move_set.append(final_cube.move_set)
                return True
        return False

    # The problem is that reverse function returns true first before solve cube does
    # which means that the moves made on the initial cube are not being appened to the move set
    # because the moves are only appened when solve cube returns true
    def solve_cube(self, depth = 0, last_move = None, final_cube = None):
        cube_key = self.cube_state_to_key()
        #print("Depth: ", depth)
        #print("moveset: ", self.move_set)

        if cube_key in self.memo and self.memo[cube_key] == depth:
            #return self.memo[cube_key]
            return False

        # should we add a check here to see if the cube memo key equals the final cube key?
        #common_keys = set(self.memo.keys()) & set(final_cube.memo.keys())
        if self.is_solved() or final_cube.common_keys:
            self.memo[cube_key] = depth
            self.common_keys = True
            return True
        
        if depth >= self.max_depth:
            return False

        solution_found = False
        for move in self.best_move(last_move):
        #self.possible_moves(last_move):
            self.apply_move(move)
            if self.solve_cube(depth + 1, move, final_cube):
                self.move_set.append(move)
                solution_found = True
                print("In solve cube, initial moveset is", self.move_set)
                break
            self.undo_move(move)
        
        if not solution_found:
            self.memo[cube_key] = depth
        return solution_found

    def reverse_solve_cube(self, depth = 0, last_move = None, cube = None):
        # I think we will need the final cube to have it's own memo 
        #print("In reverse solve cube")
        cube_key = self.cube_state_to_key()
        #print("Cube key: ", cube_key)
        #print("Depth: ", depth)
        # apply the move to solved cube

        if cube_key in self.memo and self.memo[cube_key] == depth:
            #return self.memo[cube_key]
            #print("cube key in memo and depth is the same", depth)
            return False

        # we should check if the solved_cube == the current cube, if they are equal then we have solved the cube
        common_keys = set(self.memo.keys()) & set(cube.memo.keys())

        if common_keys:
            self.common_keys = True
            print("Common keys: ", common_keys)
            #print("Initial cube keys: ", cube.memo)
            #print("Final cube keys: ", self.memo)
            #print(cube.move_set)
            self.memo[cube_key] = depth
            return True
        
        if depth >= self.max_depth:
            #print(self.max_depth)
            return False

        solution_found = False
        for move in Constants.MOVES:
        #self.possible_moves(last_move):
            self.apply_move(move)
            #print("After move for final cube")
            #self.print_cube()
            if self.reverse_solve_cube(depth + 1, move, cube):
                self.move_set.append(move)
                solution_found = True
                print("In reverse move, final cube moveset is", self.move_set)
                break
            self.undo_move(move)
        
        if not solution_found:
            #print("Solution not found")
            self.memo[cube_key] = depth
        return solution_found
    
    def apply_rem_moves(self, move_set):
        for move in move_set:
            self.apply_move(move)

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
    
    def cube_state_to_key(self):
        key = '|'.join(''.join(corner.colors) for corner in self.cube)
        return key

    def best_move(self, last_move=None):
        best_moves = []
        for move in self.possible_moves(last_move):
            self.apply_move(move)
            new_percent = self.percent_solved()
            best_moves.append((move, new_percent))  # Store both move and its result

            self.undo_move(move)
        #print("best moves: ", best_moves)
        # Sort the moves based on the percentage solved, in descending order
        best_moves.sort(key=lambda x: x[1], reverse=True)
        sorted_moves = [move[0] for move in best_moves]
        return sorted_moves

    def percent_solved(self):
        self.percent_complete = (self.percent_of_front_solved() + self.percent_of_back_solved() + self.percent_of_top_solved() + self.percent_of_bottom_solved() + self.percent_of_right_solved() + self.percent_of_left_solved()) / 6
        return (self.percent_complete)
    
    # Helper function to calculate the % of each side that is solved
    def percent_of_front_solved(self):
        # This will be the function that checks if the front side is solved
        front_count = 0
        if self.cube[0].colors[0] == self.cube[1].colors[0]:
            front_count += 1
        if self.cube[0].colors[0] == self.cube[4].colors[0]:
            front_count += 1
        if self.cube[0].colors[0] == self.cube[5].colors[0]:
            front_count += 1
        if self.cube[1].colors[0] == self.cube[4].colors[0]:
            front_count += 1
        if self.cube[1].colors[0] == self.cube[5].colors[0]:
            front_count += 1
        if self.cube[4].colors[0] == self.cube[5].colors[0]:
            front_count += 1
        
        if front_count == 1:
            front_count += 1
        elif front_count > 3:
            front_count = 4
        else:
            #print("Front count: ", str(front_count), "Front %: ", str((front_count / 4) * 100))
            return (front_count / 4) * 100
        
        #print("Front count: ", str(front_count), "Front %: ", str((front_count / 4) * 100))
        return (front_count / 4) * 100
    
    def percent_of_back_solved(self):
        # This will be the function that checks if the back side is solved
        back_count = 0
        if self.cube[2].colors[0] == self.cube[3].colors[0]:
            back_count += 1
        if self.cube[2].colors[0] == self.cube[6].colors[0]:
            back_count += 1
        if self.cube[2].colors[0] == self.cube[7].colors[0]:
            back_count += 1
        if self.cube[3].colors[0] == self.cube[6].colors[0]:
            back_count += 1
        if self.cube[3].colors[0] == self.cube[7].colors[0]:
            back_count += 1
        if self.cube[6].colors[0] == self.cube[7].colors[0]:
            back_count += 1
        
        if back_count == 1:
            back_count += 1
        elif back_count > 3:
            back_count = 4
        else:
            #print("Back count: ", str(back_count), "Back %: ", str((back_count / 4) * 100))
            return (back_count / 4) * 100
        
        #print("Back count: ", str(back_count), "Back %: ", str((back_count / 4) * 100))
        return (back_count / 4) * 100
    
    def percent_of_top_solved(self):
        # This will be the function that checks if the top side is solved
        top_count = 0
        if self.cube[0].colors[1] == self.cube[1].colors[1]:
            top_count += 1
        if self.cube[0].colors[1] == self.cube[2].colors[1]:
            top_count += 1
        if self.cube[0].colors[1] == self.cube[3].colors[1]:
            top_count += 1
        if self.cube[1].colors[1] == self.cube[2].colors[1]:
            top_count += 1
        if self.cube[1].colors[1] == self.cube[3].colors[1]:
            top_count += 1
        if self.cube[2].colors[1] == self.cube[3].colors[1]:
            top_count += 1
        
        if top_count == 1:
            top_count += 1
        elif top_count > 3:
            top_count = 4
        else:
            #print("Top count: ", str(top_count), "Top %: ", str((top_count / 4) * 100))
            return (top_count / 4) * 100
        
        #print("Top count: ", str(top_count), "Top %: ", str((top_count / 4) * 100))
        return (top_count / 4) * 100
    
    def percent_of_bottom_solved(self):
        # This will be the function that checks if the bottom side is solved
        bottom_count = 0
        if self.cube[4].colors[1] == self.cube[5].colors[1]:
            bottom_count += 1
        if self.cube[4].colors[1] == self.cube[6].colors[1]:
            bottom_count += 1
        if self.cube[4].colors[1] == self.cube[7].colors[1]:
            bottom_count += 1
        if self.cube[5].colors[1] == self.cube[6].colors[1]:
            bottom_count += 1
        if self.cube[5].colors[1] == self.cube[7].colors[1]:
            bottom_count += 1
        if self.cube[6].colors[1] == self.cube[7].colors[1]:
            bottom_count += 1
        
        if bottom_count == 1:
            bottom_count += 1
        elif bottom_count > 3:
            bottom_count = 4
        else:
            #print("Bottom count: ", str(bottom_count), "Bottom %: ", str((bottom_count / 4) * 100))
            return (bottom_count / 4) * 100
        
        #print("Bottom count: ", str(bottom_count), "Bottom %: ", str((bottom_count / 4) * 100))
        return (bottom_count / 4) * 100
    
    def percent_of_right_solved(self):
        right_count = 0
        if self.cube[0].colors[2] == self.cube[3].colors[2]:
            right_count += 1
        if self.cube[0].colors[2] == self.cube[4].colors[2]:
            right_count += 1
        if self.cube[0].colors[2] == self.cube[7].colors[2]:
            right_count += 1
        if self.cube[3].colors[2] == self.cube[4].colors[2]:
            right_count += 1
        if self.cube[3].colors[2] == self.cube[7].colors[2]:
            right_count += 1
        if self.cube[4].colors[2] == self.cube[7].colors[2]:
            right_count += 1
            
        if right_count == 1:
            right_count += 1
        elif right_count > 3:
            right_count = 4
        else:
            #print("Right count: ", str(right_count), "Right %: ", str((right_count / 4) * 100))
            return (right_count / 4) * 100
        
        #print("Right count: ", str(right_count), "Right %: ", str((right_count / 4) * 100))
        return (right_count / 4) * 100
    
    def percent_of_left_solved(self):
        
        left_count = 0
        if self.cube[1].colors[2] == self.cube[2].colors[2]:
            left_count += 1
        if self.cube[1].colors[2] == self.cube[5].colors[2]:
            left_count += 1
        if self.cube[1].colors[2] == self.cube[6].colors[2]:
            left_count += 1
        if self.cube[2].colors[2] == self.cube[5].colors[2]:
            left_count += 1
        if self.cube[2].colors[2] == self.cube[6].colors[2]:
            left_count += 1
        if self.cube[5].colors[2] == self.cube[6].colors[2]:
            left_count += 1
        
        if left_count == 1:
            left_count += 1
        elif left_count > 3:
            left_count = 4
        else:
            #print("Left count: ", str(left_count), "Left %: ", str((left_count / 4) * 100))
            return (left_count / 4) * 100
        
        #print("Left count: ", str(left_count), "Left %: ", str((left_count / 4) * 100))
        return (left_count / 4) * 100
    
