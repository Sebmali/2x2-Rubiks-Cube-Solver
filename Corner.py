COLORS = ["W", "G", "R", "B", "O", "Y"]
VALID_COMBINATIONS = [
    #This will be where the valid combinations go if this is the route we take.
]

class Corner:
    def __init__(self, colors):
        self.colors = colors

    def is_valid_corner(self):
        if len(self.colors) != 3:
            return False

        if not all(color in COLORS for color in self.colors):
            return False

        return self.is_valid_combination(self.colors)

    def is_valid_combination(self, corner_colors):
        # Will need to implement something to check if the combination is valid based on orientation and color comibanations
        return True
