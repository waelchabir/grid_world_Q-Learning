import numpy as np

# global variables
BOARD_ROWS = 3
BOARD_COLS = 4
WIN_STATE = (3, 0)
LOSE_STATE = (3, 1)
WALL_STATE = (1, 1)
START = (0, 2)
DETERMINISTIC = False

# Actions
UP      = 'up'
DOWN    = 'down'
LEFT    = 'left'
RIGHT   = 'right'

class Environment:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLS])
        self.board[WIN_STATE[1], WIN_STATE[0]] = 1
        self.board[LOSE_STATE[1], LOSE_STATE[0]] = -1
        self.state = START
        self.isEnd = False
        self.deterministic = DETERMINISTIC

    def giveReward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return -0.04

    def isEndPosition(self):
        if (self.state == WIN_STATE) or (self.state == LOSE_STATE):
            self.isEnd = True 

    def _chooseActionProb(self, action):
        if action == UP:
            return np.random.choice([UP, LEFT, RIGHT], p=[0.8, 0.1, 0.1])
        if action == DOWN:
            return np.random.choice([DOWN, LEFT, RIGHT], p=[0.8, 0.1, 0.1])
        if action == LEFT:
            return np.random.choice([LEFT, UP, DOWN], p=[0.8, 0.1, 0.1])
        if action == RIGHT:
            return np.random.choice([RIGHT, UP, DOWN], p=[0.8, 0.1, 0.1])
    
    def nextPosition(self, action):
        if self.deterministic:
            if action == UP:
                nxtState = (self.state[0], self.state[0] + 1)
            if action == DOWN:
                nxtState = (self.state[0], self.state[0] - 1)
            if action == LEFT:
                nxtState = (self.state[0] - 1, self.state[0])
            if action == RIGHT:
                nxtState = (self.state[0] + 1, self.state[0])
            self.deterministic = False
        else:
            action = self._chooseActionProb(action)
            self.deterministic = True
            nxtState = self.nextPosition(action)

        # Check if we hit the inner block
        if nxtState == WALL_STATE:
            return self.state
        # Check if we hit the LEFT/RIGHT wall
        if (nxtState[0] > (BOARD_COLS-1)) or (nxtState[0] < 0):
            return self.state
        # Check if we hit UPPER/DOWN wall
        if (nxtState[1] > (BOARD_ROWS - 1)) or (nxtState[1] < 0):
            return self.state
        return nxtState

    def showBoard(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-----------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')