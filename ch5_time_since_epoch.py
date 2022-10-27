import time

total_secs = time.time()

# seconds = the remainder of total seconds divided by the number of seconds in a minute
# minutes = the remainder of total minutes divided by the number of minutes in a hour
# the same applies for hours and days

seconds = int(total_secs % 60)
minutes = int((total_secs // 60) % 60)
hours = int((total_secs // 3600) % 24)
days = int(total_secs // (3600 * 24))

if __name__ == '__main__':
    print('There have been', str(days), 'days', str(hours), 'hours',
          str(minutes), 'minutes and', str(seconds), 'seconds since the epoch.')