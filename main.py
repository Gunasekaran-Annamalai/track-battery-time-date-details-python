import datetime as dt
import psutil as pu
import time
import json

battery = plugged = percent = 0
current_time = current_hour = current_minute = current_second = current_microsecond = 0
data = details = current_date = current_month = current_year = f = None

def battery_details():
    global battery, plugged, percent
    battery = pu.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"

def time_stamp():
    global current_time, current_hour, current_minute, current_second, current_microsecond, current_date, current_month, current_year
    current_time = dt.datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    current_second = current_time.second
    current_microsecond = current_time.microsecond
    current_date = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    if current_hour > 12:
        current_hour -= 12

def create_data():
    global data, f
    global current_date, current_month, current_year
    f = open('trackDetails.json')

    data = json.load(f)
    details = data['TrackedDetails']

    created_data = {
        "Date": "{} - {} - {}".format(current_date, current_month, current_year),
        "Time": "{} : {} : {}".format(current_hour, current_minute, current_second),
        "Percent": percent + '% | ' + plugged
     }

    details.append(created_data)
    open_json(data)

def open_json(data):
    with open('trackDetails.json', 'w') as file:
        json.dump(data, file, indent=4)
    f.close()

while True:
    battery_details()
    time_stamp()
    create_data()

    print(percent + '% | ' + plugged)
    print("{} - {} - {}".format(current_date, current_month, current_year))
    print("{} : {} : {}".format(current_hour, current_minute, current_second))
    time.sleep(1)
    open_json(data)
