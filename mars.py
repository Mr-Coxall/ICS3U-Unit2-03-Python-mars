#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program calculates the time to Mars

import constants


def main():
    # this function calculates the time to Mars

    # input
    print("The average distance to mars is 106340000000m.")
    distance = int(input("Enter distance to mars (m): "))

    # process
    time = distance / constants.SPEED_OF_LIGHT

    # output
    print(
        "If mars is {0} m away it will take you {1} seconds to get there.".format(
            distance, time
        )
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
