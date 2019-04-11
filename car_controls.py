import time
from pwm import PWM
from utils import interpolate_01, interpolate_pm1


STOP_DUTY    = 1000000
FASTEST_DUTY = 2000000  # way too fast

RIGHT_DUTY  =  700000  # 850000  if being conservative
# CENTER_DUTY = 1250000  # aim for this as the center
LEFT_DUTY   = 1900000  # 1750000 if being conservative

STOP   = 0
CENTER = 0
LEFT   = -1
RIGHT  = +1


class Controls:
    def __init__(self):
        self.motor = PWM(0)
        self.servo = PWM(1)

        self.motor.export()
        self.servo.export()

        self.motor.period = 20000000
        self.servo.period = 20000000

        self.motor.enable = True
        self.servo.enable = True

        self.neutral()

    def move(self, speed):
        """
        0 <= speed <= 1
        where 0 is stopped
              1 is full speed
        """
        speed = interpolate_01(STOP_DUTY, FASTEST_DUTY, speed)
        self.motor.duty_cycle = speed

    def turn(self, angle):
        """
        -1 <= angle <= +1
        where -1 is left
               0 is center
              +1 is right
        """
        # -angle because LEFT_DUTY > RIGHT_DUTY but want -1 to mean LEFT
        angle = interpolate_pm1(LEFT_DUTY, RIGHT_DUTY, -angle)
        self.servo.duty_cycle = angle

    def neutral(self):
        self.move(STOP)
        self.turn(CENTER)

    def test(self):
        self.neutral()

        self.turn(LEFT)
        time.sleep(.5)

        self.turn(RIGHT)
        time.sleep(.5)

        self.turn(CENTER)
        time.sleep(.5)

        self.move(.15)
        time.sleep(1)

        self.move(STOP)

    def is_stopped(self):
        return self.motor.duty_cycle <= STOP_DUTY * 1.01
