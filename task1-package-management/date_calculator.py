import datetime

# Calculates the absolute number of days between two date strings.
# Arguments:
#   date1_str (str): First date string.
#   date2_str (str): Second date string.
#   date_format (str): Expected date format (default: "%Y-%m-%d").
# Returns:
#   int: Number of days between the two dates.
# Raises:
#   ValueError: If date strings are not in the correct format.
# Example:
#   calculate_date_difference("2025-01-01", "2025-01-10") -> 9
#   calculate_date_difference("2025/01/01", "2025-01-10") -> raises ValueError
def calculate_date_difference(date1_str, date2_str, date_format="%Y-%m-%d"):
    try:
        date1 = datetime.datetime.strptime(date1_str, date_format).date()
        date2 = datetime.datetime.strptime(date2_str, date_format).date()
        return abs((date2 - date1).days)
    except ValueError as ve:
        raise ValueError(f"Invalid date format: {ve}")


if __name__ == "__main__":
    # Example usage
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        diff = calculate_date_difference(d1, d2)
        print(f"The difference is {diff} day(s).")
    except ValueError as e:
        print(f"Error: {e}")
