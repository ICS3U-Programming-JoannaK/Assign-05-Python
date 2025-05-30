#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: May 21, 2025
# This program takes a time in seconds
# and converts it into hours, minutes, and
# remaining seconds.


def convert_time(player_seconds):
    converted_times = []
    # loop through each time from the list for each player
    for time in player_seconds:
        # calculate the hours
        hours = time // 3600
        # calculate the minutes
        minutes = (time % 3600) // 60
        # calculate the remaining seconds
        remaining_seconds = time % 60
        # store the conversions
        converted_times.append([hours, minutes, remaining_seconds])
        # returns the conversions to the main function
    return converted_times


def main():
    # Displays greeting card
    print("*****************************************")
    print("*****************************************")
    print("***           Hello user !             **")
    print("*****************************************")
    print("*****************************************")
    print("\n")

    # list to store input times for each player
    player_seconds = []
    # loops 3 times to get the times for 3 players
    for counter in range(0, 3):
        # Making sure the user's inputs are valid
        while True:
            # getting the user's input (time in seconds)
            seconds_string = input("Enter the player's time in seconds: ")
            try:
                # converts the input from string to float
                seconds_float = float(seconds_string)
                # checks for invalid input, time cannot be negative
                if seconds_float < 0:
                    print(
                        "{} is not valid input. Seconds cannot be negative".format(
                            seconds_float
                        )
                    )
                else:
                    # if the input is in the allowed range, it leaves the loop
                    player_seconds.append(seconds_float)
                    break
                # catches erroneous input
            except Exception:
                print("{} is not valid input".format(seconds_string))

    # converts the user's input (seconds) into hours, minutes and remaining seconds
    converted = convert_time(player_seconds)
    counter = 0
    # goes through each player's time and displays their converted time
    for time in converted:
        # using the original input time for reference
        original = player_seconds[counter]

        # blank line
        print("\n")
        # displays the conversions for each player
        print(
            "He/She ran {} seconds, which is equal to {} hour(s), {} minutes and {} remaining seconds".format(
                original, time[0], time[1], time[2]
            )
        )
        # moves onto the next player's time
        counter += 1


    # Thank you message
    print("\n")
    print("\n")
    print("Thank you for using my program")


if __name__ == "__main__":
    main()
