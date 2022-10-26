from enum import Enum

class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Snake:
    '''
    Main class for Snake
    '''
    def __init__(self, board_width=20, board_height=20, init_length=5) -> None:
        '''
        init status of Snake
        '''
        self.length = init_length
        self.body = [(x, 0) for x in range(self.length)]
        self.direction = Direction.RIGHT
        self.board_width = board_width
        self.board_height = board_height

    def step(self, apple):
        head_pos = self.body[-1]
        if self.direction == Direction.UP:
            next_pos = (head_pos[0], (head_pos[1] - 1)%self.board_height)
        elif self.direction == Direction.LEFT:
            next_pos = ((head_pos[0] - 1)%self.board_width, head_pos[1])
        elif self.direction == Direction.DOWN:
            next_pos = (head_pos[0], (head_pos[1] + 1)%self.board_height)
        elif self.direction == Direction.RIGHT:
            next_pos = ((head_pos[0] + 1)%self.board_width, head_pos[1])
        else:
            raise ValueError('Invalid direction')

        if next_pos == apple:
            self.body.append(next_pos)
            self.length += 1
            return 1
        elif next_pos in self.body:
            return -1
        else:
            self.body.append(next_pos)
            self.body.pop(0)
            return 0

    def update(self, keyboard_down):
        head_pos = self.body[-1]
        neck_pos = self.body[-2]
        if keyboard_down == 'up':
            if head_pos[1] <= neck_pos[1]:
                self.direction = Direction.UP
        elif keyboard_down == 'left':
            if head_pos[0] <= neck_pos[0]:
                self.direction = Direction.LEFT
        elif keyboard_down == 'down':
            if head_pos[1] >= neck_pos[1]:
                self.direction = Direction.DOWN
        elif keyboard_down == 'right':
            if head_pos[0] >= neck_pos[0]:
                self.direction = Direction.RIGHT
