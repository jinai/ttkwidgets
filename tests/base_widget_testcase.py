# Copyright (c) RedFantom 2017
# For license see LICENSE
import unittest
import tkinter as tk


class BaseWidgetTest(unittest.TestCase):
    def setUp(self):
        self.window = tk.Toplevel()
        self.window.update()

    def tearDown(self):
        self.window.update()
        self.window.destroy()
