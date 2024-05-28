import map
import loot
import os




def clear():
    os.system('cls')


while True:
    
    clear()
    print(map.player.pos_y, map.player.pos_x)
    print("")
    map.update_room()
    print("w, a, s, d")
    player_input = input()

    x_lenght = len(map.room[map.player.pos_x])-1
    y_lenght = len(map.room)-1
    

    match player_input:

        case 'w': 
            if map.player.pos_y != 0:
                map.player.change_pos(0, -1)

        case 'a': 
            if map.player.pos_x != 0:
                map.player.change_pos(-1, 0)

        case 's': 
            if map.player.pos_y != y_lenght:
                map.player.change_pos(0, 1) 

        case 'd': 
            if map.player.pos_x != x_lenght:
                map.player.change_pos(1, 0) 

        case _: print("error")

