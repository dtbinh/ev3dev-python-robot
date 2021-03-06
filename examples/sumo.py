#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from ev3dev.auto import *

import ev3robot.logic as logic
import ev3robot.robot as r

if __name__ == "__main__":

    class SumoController(logic.Controller):

        def setup(self):
            self.ptc_color = self.color()

        def loop(self):

            if self.has_obstacle(range=300):
                self.forward()
            else:
                self.brake()
                self.turn(degree=10)
                self.brake()
                time.sleep(0.5)

            # 0 black -> 100 white
            if self.color() + 10 < self.ptc_color:
                self.backward()
                time.sleep(3)
                self.brake()


    controller = SumoController(right_motor=LargeMotor('outA'), left_motor=LargeMotor('outB'),
                                    gyro=GyroSensor(), ultrasonic=UltrasonicSensor(), color=ColorSensor())

    robot = r.Robot(controller)
    robot.start()

    try:
        # wait for input
        name = raw_input("Press Enter to exit: ")
    except (KeyboardInterrupt, SystemExit):
        pass

    # stop robot
    robot.kill()