#!/usr/bin/env python3

import argparse
import datetime

def get_years(day, start_year, end_year, target_date_str):
    """
    Gets the years within a given date range that match a specific weekday and date.

    Args:
        day (str): The target weekday (e.g., 'wed').
        start_year (int): The starting year of the range.
        end_year (int): The ending year of the range.
        target_date_str (str): The target date in the format "1 NOV".

    Returns:
        list: A list of years within the date range that match the criteria.
    """

    target_date = datetime.datetime.strptime(target_date_str, "%d %b")
    target_month, target_day = target_date.month, target_date.day

    years = []
    for year in range(start_year, end_year + 1):
        try:
            date = datetime.date(year, target_month, target_day)
            if date.strftime('%a').lower() == day:
                years.append(year)
        except ValueError:
            # Handle leap year issue for February 29th
            pass

    return years

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find years matching a specific weekday and date.')
    parser.add_argument('--day', type=str, default="sat",
                        help='Target weekday (e.g., mon, tue, wed)')
    parser.add_argument('--start-year', type=int, default=1980, 
                        help='Starting year of the range')
    parser.add_argument('--end-year', type=int, default=datetime.datetime.now().year, 
                        help='Ending year of the range')
    parser.add_argument('target_date', type=str, 
                        help='Target date in the format "1 NOV"')

    args = parser.parse_args()

    matching_years = get_years(args.day, args.start_year, args.end_year, args.target_date)

    if matching_years:
        print(f"Years matching {args.day} {args.target_date}: {matching_years}")
    else:
        print(f"No years found matching {args.day} {args.target_date} within the specified range.")
