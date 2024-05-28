import character

player = character.character(0, 0, 5, 1, 100 , 50)

x = "tomt"
m = "ee"
t = "tre"

room = [["x", "t", "x", "x", "t", "x"],
         
        ["m", "e", "k", "x", "t", "x"],

        ["x", "f", "x", "x", "t", "x"],

        ["x", "f", "x", "x", "t", "x"],

        ["x", "f", "x", "x", "t", "x"],

        ["x", "f", "x", "x", "t", "x"] 

        ]

def get_room(pos_y, pos_x):
    return room[player.pos_y][player.pos_x]

#print("currently in a ", get_room(player.pos_y,player.pos_x))




#l = len(player.pos_y)

def update_room():
    for mp in room:
        mp = list(map(lambda x: x.replace("▮", "▯"), mp))
        room[player.pos_y] [player.pos_x] = "▮"
        for lmnt in mp:
            print(lmnt, end='  ')
        print()

        
        


#for lst in room:
   # print(*lst)
#print(player.pos_x, player.pos_y)

