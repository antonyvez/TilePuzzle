import ast

import pygame, sys
from Button import Button
from Grid import Grid

#Initialization of pygame
pygame.init()

#Creating the screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.png")

#Level grid
grid_level = Grid([3,4,(3,1),[((0,0),"N"),((0,1)," "),((0,2)," "),((1,0),"N"),((1,1)," "),((1,2),"N"),((2,0),"N"),((2,1)," "),((2,2),"N"),((3,0),"N"),((3,1),"X"),((3,2),"N")]])

#Function to add the font
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def how_to_play_screen():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        #Screen title
        SCREEN_TITLE = get_font(70).render("How to play:", True, "Black")
        OPTIONS_RECT = SCREEN_TITLE.get_rect(center=(640, 100))
        SCREEN.blit(SCREEN_TITLE, OPTIONS_RECT)
        #Controls
        control_instruction = "Controls: Use the keyboard arrows Left (←), Rigth (→), Up (↑) or Down (↓) to move the tile."
        SCREEN_TEXT = get_font(14).render(control_instruction, True, "Black")
        OPTIONS_RECT = SCREEN_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(SCREEN_TEXT, OPTIONS_RECT)
        #Goal
        goal_instruction = "Goal: Cover each possible tile until the last one, but you cannot comme back on an already visited tile!"
        SCREEN_TEXT = get_font(12).render(goal_instruction, True, "Black")
        OPTIONS_RECT = SCREEN_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(SCREEN_TEXT, OPTIONS_RECT)
        #Back to menu button
        BACK_TO_MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(1050, 600),
                              text_input="BACK TO MENU", font=get_font(27), base_color="#d7fcd4", hovering_color="White")
        BACK_TO_MENU_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_TO_MENU_BUTTON.update(SCREEN)

        #Listening to the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_TO_MENU_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def world_selection_screen():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # Screen title
        SCREEN_TITLE = get_font(70).render("Level selection:", True, "White")
        OPTIONS_RECT = SCREEN_TITLE.get_rect(center=(640, 100))
        SCREEN.blit(SCREEN_TITLE, OPTIONS_RECT)

        #Tutorial button
        WORLD_TUTORIAL = Button(image=None, pos=(180, 300),
                           text_input="Tutorial", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_TUTORIAL.changeColor(PLAY_MOUSE_POS)
        WORLD_TUTORIAL.update(SCREEN)
        #World 1
        WORLD_1 = Button(image=None, pos=(500, 300),
                            text_input="World 1", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_1.changeColor(PLAY_MOUSE_POS)
        WORLD_1.update(SCREEN)
        #World 2
        WORLD_2 = Button(image=None, pos=(820, 300),
                         text_input="World 2", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_2.changeColor(PLAY_MOUSE_POS)
        WORLD_2.update(SCREEN)
        #World 3
        WORLD_3 = Button(image=None, pos=(1140, 300),
                         text_input="World 3", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_3.changeColor(PLAY_MOUSE_POS)
        WORLD_3.update(SCREEN)

        #Back to menu button
        BACK_TO_MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(1050, 600),
                              text_input="BACK TO MENU", font=get_font(27), base_color="#d7fcd4", hovering_color="White")
        BACK_TO_MENU_BUTTON.changeColor(PLAY_MOUSE_POS)
        BACK_TO_MENU_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WORLD_TUTORIAL.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('0')
                if WORLD_1.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('1')
                if WORLD_2.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('2')
                if WORLD_3.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('3')
                if BACK_TO_MENU_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def level_selection_screen(world):

    # Get the list of levels in the selected world
    with open('level.txt', 'r') as f:
        contents = f.read()
        levels_dic = ast.literal_eval(contents)
        levels_to_display = []
        for key in levels_dic.keys():
            if key[0] == world:
                levels_to_display.append(key)

    #Display the screen
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # Screen title
        SCREEN_TITLE = get_font(70).render("Level selection:", True, "White")
        OPTIONS_RECT = SCREEN_TITLE.get_rect(center=(640, 100))
        SCREEN.blit(SCREEN_TITLE, OPTIONS_RECT)

        #Tutorial button
        WORLD_TUTORIAL = Button(image=None, pos=(180, 300),
                           text_input="Tutorial", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_TUTORIAL.changeColor(PLAY_MOUSE_POS)
        WORLD_TUTORIAL.update(SCREEN)
        #World 1
        WORLD_1 = Button(image=None, pos=(500, 300),
                            text_input="World 1", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_1.changeColor(PLAY_MOUSE_POS)
        WORLD_1.update(SCREEN)
        #World 2
        WORLD_2 = Button(image=None, pos=(820, 300),
                         text_input="World 2", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_2.changeColor(PLAY_MOUSE_POS)
        WORLD_2.update(SCREEN)
        #World 3
        WORLD_3 = Button(image=None, pos=(1140, 300),
                         text_input="World 3", font=get_font(30), base_color="White", hovering_color="Green")
        WORLD_3.changeColor(PLAY_MOUSE_POS)
        WORLD_3.update(SCREEN)

        #Levels button
        initial_position = 400

        level_button_list = []
        LEVEL1 = LEVEL2 = LEVEL3 = LEVEL4 = LEVEL5 = LEVEL6 = LEVEL7 = LEVEL8 = LEVEL9 = LEVEL10 = LEVEL11 = LEVEL12 = LEVEL13 = LEVEL14 = LEVEL15 = LEVEL16 = LEVEL17 = LEVEL18 = LEVEL19 = LEVEL20 = Button(image=None, pos=(10, 10), text_input='', font=get_font(30), base_color="White", hovering_color="Green")
        level_button_list.extend([LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5, LEVEL6, LEVEL7, LEVEL8, LEVEL9, LEVEL10, LEVEL11, LEVEL12, LEVEL13, LEVEL14, LEVEL15, LEVEL16, LEVEL17, LEVEL18, LEVEL19, LEVEL20])

        iterator = 0
        for level in levels_to_display:
            level_button_list[iterator] = Button(image=None, pos=(640, initial_position),
                             text_input=level, font=get_font(30), base_color="White", hovering_color="Green")
            level_button_list[iterator].changeColor(PLAY_MOUSE_POS)
            level_button_list[iterator].update(SCREEN)
            initial_position += 50
            iterator += 1

        #Back to menu button
        BACK_TO_MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(1050, 600),
                              text_input="BACK TO MENU", font=get_font(27), base_color="#d7fcd4", hovering_color="White")
        BACK_TO_MENU_BUTTON.changeColor(PLAY_MOUSE_POS)
        BACK_TO_MENU_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WORLD_TUTORIAL.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('0')
                if WORLD_1.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('1')
                if WORLD_2.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('2')
                if WORLD_3.checkForInput(PLAY_MOUSE_POS):
                    level_selection_screen('3')
                if level_button_list[0].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[0].get_text())
                if level_button_list[1].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[1].get_text())
                if level_button_list[2].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[2].get_text())
                if level_button_list[3].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[3].get_text())
                if level_button_list[4].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[4].get_text())
                if level_button_list[5].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[5].get_text())
                if level_button_list[6].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[6].get_text())
                if level_button_list[7].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[7].get_text())
                if level_button_list[8].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[8].get_text())
                if level_button_list[9].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[9].get_text())
                if level_button_list[10].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[10].get_text())
                if level_button_list[11].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[11].get_text())
                if level_button_list[12].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[12].get_text())
                if level_button_list[13].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[13].get_text())
                if level_button_list[14].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[14].get_text())
                if level_button_list[15].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[15].get_text())
                if level_button_list[16].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[16].get_text())
                if level_button_list[17].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[17].get_text())
                if level_button_list[18].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[18].get_text())
                if level_button_list[19].checkForInput(PLAY_MOUSE_POS):
                    play(level_button_list[19].get_text())
                if BACK_TO_MENU_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def play(level):
    with open('level.txt', 'r') as f:
        contents = f.read()
        levels_dic = ast.literal_eval(contents)
        level_setup = levels_dic[level]
        grid_level = Grid(level_setup)

        ## Il va maintenant falloir faire en sorte d'afficher la grid (créer et pour chaque case désiner une tuille d'une couleur selon le type
        ##Faire en sorte de prendre en compte les entrées du clavier

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        # Screen title
        SCREEN_TITLE = get_font(50).render(f"Level {level}", True, "White")
        OPTIONS_RECT = SCREEN_TITLE.get_rect(center=(640, 50))
        SCREEN.blit(SCREEN_TITLE, OPTIONS_RECT)
        # Back to level selection button
        BACK_TO_LEVEL_SELECTION = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(200, 100),
                                     text_input="BACK TO LEVEL SELECTION", font=get_font(15), base_color="#d7fcd4",
                                     hovering_color="White")
        BACK_TO_LEVEL_SELECTION.changeColor(OPTIONS_MOUSE_POS)
        BACK_TO_LEVEL_SELECTION.update(SCREEN)
        #Back to menu button
        START_OVER_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1100, 100),
                              text_input="START OVER", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        START_OVER_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        START_OVER_BUTTON.update(SCREEN)

        #Draw the grid content in the grid of 500x500
        grid = grid_level.get_grid()
        TILE_SIZE_X = 400 // len(grid)
        TILE_SIZE_Y = 400 // len(grid[0])

        for row in range(len(grid[0])):
            for col in range(len(grid)):
                type = grid[col][row].get_type()
                color = 'Black'
                if(type == 'N'):
                    color = 'Black'
                elif(type == 'B'):
                    color = 'Red'
                elif(type == 'X'):
                    color = '#929dfc' #Soft blue
                elif(type in [' ','I','T']):
                    color = 'White'
                if(grid_level.get_player_position() == (col, row)):
                    color = 'Blue'
                pygame.draw.rect(SCREEN, color, (390 + (row * TILE_SIZE_Y), 200 + (col * TILE_SIZE_X), TILE_SIZE_Y, TILE_SIZE_X))
                if type == 'I':
                    pygame.draw.rect(SCREEN, 'Yellow', (390 + (row * TILE_SIZE_Y) + TILE_SIZE_Y/4, 200 + (col * TILE_SIZE_X) + TILE_SIZE_X/4, TILE_SIZE_Y /2, TILE_SIZE_X / 2))
                    pygame.draw.rect(SCREEN, '#a1a1a1', (390 + (row * TILE_SIZE_Y) + TILE_SIZE_Y/4, 200 + (col * TILE_SIZE_X) + TILE_SIZE_X/4, TILE_SIZE_Y /2, TILE_SIZE_X / 2), 1)
                if type == 'T':
                    pygame.draw.rect(SCREEN, '#550180', (390 + (row * TILE_SIZE_Y) + TILE_SIZE_Y/4, 200 + (col * TILE_SIZE_X) + TILE_SIZE_X/4, TILE_SIZE_Y /2, TILE_SIZE_X / 2))
                    pygame.draw.rect(SCREEN, '#a1a1a1', (390 + (row * TILE_SIZE_Y) + TILE_SIZE_Y/4, 200 + (col * TILE_SIZE_X) + TILE_SIZE_X/4, TILE_SIZE_Y /2, TILE_SIZE_X / 2), 1)
                if color not in ['Black','Red']:
                    pygame.draw.rect(SCREEN, '#a1a1a1', (390 + (row * TILE_SIZE_Y), 200 + (col * TILE_SIZE_X), TILE_SIZE_Y, TILE_SIZE_X), 1)

        #Show the text if the game is over
        if(grid_level.get_game_over()):
            if(grid_level.get_game_win()):
                message = "Congratulations, level completed!"

                # Back to menu button
                NEXT_LEVEL_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1100, 500),
                                           text_input="Go to next level", font=get_font(20), base_color="#d7fcd4",
                                           hovering_color="White")
                NEXT_LEVEL_BUTTON.changeColor(OPTIONS_MOUSE_POS)
                NEXT_LEVEL_BUTTON.update(SCREEN)

            else:
                message = "Game over... Start over!"
            MESSAGE_TEXT = get_font(30).render(message, True, "White")
            OPTIONS_RECT = MESSAGE_TEXT.get_rect(center=(640, 670))
            SCREEN.blit(MESSAGE_TEXT, OPTIONS_RECT)


        # Listening to the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_TO_LEVEL_SELECTION.checkForInput(OPTIONS_MOUSE_POS):
                    level_selection_screen(level[0])
                if START_OVER_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    play(level)
                if NEXT_LEVEL_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    with open('level.txt', 'r') as f:
                        contents = f.read()
                        levels_dic = ast.literal_eval(contents)
                        levels_to_display = []

                        actual_world = level[0]
                        actual_level = level[-1]
                        #Validate if there is a next level in this world
                        next_level = f"{actual_world}-{int(actual_level) + 1}"
                        for key in levels_dic.keys():
                            if key == next_level:
                                play(next_level)
                        #Validate if another world exist
                        next_level = f"{int(actual_world) + 1}-1"
                        for key in levels_dic.keys():
                            if key == next_level:
                                play(next_level)
                        #Go back to level 1
                        play("0-1")

                    play(level)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    grid_level.move('Left')
                if event.key == pygame.K_RIGHT:
                    grid_level.move('Right')
                if event.key == pygame.K_UP:
                    grid_level.move('Up')
                if event.key == pygame.K_DOWN:
                    grid_level.move('Down')
                if event.key == pygame.K_SPACE:
                    play(level)

        pygame.display.update()



# def play():
#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()
#
#         SCREEN.fill("black")
#
#         PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
#         PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(PLAY_TEXT, PLAY_RECT)
#
#         PLAY_BACK = Button(image=None, pos=(640, 460),
#                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
#
#         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         PLAY_BACK.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#                     main_menu()
#
#         pygame.display.update()





def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Tile Puzzle", True, "White") ##b68f40
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        HOW_TO_PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300),
                                text_input="HOW TO PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 450),
                             text_input="PLAY", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1075, 600),
                             text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HOW_TO_PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #play()
                    world_selection_screen()
                if HOW_TO_PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    how_to_play_screen()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()