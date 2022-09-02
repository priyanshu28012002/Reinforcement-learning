import numpy as np
from env import Field
import random
size = 10
item_start = (0, 0)
item_drop_off = (9, 9)
start_position = (0, 9)

field = Field(size, item_start, item_drop_off, start_position)

number_of_states = field.get_number_of_states()
number_of_actions = 6
print(number_of_states,number_of_actions)
q_table = np.zeros((number_of_states, number_of_actions))
epsilon = 0.1
alpha = 0.1
gamma = 0.6

for _ in range(1000):
    field = Field(size, item_start, item_drop_off, start_position)
    done = False
    steps = 0
    
    while not done:
        state = field.get_state()
        #print(state)
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 5)
        else:
            action = np.argmax(q_table[state])
            
        reward, done = field.make_action(action)        
        new_state = field.get_state()
        new_state_max = np.max(q_table[new_state])
        
        q_table[state, action] = (1 - alpha)*q_table[state, action] + alpha*(reward + gamma*new_state_max - q_table[state, action])
        steps = steps + 1
print(steps)       
print(q_table)        


def reinforcement_learning():
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.6
    
    field = Field(size, item_start, item_drop_off, start_position)
    done = False
    steps = 0
    
    while not done:
        state = field.get_state()
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 5)
        else:
            action = np.argmax(q_table[state])
            
        reward, done = field.make_action(action)
        
        new_state = field.get_state()
        new_state_max = np.max(q_table[new_state])
        
        q_table[state, action] = (1 - alpha)*q_table[state, action] + alpha*(reward + gamma*new_state_max - q_table[state, action])
        
        steps = steps + 1
    
    return steps
#print(reinforcement_learning())    