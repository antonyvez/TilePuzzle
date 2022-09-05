from Tile import Tile


class Grid:

    def __init__(self, setup):
        #Setup: [length, height, (player_position), [((tile1_x,tile1_y], type)]
        #        [3, 4, (3, 1), [((0, 0), N), ((0, 1),), ((0, 2),), ...]
        # Create a 2D table with tile
        self.grid = [[Tile(' ') for x in range(setup[0])] for y in range(setup[1])]

        # Fill the grid according to the setup
        #Array as: [(x,y),type], ex [((0,0),N)]
        for tile in setup[3]:
            self.grid[tile[0][0]][tile[0][1]].set_type(tile[1])
            if len(tile) >= 3:
                self.grid[tile[0][0]][tile[0][1]].set_switch_tiles(tile[2])


        # Set the user position
        self.player_position = setup[2]

        # Define if the game is over or not
        self.game_over = False
        self.game_win = False


    def get_grid(self):
        return self.grid

    def get_player_position(self):
        return self.player_position

    def get_game_over(self):
        return self.game_over

    def get_game_win(self):
        return self.game_win

    # Print the grid in the console
    def print_grid(self):

        print("====================")
        for i in range(len(self.grid)):
            print('|', end='')
            for j in range(len(self.grid[0])):
                print(self.grid[i][j].get_type(), end='')
                print("|", end='')
            print('')


    def move(self, move):
        #Move = Left/Right/Up/Down

        # Move only if the game is not over
        if (self.game_over is False):

            #1. Get the expected position
            if move == 'Left':
                new_position = (self.player_position[0],self.player_position[1] - 1)
            elif move == 'Right':
                new_position = (self.player_position[0], self.player_position[1] + 1)
            elif move == 'Up':
                new_position = (self.player_position[0] - 1,self.player_position[1])
            elif move == 'Down':
                new_position = (self.player_position[0] + 1,self.player_position[1])

            #2. Validate if the move is not on a visited tile (if so, the game is over)
            if (new_position[0] >= 0 and new_position[1] >= 0 and new_position[0] <= len(self.grid) - 1 and new_position[1] <= len(self.grid[0]) - 1):
                # if self.grid[new_position[0]][new_position[1]].get_type() == 'X':
                #     self.game_over = True
                #     self.player_position = new_position
                #     self.grid[self.player_position[0]][self.player_position[1]].set_type('X')

                #3. Show a message that the player lost
                if self.game_over:
                    print('GAME OVER :(')
                    print("Enter 'M' to go to the Menu, or 'R' to start over.")
                    self.game_win = False

                #4. Move if it was ok
                if self.game_over is False and self.grid[new_position[0]][new_position[1]].get_type() not in ['B','N','X']:

                    # Unblock a the tiles if the player is on a switch
                    if(self.grid[new_position[0]][new_position[1]].get_type() == 'I'):
                        tiles_to_unlock = self.grid[new_position[0]][new_position[1]].get_switch_tiles()
                        for tile_to_unlock in tiles_to_unlock:
                            self.grid[tile_to_unlock[0]][tile_to_unlock[1]].set_type(' ')

                    # Teleport to another tile if the player is on a teleport
                    if (self.grid[new_position[0]][new_position[1]].get_type() == 'T'):
                        self.player_position = new_position
                        self.grid[self.player_position[0]][self.player_position[1]].set_type('X')
                        self.player_position = self.grid[new_position[0]][new_position[1]].get_switch_tiles()[0]
                        self.grid[self.player_position[0]][self.player_position[1]].set_type('X')

                    else:
                        #Move the player
                        self.player_position = new_position
                        self.grid[self.player_position[0]][self.player_position[1]].set_type('X')
                        self.print_grid()



                #5. Validate if the level is completed
                level_completed = True
                for i in range(len(self.grid)):
                    for j in range(len(self.grid[0])):
                        if self.grid[i][j].get_type() == ' ':
                            level_completed = False

                if level_completed:
                    self.game_over = True
                    self.game_win = True
                    print('Level completed!!!')
                    print("Enter 'M' to go to the Menu, or 'R' to start over.")






