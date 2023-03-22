from datetime import datetime as dt, timedelta as td

now = dt.now()
hours_ago = now - td(hours=2)
print(now.strftime("%H:%M"), hours_ago)

