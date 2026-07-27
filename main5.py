import datetime

# Get current date and time down to the microsecond
now = datetime.datetime.now()
print(now)  # Output example: 2026-07-27 12:06:15.123456

# Get just today's date (no time component)
today = datetime.date.today()
print(today)  # Output example: 2026-07-27
