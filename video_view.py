# -*- coding: utf-8 -*-

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core

import time
import threading

from image_view import ImageView


class VideoView(ImageView):

    def __init__(self, parent, callback=None,
                 size=(-1, -1), black=False):
        ImageView.__init__(self, parent, size=size, black=black)

        self.callback = callback

        self.playing = False
        self.thread = threading.Thread(target=self.player)

    def player(self):
        while self.playing:
            if self.callback is not None:
                frame = self.callback()
                wx.CallAfter(self.set_frame, frame)
            time.sleep(0.035)

    def play(self):
        if not self.playing:
            self.playing = True
            self.thread.start()

    def pause(self):
        if self.playing:
            self.playing = False

    def stop(self):
        if self.playing:
            self.playing = False
            self.hide = True
            self.set_default_image()
