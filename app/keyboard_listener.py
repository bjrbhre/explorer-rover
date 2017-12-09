import sys
import tty
import termios

class Key():
    KEY_CODES = {
        'up':    '\x1b[A',
        'down':  '\x1b[B',
        'right': '\x1b[C',
        'left':  '\x1b[D',
    }

    def __init__(self, code):
        self.code = code

    def is_key_code(self, code):
        key_code = self.KEY_CODES.get(code, None)
        return key_code and self.code == key_code

    @property
    def is_empty(self):
        return self.code == ''

    @property
    def is_key_up(self):
        return self.is_key_code('up')

    @property
    def is_key_down(self):
        return self.is_key_code('down')

    @property
    def is_key_right(self):
        return self.is_key_code('right')

    @property
    def is_key_left(self):
        return self.is_key_code('left')

class KeyGetter:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return Key(ch)

class KeyboardListener:
    def __call__(self):
        getter = KeyGetter()
        key = getter()
        while key.is_empty:
            key = getter()
        return key

if __name__=='__main__':
    keyboard = KeyboardListener()
    for _ in range(20):
        key = keyboard()
        if key.is_key_up:
            print('up')
        elif key.is_key_down:
            print('down')
        elif key.is_key_right:
            print('right')
        elif key.is_key_left:
            print('left')
        else:
            print('not an arrow key!')
