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

    def set_initial_state(self):
        inputted = False 
        while not inputted:
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

    def set_final_state(self): #test
        final_cube = []
        for corner in Constants.SOLVED_CUBE:
            c1 = corner[0]
            c2 = corner[1]
            c3 = corner[2]
            new_corner = Corner([c1, c2, c3])
            if new_corner.is_valid_corner():
                final_cube.append(new_corner)
        return final_cube  

    def is_solved(self):
        if (self.side_solved(FRONT, 0) and self.side_solved(BACK, 0) and 
            self.side_solved(TOP, 1) and self.side_solved(BOTTOM, 1) and 
            self.side_solved(RIGHT, 2) and self.side_solved(LEFT, 2)):
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

    def move(self, move_corners, move1, move2): #placeholder for above functions
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

    def solve_cube_outer(self):
        for depth_limit in range(1, self.max_depth_limit + 1):
            self.max_depth = depth_limit
            self.memo.clear()
            self.move_set = []
            if self.solve_cube(0):
                return True
        return False

    def solve_cube(self, depth = 0, last_move = None, final_cube = None):
        cube_key = self.cube_state_to_key()

        if cube_key in self.memo and self.memo[cube_key] == depth:
            return False

        if self.is_solved() or cube_key == final_cube.common_keys:
            self.memo[cube_key] = depth
            self.common_keys = True
            return True
        
        if depth >= self.max_depth:
            return False

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

    def reverse_solve_cube(self, depth = 0, last_move = None, cube = None):
        cube_key = self.cube_state_to_key()

        if cube_key in self.memo and self.memo[cube_key] == depth:
            return False

        common_keys = set(self.memo.keys()) & set(cube.memo.keys())

        if common_keys:
            self.common_keys = list(common_keys)[0]
            self.memo[cube_key] = depth
            return True
        
        if depth >= self.max_depth:
            return False

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
    
    def reverse_solve_cube_v2(self, depth = 0, last_move = None):
        cube_key = self.cube_state_to_key()

        if cube_key in self.memo and self.memo[cube_key] == depth:
            return False

        if cube_key == self.common_keys:
            self.memo[cube_key] = depth
            return True
        
        if depth >= self.max_depth:
            return False

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
            case RVU: self.move(RVU_IND, C1, C2)
            case RVD: self.move(RVD_IND, C1, C2)
            case LVU: self.move(LVU_IND, C1, C2)
            case LVD: self.move(LVD_IND, C1, C2)
            case THR: self.move(THR_IND, C1, C3)
            case THL: self.move(THL_IND, C1, C3)
            case BHR: self.move(BHR_IND, C1, C3)
            case BHL: self.move(BHL_IND, C1, C3)
            case FC: self.move(FC_IND, C2, C3)
            case FCC: self.move(FCC_IND, C2, C3)
            case BC: self.move(BC_IND, C2, C3)
            case BCC: self.move(BCC_IND, C2, C3)
            case _: print("Invalid move")

    def undo_move(self, move):
        match move:
            case RVU: self.move(RVD_IND, C1, C2)
            case RVD: self.move(RVU_IND, C1, C2)
            case LVU: self.move(LVD_IND, C1, C2)
            case LVD: self.move(LVU_IND, C1, C2)
            case THR: self.move(THL_IND, C1, C3)
            case THL: self.move(THR_IND, C1, C3)
            case BHR: self.move(BHL_IND, C1, C3)
            case BHL: self.move(BHR_IND, C1, C3)
            case FC: self.move(FCC_IND, C2, C3)
            case FCC: self.move(FC_IND, C2, C3)
            case BC: self.move(BCC_IND, C2, C3)
            case BCC: self.move(BC_IND, C2, C3)
            case _: print("Invalid move")

    def possible_moves(self, last_move=None):
        if last_move:
            return self.prune_moves(last_move)
        return MOVES

    def prune_moves(self, last_move):
        match last_move:
            case RVU: return RVU_MOVES
            case RVD: return RVD_MOVES
            case LVU: return LVU_MOVES
            case LVD: return LVD_MOVES
            case THR: return THR_MOVES
            case THL: return THL_MOVES
            case BHR: return BHR_MOVES
            case BHL: return BHL_MOVES
            case FC: return FC_MOVES
            case FCC: return FCC_MOVES
            case BC: return BC_MOVES
            case BCC: return BCC_MOVES
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
            case RVU: return RVD 
            case RVD: return RVU
            case LVU: return LVD
            case LVD: return LVU
            case THR: return THL
            case THL: return THR
            case BHR: return BHL
            case BHL: return BHR
            case FC: return FCC 
            case FCC: return FC
            case BC: return BCC
            case BCC: return BC