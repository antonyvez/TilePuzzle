class Tile:

    def __init__(self, type):
        self.type = type

        # Type:
        # N: NULL (Empty tile)
        # B: Block (Tile that block the user)
        # X: Visited (Tile that has been visited
        # ' ': Empty tile (yet to be visited)

    # Getter for the attribute Type
    def get_type (self):
        return self.type

    # Setter for the attribute Type
    def set_type (self, new_type):
        self.type = new_type
