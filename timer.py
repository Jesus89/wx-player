#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

from threading import Timer


class PerpetualTimer(object):

    def __init__(self, t, function):
        self.t = t
        self.function = function
        self.running = False
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        if self.running:
            self.function()
            self.thread = Timer(self.t, self.handle_function)
            self.thread.start()

    def start(self):
        self.running = True
        self.thread.start()

    def cancel(self):
        self.running = False
        self.thread.cancel()
