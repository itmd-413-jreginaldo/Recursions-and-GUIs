"""
Credit: https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

This website helped me with the syntax on how to initially set-up tkinter as a class and how to properly define the
constructor

'def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)'

Class / Program Description:
    'coin.py' will be the main class to instantiate a tkinter GUI object when called upon in 'main.ipynb'

    This program will display an interactive GUI that a user can input coin quantities to get the total converted
    output in $USD.
"""

import tkinter as tk
import re


class Coin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        coins = ["Pennies", "Nickels", "Dimes", "Quarters", "Half Dollars", "Dollars"]

        """
        Styling
        """
        self.title("Coin Converter")
        self.geometry("400x250")  # Launch gui with this size
        self.minsize(400, 250)  # Display as fixed size
        self.maxsize(400, 250)  # Display as fixed size

        """
        Main
        """
        coin_entries = self.create_coin_input_fields(coins)  # Create input fields and return dict of {"Coin":Value}
        self.display_converted_values(coin_entries)  # Create output fields with the initiated zero values
        convert_button = tk.Button(self, text="Convert",  # Button to initiate conversion
                                   command=(lambda e=coin_entries: self.display_converted_values(e)))
        convert_button.grid(column=0, row=5)

    def create_coin_input_fields(self, coins):
        entries = {}

        coin_group = tk.LabelFrame(self, text="Coins")
        coin_group.grid(column=0, row=0, padx=25, pady=(30, 15))  # Create coin group

        row = 0
        for coin in coins:
            tk.Label(coin_group, text=coin).grid(column=0, row=row)  # Create labels
            coin_input = tk.Entry(coin_group, width=10)  # Create entry fields
            coin_input.insert(0, "0")
            coin_input.grid(column=1, row=row)

            entries[coin] = coin_input  # Insert user inputs into dict to be returned
            row += 1

        return entries

    def display_converted_values(self, entries):
        # "Pennies", "Nickels", "Dimes", "Quarters", "Half Dollars", "Dollars"

        totals_group = tk.LabelFrame(self, text="Coin Totals")  # Create totals group
        totals_group.grid(column=1, row=0, padx=25, pady=(30, 10))

        total = 0
        row = 0
        for entry in entries:
            tk.Label(totals_group, text=entry).grid(column=0, row=row)  # Create labels
            if entry == "Pennies":
                penny = self.check_entry_values(entry, entries[entry].get())
                total += penny

                penny = f"$ {penny:.2f}"

                tk.Label(totals_group, text=penny, width=10).grid(column=1, row=row)
            elif entry == "Nickels":
                nickel = self.check_entry_values(entry, entries[entry].get())
                total += nickel

                nickel = f"$ {nickel:.2f}"

                tk.Label(totals_group, text=nickel, width=10).grid(column=1, row=row)
            elif entry == "Dimes":
                dimes = self.check_entry_values(entry, entries[entry].get())
                total += dimes

                dimes = f"$ {dimes:.2f}"

                tk.Label(totals_group, text=dimes, width=10).grid(column=1, row=row)
            elif entry == "Quarters":
                quarters = self.check_entry_values(entry, entries[entry].get())
                total += quarters

                quarters = f"$ {quarters:.2f}"

                tk.Label(totals_group, text=quarters, width=10).grid(column=1, row=row)
            elif entry == "Half Dollars":
                half_dollar = self.check_entry_values(entry, entries[entry].get())
                total += half_dollar

                half_dollar = f"$ {half_dollar:.2f}"

                tk.Label(totals_group, text=half_dollar, width=10).grid(column=1, row=row)
            elif entry == "Dollars":
                dollar = self.check_entry_values(entry, entries[entry].get())
                total += dollar

                dollar = f"$ {dollar:.2f}"

                tk.Label(totals_group, text=dollar, width=10).grid(column=1, row=row)
            row += 1

        display_total = tk.LabelFrame(self, text="Final Total")  # Create totals group
        display_total.grid(column=1, row=5)

        total = f"$ {total:.2f}"
        tk.Label(display_total, text="Total").grid(column=0, row=0)
        tk.Label(display_total, text=total, width=15).grid(column=1, row=0)

    def check_entry_values(self, coin_name, value):
        coin_vals = {
            "Pennies": 0.01,
            "Nickels": 0.05,
            "Dimes": 0.1,
            "Quarters": .25,
            "Half Dollars": .5,
            "Dollars": 1
        }

        # regex = "^0+"
        # value.replaceAll(regex, value)

        try:
            value = coin_vals[coin_name] * float(value)
            if value < 0:
                value *= -1
        except ValueError:
            value = 0.0

        return value
