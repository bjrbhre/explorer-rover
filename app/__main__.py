import time
from .rover import Rover
from .keyboard_listener import KeyboardListener

def speed_up_sequence(rover):
    for i in range(10):
        rover.speed_up()
        time.sleep(1)

def slow_down_sequence(rover):
    for i in range(10):
        rover.slow_down()
        time.sleep(1)

if __name__ == '__main__':
    rover = Rover(verbose=True)
    keyboard = KeyboardListener()
    key = keyboard()
    while key.code != 'qqq':
        if key.is_key_up:
            rover.speed_up()
        elif key.is_key_down:
            rover.slow_down()
        elif key.is_key_left:
            rover.turn_left()
        elif key.is_key_right:
            rover.turn_right()
        else:
            print(key.code)
        key = keyboard()
