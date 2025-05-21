#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: May 21, 2025
# This program asks the user for the
# subtotal and total cost of an item.
# Then uses a function to calculate
# and display the tax as a percentage.

def convert_time(seconds):
    hours = seconds / 3600
    minutes = (seconds % 3600) / 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

def main():
    while True:
        while True:
            seconds_input_string = input("Enter the time in seconds: ")
            try:
                seconds_input_integer = int(seconds_input_string)
            except Exception:
                print("{} is not valid input".format(seconds_input_string))

