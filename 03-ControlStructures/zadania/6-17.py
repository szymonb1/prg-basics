format_24h = input("Enter time (24-hour format): ")
hoursin12h = abs(int(format_24h[0:2]) - 12)
minutes = format_24h[3:6]
print(f"Time in 12-hour format: {hoursin12h}:{minutes}pm") 
