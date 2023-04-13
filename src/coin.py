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
        coin_entries = self.create_coin_input_fields(coins)

        convert_button = tk.Button(self, text="Convert",
                                   command=(lambda e=coin_entries: self.check_entry_values(e)))
        convert_button.grid(column=0, row=5)

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

    def create_coin_input_fields(self, coins):
        entries = {}

        coin_group = tk.LabelFrame(self, text="Coins")
        coin_group.grid(column=0, padx=(25, 25), pady=(10, 10))  # Create coin group

        row = 0
        for coin in coins:
            tk.Label(coin_group, text=coin).grid(column=0, row=row)  # Create labels
            coin_input = tk.Entry(coin_group, width=5)  # Create entry fields
            coin_input.insert(0, "0")
            coin_input.grid(column=1, row=row)

            entries[coin] = coin_input  # Insert user inputs into dict to be returned
            row += 1

        return entries

    def check_entry_values(self, entries):
        for entry in entries:
            print(entries[entry].get())
            # try:  # Attempt to convert entry values into ints
            #     int_check = int(entries[entry].get)  # Get each coin value from dict
            #     print(int_check)
            # except ValueError as e:
            #     print(e)

    def display_converted_values(self, entries):

        pass
