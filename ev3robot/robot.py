#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import time

class Robot(threading.Thread):

    def __init__(self, strategy):
        super(Robot, self).__init__()
        self.timeout = 0.1
        self.running = True
        self.strategy = strategy

    def run(self):
        self._invoke()

    def _invoke(self):

        while self.running:

            self.strategy.loop()

            time.sleep(self.timeout)


    def kill(self):
        self.running = False
        self.strategy.stop()

