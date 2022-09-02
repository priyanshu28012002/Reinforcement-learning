


class Field:
    def __init__(self, size, item_pickup, item_drop_off, start_position):
        self.size = size
        self.item_pickup = item_pickup
        self.item_drop_off = item_drop_off
        self.position = start_position
        self.item_in_car = False
        
    def get_number_of_states(self):
        return self.size*self.size*self.size*self.size*2
    
    def get_state(self):
        state = self.position[0]*self.size*self.size*self.size*2
        state = state + self.position[1]*self.size*self.size*2
        state = state + self.item_pickup[0]*self.size*2
        state = state + self.item_pickup[1]*2
        if self.item_in_car:
            state = state + 1
        return state
        
    def make_action(self, action):
        (x, y) = self.position
        if action == 0:  # Go South
            if y == self.size - 1:
                return -10, False
            else:
                self.position = (x, y + 1)
                return -1, False
        elif action == 1:  # Go North
            if y == 0:
                return -10, False
            else:
                self.position = (x, y - 1)
                return -1, False
        elif action == 2:  # Go East
            if x == 0:
                return -10, False
            else:
                self.position = (x - 1, y)
                return -1, False
        elif action == 3:  # Go West
            if x == self.size - 1:
                return -10, False
            else:
                self.position = (x + 1, y)
                return -1, False
        elif action == 4:  # Pickup item
            if self.item_in_car:
                return -10, False
            elif self.item_pickup != (x, y):
                return -10, False
            else:
                self.item_in_car = True
                return 20, False
        elif action == 5:  # Drop off item
            if not self.item_in_car:
                return -10, False
            elif self.item_drop_off != (x, y):
                self.item_pickup = (x, y)
                self.item_in_car = False
                return -10, False
            else:
                return 20, True
        
