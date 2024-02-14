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
MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
RVU_MOVES = [RVU, LVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
RVD_MOVES = [RVD, LVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
LVU_MOVES = [RVU, RVD, LVU, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
LVD_MOVES = [RVU, RVD, LVD, THR, THL, BHR, BHL, FC, FCC, BC, BCC]
THR_MOVES = [RVU, RVD, LVU, LVD, THR, BHR, BHL, FC, FCC, BC, BCC]
THL_MOVES = [RVU, RVD, LVU, LVD, THL, BHR, BHL, FC, FCC, BC, BCC]
BHR_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, FC, FCC, BC, BCC]
BHL_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHL, FC, FCC, BC, BCC]
FC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, BC, BCC]
FCC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FCC, BC, BCC]
BC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, FCC, BC]
BCC_MOVES = [RVU, RVD, LVU, LVD, THR, THL, BHR, BHL, FC, FCC, BCC]

SOLVED_CUBE = [["R", "W", "B"],
               ["R", "W", "G"],
               ["O", "W", "G"],
               ["O", "W", "B"],
               ["R", "Y", "B"],
               ["R", "Y", "G"],
               ["O", "Y", "G"],
               ["O", "Y", "B"]]
