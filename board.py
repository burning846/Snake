import random
import os

from snake import Snake

class Board:
    def __init__(self, width=20, height=20) -> None:
        self.width = width
        self.height = height
        self.snake = Snake(self.width, self.height)
        self.apple = self._generate_apple(self.snake)
        

    def _generate_apple(self, snake):
        while True:
            apple = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1)
            )
            if apple not in snake.body:
                return apple

    def print(self):
        os.system("cls")
        array = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for x,y in self.snake.body:
            array[y][x] = 'o'
        array[self.apple[1]][self.apple[0]] = '*'

        for l in array:
            print(''.join(l))


    def step(self):
        status = self.snake.step(self.apple)
        if status == 1:
            self.apple = self._generate_apple(self.snake)
        elif status == -1:
            print('You Lost!')
            return False
        self.print()
        return True

    def update(self, keyboard_down):
        self.snake.update(keyboard_down)
