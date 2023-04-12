"""
Credit: https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

This website helped me with the syntax on how to initially set-up tkinter as a class and how to properly define the
constructor

'def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)'
"""

import tkinter as tk
from tkinter import ttk


class Coin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        """
        Create Window Size
        """
        self.geometry("500x250")  # Launch gui with this size
        self.minsize(500, 250)  # Display as fixed size
        self.maxsize(500, 250)  # Display as fixed size

        """
        Styling
        """

        """
        Create Coin Inputs
            - Penny
            - Nickel
            - Dime
            - Quarter
            - Half Dollar
            - Dollar
        """

        """
        Coin Calculations
        """

        """
        Input Checks
        """


