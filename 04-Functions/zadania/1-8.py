def time_string(hours, minutes, time_format):
    if time_format == '12':
        if hours>12:
            hours = abs(hours-12)
            return f"{hours}:{minutes:02d}pm"
        elif hours == 0 or hours == 00:
            return f"12:{minutes:02d}am"
        elif hours == 12:
            return f"12:{minutes:02d}pm"
        else:
            return f"{hours}:{minutes:02d}am"
    elif time_format == '24':
        return f"{hours}:{minutes:02d}"
    else:
        return "nieprawidłowy format"
print(time_string(12, 46, '12'))