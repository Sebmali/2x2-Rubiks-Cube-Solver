"""
Rubiks.py
Purpose: This file contains the Cube class which is used to represent the Rubik's Cube. 
It contains methods to solve the cube and manipulate the cube.
Authors: Sebastian Maliczewski, Shayne Prakash
"""

from Corner import Corner
import Constants
from Constants import *

class Cube:
    def __init__(self, final = False):
        if final:
            self.cube = self.set_final_state()
        else:
            self.cube = self.set_initial_state()
        self.final_cube = self.set_final_state() #test
        self.max_depth_limit = 15
        self.max_depth = 0
        self.move_set = []
        self.final_move_set = []
        self.memo = {}
        self.common_keys = None

    #Sets the initial state of the cube based on user input
    def set_initial_state(self):
        inputted = False 
        while not inputted:
            print("Would you like to input a file ? (Y/N)")
            corners = []
            choice = input().strip().upper()
            if choice == "Y":
                print("Enter the file name: ")
                file_name = input().strip()
                try: 
                    with open(file_name, "r") as file:
                        for line in file:
                            corner_colors = line.strip().upper().split()
                            corner_combo = Corner(corner_colors)
                            if corner_combo.is_valid_corner():
                                corners.append(Corner(corner_colors))
                            else:
                                print("Invalid corner colors. Please try again.")
                                break
                except FileNotFoundError:
                    print("File not found. Please try again.")
                    continue
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
            if(self.check_initial_cube(corners)):
                inputted = True
        return corners

    def check_initial_cube(self, cube):
        colorCount = {color: 0 for color in COLORS}
        for corner in cube:
            if corner.colors not in INITIAL_POSSIBILITIES:
                return False
            for color in corner.colors:
                colorCount[color] += 1
                if colorCount[color] > 4:
                    return False     
        return True

    def set_final_state(self): 
        final_cube = []
        for corner in Constants.SOLVED_CUBE:
            c1 = corner[0]
            c2 = corner[1]
            c3 = corner[2]
            new_corner = Corner([c1, c2, c3])
            if new_corner.is_valid_corner():
                final_cube.append(new_corner)
        return final_cube  

    def get_color(self, index, color_index):
        return self.cube[index].colors[color_index]

    def is_solved(self, key):
        if key == "365465461361325425421321":
            return True
        return False

    def side_solved(self, indices, color_index):
        return len(set(self.cube[i].colors[color_index] for i in indices)) == 1
 
    def print_cube(self):
        for corner in self.cube:
            print(corner.colors)

    def print_final_cube(self):
        for corner in self.final_cube:
            print(corner.colors)

    def move(self, move_corners, move1, move2): 
        for index in move_corners:
            self.swap_colors(self.cube[index], move1, move2)
        temp_cube0 = self.cube[move_corners[0]]
        self.cube[move_corners[0]] = self.cube[move_corners[1]]
        self.cube[move_corners[1]] = self.cube[move_corners[2]]
        self.cube[move_corners[2]] = self.cube[move_corners[3]]
        self.cube[move_corners[3]] = temp_cube0    

    def swap_colors(self, corner, c1, c2):
        temp = corner.colors[c1]
        corner.colors[c1] = corner.colors[c2]
        corner.colors[c2] = temp

    #Function to solve the initial cube
    def solve_cube(self, depth = 0, last_move = None, final_cube = None):
        if depth >= self.max_depth:
            return False

        cube_key = self.cube_state_to_key()

        if cube_key in self.memo and self.memo[cube_key] == depth:
            return False

        if self.is_solved(cube_key) or cube_key == final_cube.common_keys:
            self.memo[cube_key] = depth
            self.common_keys = True
            return True

        solution_found = False
        for move in self.possible_moves(last_move):
            self.apply_move(move)
            if self.solve_cube(depth + 1, move, final_cube):
                self.move_set.append(move)
                solution_found = True
                break
            self.undo_move(move)
        
        if not solution_found:
            self.memo[cube_key] = depth
        return solution_found

    #Function to solve the final cube checking for common keys.
    def reverse_solve_cube(self, depth = 0, last_move = None, cube = None):
        if depth >= self.max_depth:
            return False

        cube_key = self.cube_state_to_key()

        if cube_key in self.memo and self.memo[cube_key] == depth:
            return False

        if cube_key in cube.memo:
            self.common_keys = cube_key
            self.memo[cube_key] = depth
            return True

        solution_found = False
        for move in self.possible_moves(last_move):
            self.apply_move(move)
            if self.reverse_solve_cube(depth + 1, move, cube):
                self.move_set.append(move)
                solution_found = True
                break
            self.undo_move(move)
        
        if not solution_found:
            self.memo[cube_key] = depth
        return solution_found
    
    #Function to get the final moveset when a solution is finally found. 
    def reverse_solve_cube_v2(self, depth = 0, last_move = None):
        if depth >= self.max_depth:
            return False
        
        cube_key = self.cube_state_to_key()

        if cube_key in self.memo and self.memo[cube_key] == depth:
            return False

        if cube_key == self.common_keys:
            self.memo[cube_key] = depth
            return True

        solution_found = False
        for move in self.possible_moves(last_move):
            self.apply_move(move)
            if self.reverse_solve_cube_v2(depth + 1, move):
                self.move_set.append(move)
                solution_found = True
                break
            self.undo_move(move)
        
        if not solution_found:
            self.memo[cube_key] = depth
        return solution_found
    
    def apply_rem_moves(self, move_set):
        for move in move_set:
            revised_move = self.convert_move(move)
            self.apply_move(revised_move)
            self.move_set.append(revised_move)

    def apply_move(self, move):
        match move:
            case Constants.RVU: self.move(RVU_IND, C1, C2)
            case Constants.RVD: self.move(RVD_IND, C1, C2)
            case Constants.LVU: self.move(LVU_IND, C1, C2)
            case Constants.LVD: self.move(LVD_IND, C1, C2)
            case Constants.THR: self.move(THR_IND, C1, C3)
            case Constants.THL: self.move(THL_IND, C1, C3)
            case Constants.BHR: self.move(BHR_IND, C1, C3)
            case Constants.BHL: self.move(BHL_IND, C1, C3)
            case Constants.FC: self.move(FC_IND, C2, C3)
            case Constants.FCC: self.move(FCC_IND, C2, C3)
            case Constants.BC: self.move(BC_IND, C2, C3)
            case Constants.BCC: self.move(BCC_IND, C2, C3)
            case _: print("Invalid move")

    def undo_move(self, move):
        match move:
            case Constants.RVU: self.move(RVD_IND, C1, C2)
            case Constants.RVD: self.move(RVU_IND, C1, C2)
            case Constants.LVU: self.move(LVD_IND, C1, C2)
            case Constants.LVD: self.move(LVU_IND, C1, C2)
            case Constants.THR: self.move(THL_IND, C1, C3)
            case Constants.THL: self.move(THR_IND, C1, C3)
            case Constants.BHR: self.move(BHL_IND, C1, C3)
            case Constants.BHL: self.move(BHR_IND, C1, C3)
            case Constants.FC: self.move(FCC_IND, C2, C3)
            case Constants.FCC: self.move(FC_IND, C2, C3)
            case Constants.BC: self.move(BCC_IND, C2, C3)
            case Constants.BCC: self.move(BC_IND, C2, C3)
            case _: print("Invalid move")

    def possible_moves(self, last_move=None):
        if last_move:
            return self.prune_moves(last_move)
        return MOVES

    def prune_moves(self, last_move):
        match last_move:
            case Constants.RVU: return RVU_MOVES
            case Constants.RVD: return RVD_MOVES
            case Constants.LVU: return LVU_MOVES
            case Constants.LVD: return LVD_MOVES
            case Constants.THR: return THR_MOVES
            case Constants.THL: return THL_MOVES
            case Constants.BHR: return BHR_MOVES
            case Constants.BHL: return BHL_MOVES
            case Constants.FC: return FC_MOVES
            case Constants.FCC: return FCC_MOVES
            case Constants.BC: return BC_MOVES
            case Constants.BCC: return BCC_MOVES
            case _: return []
    
    def cube_state_to_key(self):
        key_dict = {}
        position = 1
        key = "" 
        for corner in self.cube:
            for color in corner.colors:
                if color not in key_dict:
                    key_dict[color] = position
                    position += 1
                key += str(key_dict[color])

        return key

    def convert_move(self, move):
        match move:
            case Constants.RVU: return RVD 
            case Constants.RVD: return RVU
            case Constants.LVU: return LVD
            case Constants.LVD: return LVU
            case Constants.THR: return THL
            case Constants.THL: return THR
            case Constants.BHR: return BHL
            case Constants.BHL: return BHR
            case Constants.FC: return FCC 
            case Constants.FCC: return FC
            case Constants.BC: return BCC
            case Constants.BCC: return BC