class Tile:

    def __init__(self, type, switch_tiles=[]):
        self.type = type
        self.switch_tiles = switch_tiles

        # Type:
        # N: NULL (Empty tile)
        # B: Block (Tile that block the user)
        # X: Visited (Tile that has been visited
        # I: Switch that will unblock a serie of tile
        # ' ': Empty tile (yet to be visited)

    # Getter for the attribute Type
    def get_type (self):
        return self.type

    # Getter for the list of tile that are unblocked by the switch
    def get_switch_tiles (self):
        return self.switch_tiles

    # Setter for the attribute Type
    def set_type (self, new_type):
        self.type = new_type

    # Setter for the attribute Switch_Tile
    def set_switch_tiles (self, new_switch_tiles):
        self.switch_tiles = new_switch_tiles
