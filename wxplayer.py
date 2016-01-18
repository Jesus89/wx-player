#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx

from camera import Camera
from video_view import VideoView


class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(640, 480))

        camera = Camera(1)
        video_view = VideoView(self, camera.capture_image, 35)
        video_view.play()

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(video_view, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(box)
        self.Centre()


class MyApp(wx.App):
    def OnInit(self):
        frame = Frame(None)
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
