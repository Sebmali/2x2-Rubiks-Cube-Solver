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
        # This will be the function that checks if the right side is solved
        if self.cube[0].colors[2] == self.cube[3].colors[2] == self.cube[4].colors[2] == self.cube[7].colors[2]:
            return True
    
        return False
    
    def left_side_solved(self):
        # This will be the function that checks if the left side is solved
        if self.cube[1].colors[2] == self.cube[2].colors[2] == self.cube[5].colors[2] == self.cube[6].colors[2]:
            return True
    
        return False

    """    
    def print_front_side(self):
        # This will be the function that prints the front side
        print(self.cube[0].colors[0] + " " + self.cube[1].colors[0])
        print(self.cube[4].colors[0] + " " + self.cube[5].colors[0])
    """
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

#These are the 12 possible steps that are available at each step of the search. 

   #CORNERS = ["Front-Right-Top", "Front-Left-Top", "Back-Left-Top", "Back-Right-Top", "Front-Right-Bottom", "Front-Left-Bottom", "Back-Left-Bottom", "Back-Right-Bottom"]

#These are the 12 possible steps that are available at each step of the search. 


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

        #do we need to return the new cube? or is it pass by ref

        return True
    
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

        return True
    
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
        
        return True

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
        
        return True

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
        
        return True

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
        
        return True

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
        
        return True

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
        
        return True

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
        
        return True    

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
        
        return True

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
        
        return True

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
        
        return True

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
    

