import time
import explorerhat

class Rover:
    MAX_SPEED =  100
    MIN_SPEED = -100
    ACCELERATION_DELTA=10
    TURN_TIME_IN_SECONDS=1.5

    def __init__(self, verbose=False):
        self.motors = explorerhat.motor
        self.speed = 0
        self.verbose = verbose

    @property
    def left(self):
        return self.motors.one

    @property
    def right(self):
        return self.motors.two

    def stop(self):
        self.set_speed(0)

    def speed_up(self):
        self.set_speed(self.speed + self.ACCELERATION_DELTA)

    def slow_down(self):
        self.set_speed(self.speed - self.ACCELERATION_DELTA)

    def turn_right(self):
        self.turn(self.right)

    def turn_left(self):
        self.turn(self.left)

    def turn(self, side):
        low_speed = 0 # self.speed - self.ACCELERATION_DELTA
        side.speed(low_speed)
        time.sleep(self.TURN_TIME_IN_SECONDS)
        self.set_speed(self.speed)

    def set_speed(self, speed):
        self.speed = min(max(speed, self.MIN_SPEED), self.MAX_SPEED)
        if self.verbose:
            print('speed is {}'.format(speed)) 
        self.motors.speed(self.speed)
            
