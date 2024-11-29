#!/usr/bin/env python3

import argparse
import datetime

def print_calendar(start_date, num_weeks):
    """Prints a calendar starting from the given start date for the specified number of weeks.

    Args:
        start_date: The date to start the calendar from.
        num_weeks: The number of weeks to display.
    """

    print()

    # Determine the first day of the week (Monday)
    first_day_of_week = start_date - datetime.timedelta(days=start_date.weekday())

    # Calculate the end date
    end_date = first_day_of_week + datetime.timedelta(weeks=num_weeks)

    # Print the header
    print("       Mon  Tue  Wed  Thu  Fri    Sat  Sun")
    print()
        
    # Iterate through each week
    current_date = first_day_of_week
    first_time = True
    while current_date < end_date  :
        mon_str = f"{current_date:%b}" if (current_date.day <=q 7 or first_time) else "   " 
        print(f"{mon_str}   ", end="")
        first_time = False

        for day_of_week in range(7) :
            # Print the date, highlighting today's date
            if current_date == datetime.date.today():
                print(f" \033[31m{current_date.day:2d}\033[0m  ", end="")  # Highlight today's date in red
            else:
                print(f" {current_date.day:2d}  ", end="")
            if day_of_week == 4 :
                print("  ", end="")

            current_date += datetime.timedelta(days=1)

        # Print a newline at the end of each week
        print()
        # print() # extra line (make config?)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print a calendar for a specified period.")
    parser.add_argument("-B", "--weeks_before", type=int, default=0, help="Number of weeks before today")
    parser.add_argument("-A", "--weeks_after", type=int, default=4, help="Number of weeks after today")

    args = parser.parse_args()

    # Calculate the start date
    today = datetime.date.today()
    start_date = today - datetime.timedelta(weeks=args.weeks_before)

    # Calculate the total number of weeks to print
    num_weeks = args.weeks_before + args.weeks_after + 1

    print_calendar(start_date, num_weeks)