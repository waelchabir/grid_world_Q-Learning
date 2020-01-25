import numpy as np
from environment.grid_env import Environment

BOARD_COLS = 4
BOARD_ROWS = 3
EPSILON = 0.00001
GAMMA = 0.9

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
ACTIONS = { \
    UP:[UP, LEFT, RIGHT], \
    DOWN:[DOWN, LEFT, RIGHT], \
    LEFT:[LEFT, UP, DOWN], \
    RIGHT:[RIGHT, UP, DOWN]}

# Init V(s)
V = np.zeros((BOARD_ROWS, BOARD_COLS), dtype='float16')

# init actions probabilities 
# [prob_main_action, prob_first_alternative_action, prob_second_alternative_action]
p = [0.8, 0.1, 0.1]

delta  = 1 # a value greater than EPSILON to kick off the process
while(delta > EPSILON):
    delta = 0
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            state_value_old = V[row][col]
            values = [] # stores the value of each action (for a single state)
            for action in ACTIONS:
                new_state_value = 0.0
                for prob_action, prob in zip(ACTIONS[action], p):
                    env = Environment(state = (row, col), deterministic=True)
                    next_state = env.nextPosition(prob_action)
                    print()
                    reward = env.giveReward()
                    new_state_value += prob * (reward + GAMMA * V[next_state[0]][next_state[1]])
                values.append(new_state_value)
            V[row][col] = np.max(values)
            v_change = np.abs(state_value_old - np.max(values))
            delta = np.maximum(delta, v_change)
print("V = \n" + str(V))