"""
Credit: https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

This website helped me with the syntax on how to initially set-up tkinter as a class and how to properly define the
constructor

'def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)'
"""

import tkinter as tk


class Coin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        coins = ["Pennies", "Nickels", "Dimes", "Quarters", "Half Dollars", "Dollars"]

        """
        Styling
        """
        self.title("Coin Converter")
        self.geometry("500x250")  # Launch gui with this size
        self.minsize(500, 250)  # Display as fixed size
        self.maxsize(500, 250)  # Display as fixed size

        """
        Main
        """
        coin_entries = self.create_coin_input_fields(coins)  # Create input fields and return dict of {"Coin":Value}
        self.display_converted_values(coin_entries)
        convert_button = tk.Button(self, text="Convert",  # Button to initiate conversion
                                   command=(lambda e=coin_entries: self.check_entry_values(e)))
        convert_button.grid(column=0, row=5)

    def create_coin_input_fields(self, coins):
        entries = {}

        coin_group = tk.LabelFrame(self, text="Coins")
        coin_group.grid(column=0, row=0, padx=25, pady=(30, 10))  # Create coin group

        row = 0
        for coin in coins:
            tk.Label(coin_group, text=coin).grid(column=0, row=row)  # Create labels
            coin_input = tk.Entry(coin_group, width=10)  # Create entry fields
            coin_input.insert(0, "0")
            coin_input.grid(column=1, row=row)

            entries[coin] = coin_input  # Insert user inputs into dict to be returned
            row += 1

        return entries

    def check_entry_values(self, entries):
        for entry in entries:
            print(entries[entry].get())
            try:  # Attempt to convert entry values into ints
                int_entry = int(entries[entry].get())  # Get each coin value from dict
                if int_entry < 0:  # Just convert negative values to positive nums
                    int_entry *= -1
            except ValueError as e:
                print("Error: Non-Integer value detected")

        self.display_converted_values(entries)

    def display_converted_values(self, entries):
        # "Pennies", "Nickels", "Dimes", "Quarters", "Half Dollars", "Dollars"

        totals_group = tk.LabelFrame(self, text="Coin Totals")  # Create totals group
        totals_group.grid(column=1, row=0, padx=25, pady=(30, 10))

        total = 0
        row = 0
        for entry in entries:
            tk.Label(totals_group, text=entry).grid(column=0, row=row)  # Create labels
            if entry == "Pennies":
                penny = str(round((float(entries[entry].get()) * .01), 2))

                total += float(penny)
                tk.Label(totals_group, text=penny, width=25).grid(column=1, row=row)
            elif entry == "Nickels":
                nickel = str(round((float(entries[entry].get()) * .05), 2))

                total += float(nickel)
                tk.Label(totals_group, text=nickel, width=25).grid(column=1, row=row)
            elif entry == "Dimes":
                dimes = str(round((float(entries[entry].get()) * .1), 2))
                total += float(dimes)
                tk.Label(totals_group, text=dimes, width=25).grid(column=1, row=row)
            elif entry == "Quarters":
                quarters = str(round((float(entries[entry].get()) * .25), 2))

                total += float(quarters)
                tk.Label(totals_group, text=quarters, width=25).grid(column=1, row=row)
            elif entry == "Half Dollars":
                half_dollar = str(round((float(entries[entry].get()) * .5), 2))

                total += float(half_dollar)
                tk.Label(totals_group, text=half_dollar, width=25).grid(column=1, row=row)
            elif entry == "Dollars":
                dollar = str(float(entries[entry].get()))

                total += float(dollar)
                tk.Label(totals_group, text=dollar, width=25).grid(column=1, row=row)

            row += 1

        display_total = tk.LabelFrame(self, text="Final Total")  # Create totals group
        display_total.grid(column=1, row=5)
        tk.Label(display_total, text="Total").grid(column=0, row=0)
        tk.Label(display_total, text=str(total), width=30).grid(column=1, row=0)
