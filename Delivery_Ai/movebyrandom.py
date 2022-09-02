from env import Field
import random

def naive_solution():
    size = 10
    item_start = (0, 0)
    item_drop_off = (9, 9)
    start_position = (0, 8)
    
    field = Field(size, item_start, item_drop_off, start_position)
    done = False
    steps = 0
    
    while not done:
        action = random.randint(0, 5)
        reward, done = field.make_action(action)
        steps = steps + 1
    
    return steps

print(naive_solution())    