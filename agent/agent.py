from environment.grid_env import Environment

# global variables
BOARD_ROWS = 3
BOARD_COLS = 4

# Actions
UP      = 'up'
DOWN    = 'down'
LEFT    = 'left'
RIGHT   = 'right'

class Agent:
    def __init__(self):
        self.states = []
        self.actions = [UP, DOWN, LEFT, RIGHT]
        self.State = Environment
        self.lr = 0.1
        self.exp_rate = 0.3
        # initial state reward
        self.state_values = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.state_values[(i, j)] = 0  # set initial value to 0
