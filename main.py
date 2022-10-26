from time import sleep
from board import Board
from snake import Snake
import keyboard

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.run = True

    def hook(self, x):
        if x.name == 'q':
            self.run = False
        if x.event_type == 'down':
            self.board.update(x.name)

    def start(self):
        keyboard.hook(self.hook)
        while self.run:
            sleep(0.2)
            self.run = self.run and self.board.step()



def main():
    game = Game()
    game.start()

if __name__ == '__main__':
    main()