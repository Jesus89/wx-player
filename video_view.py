# -*- coding: utf-8 -*-

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core

from image_view import ImageView
from timer import PerpetualTimer


class VideoView(ImageView):

    def __init__(self, parent, callback=None, size=(-1, -1)):
        ImageView.__init__(self, parent, size=size)

        self.callback = callback
        self.playing = False
        self.timer = PerpetualTimer(0.05, self.on_timer)

    def __del__(self):
        self.timer.cancel()

    def on_timer(self):
        if self.callback is not None:
            frame = self.callback()
            wx.CallAfter(self.set_frame, frame)

    def play(self):
        if not self.playing:
            self.playing = True
            self.timer.start()

    def pause(self):
        if self.playing:
            self.playing = False
            self.timer.cancel()

    def stop(self):
        if self.playing:
            self.playing = False
            self.timer.cancel()
            self.hide = True
            self.set_default_image()
