CORNERS = ["Front-Right-Top", "Front-Left-Top", "Back-Left-Top", "Back-Right-Top", 
           "Front-Right-Bottom", "Front-Left-Bottom", "Back-Left-Bottom", "Back-Right-Bottom"]
COLORS = ["W", "G", "R", "B", "O", "Y"]
RVU = "right_vertical_up"
RVD = "right_vertical_down"
LVU = "left_vertical_up"
LVD = "left_vertical_down"
THR = "top_horizontal_right"
THL = "top_horizontal_left"
BHR = "bottom_horizontal_right"
BHL = "bottom_horizontal_left"
FC = "front_clockwise"
FCC = "front_counter_clockwise"
BC = "back_clockwise"
BCC = "back_counter_clockwise"

# All possible moves
MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
RVU_MOVES = [RVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
RVD_MOVES = [RVD, LVU, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
LVU_MOVES = [RVD, LVU, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
LVD_MOVES = [RVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
THR_MOVES = [RVU, RVD, LVU, LVD, THR, BHL, FC, FCC, BC, BCC]
THL_MOVES = [RVU, RVD, LVU, LVD, THL, BHR, FC, FCC, BC, BCC]
BHR_MOVES = [RVU, RVD, LVU, LVD, THL, BHR, FC, FCC, BC, BCC]
BHL_MOVES = [RVU, RVD, LVU, LVD, THR, BHL, FC, FCC, BC, BCC]
FC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, BCC]
FCC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FCC, BC]
BC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FCC, BC]
BCC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, BCC]

SOLVED_CUBE = [['R','W','B'],['R','W','G'],['O','W','G'],['O','W','B'],
                ['R','Y','B'],['R','Y','G'],['O','Y','G'],['O','Y','B']]

#Corner indices for each move
RVU_IND = [0, 4, 7, 3]
RVD_IND = [0, 3, 7, 4]
LVU_IND = [1, 5, 6, 2]
LVD_IND = [1, 2, 6, 5]
THR_IND = [0, 1, 2, 3]
THL_IND = [0, 3, 2, 1]
BHR_IND = [4, 5, 6, 7]
BHL_IND = [4, 7, 6, 5]
FC_IND = [0, 1, 5, 4]
FCC_IND = [0, 4, 5, 1]
BC_IND = [2, 6, 7, 3]
BCC_IND = [2, 3, 7, 6]

#Color Indeces 1,2,3 in a corner
C1 = 0
C2 = 1
C3 = 2

#Face indices for solving check
FRONT = [0, 1, 4, 5] 
BACK = [2, 3, 6, 7]
TOP = [0, 1, 2, 3]
BOTTOM = [4, 5, 6, 7]
RIGHT = [0, 3, 4, 7]
LEFT = [1, 2, 5, 6]

#All possible corner orientations to check for correct initial cube
INITIAL_POSSIBILITIES = [['W','O','B'], ['W','B','O'], ['O','W','B'], ['O','B','W'], ['B','W','O'], ['B','O','W'],
                         ['W','O','G'], ['W','G','O'], ['O','W','G'], ['O','G','W'], ['G','W','O'], ['G','O','W'],
                         ['W','R','G'], ['W','G','R'], ['R','W','G'], ['R','G','W'], ['G','W','R'], ['G','R','W'],
                         ['W','R','B'], ['W','B','R'], ['R','W','B'], ['R','B','W'], ['B','W','R'], ['B','R','W'],
                         ['Y','O','B'], ['Y','B','O'], ['O','Y','B'], ['O','B','Y'], ['B','Y','O'], ['B','O','Y'],
                         ['Y','O','G'], ['Y','G','O'], ['O','Y','G'], ['O','G','Y'], ['G','Y','O'], ['G','O','Y'],
                         ['Y','R','G'], ['Y','G','R'], ['R','Y','G'], ['R','G','Y'], ['G','Y','R'], ['G','R','Y'],
                         ['Y','R','B'], ['Y','B','R'], ['R','Y','B'], ['R','B','Y'], ['B','Y','R'], ['B','R','Y']]
