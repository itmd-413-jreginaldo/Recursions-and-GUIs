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

        # def create_coin_inputs():
        #     coins = ["Pennies", "Nickels", "Dimes", "Quarters", "Half Dollars", "Dollars"]
        #     row = 0
        #
        #     coin_group = tk.LabelFrame(self, text="Coins")  # Create coin group
        #     coin_group.grid(column=0, row=3)
        #
        #     for x in coins:
        #         tk.Label(coin_group, text=x).grid(column=0, row=row)
        #         tk.Entry(coin_group, width=3).grid(column=1, row=row)
        #
        #         row += 1

        """
        Methods
        """

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
        coin_group = tk.LabelFrame(self, text="Coins")  # Create coin group
        coin_group.grid(column=0, row=3, padx=(25, 25))

        tk.Label(coin_group, text="Pennies:").grid(column=0, row=0)  # Penny entry
        penny_input = tk.Entry(coin_group, width=3)
        penny_input.grid(column=1, row=0)

        tk.Label(coin_group, text="Nickels:", padx=0).grid(column=0, row=1)  # Nickel entry
        nickel_input = tk.Entry(coin_group, width=3)
        nickel_input.grid(column=1, row=1)

        tk.Label(coin_group, text="Dimes:").grid(column=0, row=2)  # Dime entry
        dime_input = tk.Entry(coin_group, width=3)
        dime_input.grid(column=1, row=2)

        tk.Label(coin_group, text="Quarters:").grid(column=0, row=3)  # Quarter entry
        quarter_input = tk.Entry(coin_group, width=3)
        quarter_input.grid(column=1, row=3)

        tk.Label(coin_group, text="Half Dollars:").grid(column=0, row=4)  # Half Dollar entry
        half_dollar_input = tk.Entry(coin_group, width=3)
        half_dollar_input.grid(column=1, row=4)

        tk.Label(coin_group, text="Dollars:").grid(column=0, row=5)  # Dollar entry
        dollar_input = tk.Entry(coin_group, width=3)
        dollar_input.grid(column=1, row=5)

        tk.Button(coin_group, text="Convert", command=lambda:())

        """
        Coin Calculations
        """

        """
        Display Coin Totals
        """
        totals_group = tk.LabelFrame(self, text="Totals")  # Create totals group
        totals_group.grid(column=1, row=3, padx=(25, 25))

        tk.Label(totals_group, text="Penny Value: $").grid(column=0, row=0)  # Create coin totals
        tk.Label(totals_group, text="Nickel Total").grid(column=0, row=1)
        tk.Label(totals_group, text="Dime Total").grid(column=0, row=2)
        tk.Label(totals_group, text="Quarter Total").grid(column=0, row=3)
        tk.Label(totals_group, text="Half Dollar Total").grid(column=0, row=4)
        tk.Label(totals_group, text="Dollar Total").grid(column=0, row=5)

        """
        Input Checks
        """
