


class character:
    def __init__(self, pos_x, pos_y, health, attack, speed, defence):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
        self.attack = attack
        self.speed = speed
        self.defence = defence

    def set_pos(self, x, y):
      self.pos_x = x
      self.pos_y = y


    def change_pos(self, x, y):
       self.pos_x += x
       self.pos_y += y

    def get_pos(self):
      return(self.pos_x,self.pos_y)
    
