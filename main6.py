from datetime import datetime, date, time, timedelta, timezone

print("=== 1. DATETIME CLASS METHODS (Date + Time) ===")
# Current date and local time
now = datetime.now()
print(f"Current Date & Time (now): {now}")

# Current time in UTC (Universal Coordinated Time)
utc_now = datetime.now(timezone.utc)
print(f"UTC Time (now with timezone): {utc_now}")

# Create a specific custom datetime object (Year, Month, Day, Hour, Minute, Second)
custom_dt = datetime(2026, 7, 27, 14, 30, 45)
print(f"Custom Datetime: {custom_dt}")

# Parse a text string into a real datetime object (strptime)
date_string = "2026-12-25 09:00:00"
parsed_dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed from string (strptime): {parsed_dt}")

# Convert a datetime object into a clean text string format (strftime)
formatted_str = now.strftime("%A, %B %d, %Y I:%M %p")
print(f"Formatted into readable text (strftime): {formatted_str}\n")


print("=== 2. DATE CLASS METHODS (Date Only) ===")
# Today's date
today = date.today()
print(f"Today's Date (today): {today}")

# Create a specific custom date object (Year, Month, Day)
custom_date = date(2026, 1, 1)
print(f"Custom Date: {custom_date}")

# Extract parts of the date
print(f"Year: {today.year} | Month: {today.month} | Day: {today.day}")
# Day of the week (0 = Monday, 6 = Sunday)
print(f"Weekday index (0-6): {today.weekday()}\n")


print("=== 3. TIME CLASS METHODS (Time Only) ===")
# Create a specific custom time object (Hour, Minute, Second, Microsecond)
custom_time = time(18, 45, 30, 500)
print(f"Custom Time: {custom_time}")
print(f"Hour: {custom_time.hour} | Minute: {custom_time.minute} | Second: {custom_time.second}\n")


print("=== 4. TIMEDELTA CLASS METHODS (Time Math & Duration) ===")
# Define time durations
five_days = timedelta(days=5)
three_hours = timedelta(hours=3)

# Future date calculation (Addition)
future_date = today + five_days
print(f"Date 5 days from today: {future_date}")

# Past time calculation (Subtraction)
past_time = now - three_hours
print(f"Time 3 hours ago: {past_time}")

# Finding the exact difference between two dates
date1 = date(2026, 12, 25)
date2 = date(2026, 7, 27)
duration_left = date1 - date2
print(f"Days left until Christmas: {duration_left.days} days\n")


print("=== 5. TIMEZONE CLASS METHODS ===")
# Create specific timezone offsets (e.g., UTC+5:30 for Indian Standard Time)
ist_timezone = timezone(timedelta(hours=5, minutes=30))
ist_time = datetime.now(ist_timezone)
print(f"Current Time in IST: {ist_time}")
