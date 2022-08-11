from Grid import Grid
import keyboard
import ast



#Mettre dans GIT
#Faire le level editor dans Excel - DONE
#Mettre en forme la liste des tableaux dans Excel
#Créer plus de niveaux

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


if __name__ == '__main__':

    #Load the list of levels
    with open('level.txt', 'r') as f:
        contents = f.read()
        levels_dic = ast.literal_eval(contents)


        level = level_select()

        level_setup = levels_dic[level]
        #grid1 = Grid([3,4,(3,1),[((0,0),'N'),((0,1),' '),((0,2),' '),((1,0),'N'),((1,1),' '),((1,2),'N'),((2,0),'N'),((2,1),' '),((2,2),'N'),((3,0),'N'),((3,1),'X'),((3,2),'N')]])
        #grid1 = Grid([7,4,(3,3),[((0,0),' '),((0,1),' '),((0,2),' '),((0,3),' '),((0,4),' '),((0,5),' '),((0,6),' '),((1,0),' '),((1,1),'B'),((1,2),'B'),((1,3),' '),((1,4),' '),((1,5),'B'),((1,6),' '),((2,0),' '),((2,1),' '),((2,2),' '),((2,3),' '),((2,4),' '),((2,5),' '),((2,6),' '),((3,0),'N'),((3,1),'N'),((3,2),'N'),((3,3),'X'),((3,4),'N'),((3,5),'N'),((3,6),'N')]])
        grid1 = Grid(level_setup)

        grid1.print_grid()

        keyboard.on_press_key("left arrow", lambda _: grid1.move('Left'))
        keyboard.on_press_key("right arrow", lambda _: grid1.move('Right'))
        keyboard.on_press_key("up arrow", lambda _: grid1.move('Up'))
        keyboard.on_press_key("down arrow", lambda _: grid1.move('Down'))

        fin = False
        while fin != True:

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

