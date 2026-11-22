import arcade
import math
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "KPop Demon Hunters"


class Game(arcade.Window):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def update(self, delta_time: float):
        pass

    def on_draw(self):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

window = arcade.Window()
arcade.run()