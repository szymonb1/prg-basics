def f(time1, time2):
    time1_min = time_to_minutes(time1)
    time2_min = time_to_minutes(time2)

    if (time2_min < time1_min):
        return time2
    return time1

def time_to_minutes(time):
    time_split = time.split(':')
    is_12 = len(time_split[1]) > 2

    hour = int(time_split[0])
    minute = int(time_split[1][0:2])

    if (is_12 and time_split[1][2] == 'p'):
        hour += 12

    return hour * 60 + minute