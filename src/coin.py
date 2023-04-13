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

        coins = ["Pennies", "Nickels", "Dimes", "Quarters", "Half Dollars", "Dollars"]

        """
        Create Window Size
        """
        self.geometry("500x250")  # Launch gui with this size
        self.minsize(500, 250)  # Display as fixed size
        self.maxsize(500, 250)  # Display as fixed size

        """
        Styling
        """
        self.title("Coin Converter")

        """
        Create Coin Inputs
            - Penny
            - Nickel
            - Dime
            - Quarter
            - Half Dollar
            - Dollar
        """
        coin_entries = self.create_coin_input_fields(coins)

        """
        Coin Calculations
        """

        """
        Display Coin Totals
        """
        # totals_group = tk.LabelFrame(self, text="Totals")  # Create totals group
        # totals_group.grid(column=1, row=3, padx=(25, 25))
        #
        # tk.Label(totals_group, text="Penny Value: $").grid(column=0, row=0)  # Create coin totals
        # tk.Label(totals_group, text="Nickel Total").grid(column=0, row=1)
        # tk.Label(totals_group, text="Dime Total").grid(column=0, row=2)
        # tk.Label(totals_group, text="Quarter Total").grid(column=0, row=3)
        # tk.Label(totals_group, text="Half Dollar Total").grid(column=0, row=4)
        # tk.Label(totals_group, text="Dollar Total").grid(column=0, row=5)

        """
        Input Checks
        """
    def create_coin_input_fields(self, coins):
        entries = {}

        coin_group = tk.LabelFrame(self, text="Coins")
        coin_group.grid(column=0, row=3, padx=(25, 25), pady=(10, 25))  # Create coin group

        row = 0
        for coin in coins:
            tk.Label(coin_group, text=coin).grid(column=0, row=row)
            coin_input = tk.Entry(coin_group, width=3)
            coin_input.grid(column=1, row=row)

            entries[coin] = coin_input
            row += 1

        return entries