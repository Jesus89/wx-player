# -*- coding: utf-8 -*-

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core
# import datetime

from image_view import ImageView


class VideoView(ImageView):

    def __init__(self, parent, callback=None, milliseconds=1,
                 size=(-1, -1), black=False, _reload=False):
        ImageView.__init__(self, parent, size=size, black=black)

        self.reload = _reload
        self.callback = callback
        self.milliseconds = milliseconds

        self.playing = False

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)

    def on_timer(self, event):
        if self.playing:
            if self.callback is not None:
                # begin = datetime.datetime.now()
                frame = self.callback()
                self.set_frame(frame)
                # print datetime.datetime.now() - begin

    def play(self):
        if not self.playing:
            self.playing = True
            self._start()

    def _start(self):
        self.timer.Start(milliseconds=self.milliseconds)

    def pause(self):
        if self.playing:
            self.playing = False
            self.timer.Stop()

    def stop(self):
        if self.playing:
            self.playing = False
            self.timer.Stop()
            self.hide = True
            self.set_default_image()
