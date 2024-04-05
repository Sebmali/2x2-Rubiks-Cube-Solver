"""
Corner.py
Purpose: This file contains the Corner class which is used to represent the corners
of the Rubiks Cube. This class is used to represent the colors of the corner as well. 
Authors: Sebastian Maliczewski, Shayne Prakash
"""
COLORS = ["W", "G", "R", "B", "O", "Y"]

class Corner:
    def __init__(self, colors):
        self.colors = colors

    def is_valid_corner(self):
        if len(self.colors) != 3:
            return False

        if not all(color in COLORS for color in self.colors):
            return False

        return True
