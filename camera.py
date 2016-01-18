# -*- coding: utf-8 -*-

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import cv2
import time


class Camera(object):

    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self._capture = None
        self._is_connected = False

        self.connect()

    def connect(self):
        self._is_connected = False
        self._capture = cv2.VideoCapture(self.camera_id)
        time.sleep(0.2)
        if self._capture.isOpened():
            self._is_connected = True

    def disconnect(self):
        if self._is_connected:
            if self._capture is not None:
                if self._capture.isOpened():
                    self._is_connected = False
                    self._capture.release()

    def capture_image(self, flush=0, mirror=False):
        if self._is_connected:
            if flush > 0:
                for i in xrange(0, flush):
                    self._capture.grab()
            ret, image = self._capture.read()
            if ret:
                image = cv2.transpose(image)
                if not mirror:
                    image = cv2.flip(image, 1)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                return image
