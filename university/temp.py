from datetime import datetime, timedelta


def separate_weeks_by_weekdays_from_past():
    # Get today's date
    today = datetime.today()

    # Calculate the first day, which is 30 days before today
    first_day = today - timedelta(days=30)

    # Ensure we start from the first weekday of the week (Monday)
    if first_day.weekday() > 4:  # If it's Saturday or Sunday, move to the next Monday
        first_day += timedelta(days=(7 - first_day.weekday()))

    current_day = first_day
    week_num = 1
    week_info = {}

    while current_day <= today:  # Keep looping until we reach today's date
        # Find the Friday of the current week
        next_weekday = current_day + timedelta(days=4 - current_day.weekday())

        # If the calculated Friday goes beyond today, adjust it to today
        if next_weekday > today:
            next_weekday = today

        # Store the week range in the dictionary
        week_info[week_num] = (
            current_day.strftime("%d/%m/%A"),
            next_weekday.strftime("%d/%m/%A"),
        )

        # Prepare for the next week (move to next Monday)
        current_day = next_weekday + timedelta(days=(7 - next_weekday.weekday()))

        if current_day <= today:
            week_num += 1

    return week_info


# Example usage:
weeks = separate_weeks_by_weekdays_from_past()

# Print the stored week information
for week, dates in weeks.items():
    print(f"Week {week}: {dates[0]} - {dates[1]}")
