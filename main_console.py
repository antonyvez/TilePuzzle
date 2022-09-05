import ast

from Grid import Grid
import keyboard


def level_select():
    with open('level.txt', 'r') as f:
        contents = f.read()
        levels_dic = ast.literal_eval(contents)

        print("Select a level:")
        print("==================")
        for key in levels_dic.keys():
            print(key)

        level = input()
        return level


# Draw the grid in the window
# def draw_grid(grid, window):
#
#     window.fill(BLACK)
#
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#
#             #Get the color according to the type of tile
#             tile_color = (0, 0, 0)
#
#             if (grid[i][j].get_type() == 'X'):
#                 tile_color = (0, 255, 0) #Green
#             elif (grid[i][j].get_type() == ' '):
#                 tile_color = (158, 173, 233)  #Light blue
#             elif (grid[i][j].get_type() == 'B'):
#                 tile_color = (255, 0, 0)  #Red
#             elif (grid[i][j].get_type() == 'N'):
#                 tile_color = (0, 0, 0)  #Black
#
#             #Draw the grid
#             pygame.draw.rect(window, tile_color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
#             pygame.display.update()




if __name__ == '__main__':

    #Load the list of levels
    with open('level.txt', 'r') as f:
        contents = f.read()
        levels_dic = ast.literal_eval(contents)


        level = level_select()

        level_setup = levels_dic[level]
        grid1 = Grid(level_setup)

        grid1.print_grid()

        keyboard.on_press_key("left arrow", lambda _: grid1.move('Left'))
        keyboard.on_press_key("right arrow", lambda _: grid1.move('Right'))
        keyboard.on_press_key("up arrow", lambda _: grid1.move('Up'))
        keyboard.on_press_key("down arrow", lambda _: grid1.move('Down'))

        end = False
        while end != True:

            player_input = input()

            if(player_input == 'Q'):
                fin = True

            if(player_input == 'L'):
                grid1.print_grid()

            if(player_input == 'R'):
                grid1 = Grid(level_setup)
                grid1.print_grid()

            if(player_input == 'M'):
                level = level_select()
                level_setup = levels_dic[level]
                grid1 = Grid(level_setup)
                grid1.print_grid()
                keyboard.on_press_key("left arrow", lambda _: grid1.move('Left'))
                keyboard.on_press_key("right arrow", lambda _: grid1.move('Right'))
                keyboard.on_press_key("up arrow", lambda _: grid1.move('Up'))
                keyboard.on_press_key("down arrow", lambda _: grid1.move('Down'))
