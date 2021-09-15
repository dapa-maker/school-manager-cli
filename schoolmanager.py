import datetime
from datetime import date
import os.path
import csv
import os
import time
import asyncio

now = date.today()
# get holidays from user if not already existing and store to csv
if not os.path.exists("h_days.csv"):
    ans = "n"
    while ans == "n":
        print("No holidays found.")
        oster_h = input("oster holidays(YYYY-MM-DD): ")
        sommer_h = input("sommer holidays(YYYY-MM-DD): ")
        herbst_h = input("herbst holidays(YYYY-MM-DD): ")
        winter_h = input("Winter holidays(YYYY-MM-DD): ")
        holidays = {"oster": oster_h, "sommer": sommer_h, "herbst": herbst_h,"winter": winter_h}
        print(holidays)
        ans = input("Correct(Y/N)").lower()
    with open('h_days.csv', 'w') as f: 
        w = csv.DictWriter(f, holidays.keys())
        w.writeheader()
        w.writerow(holidays)

#get dates for holidays from h_das.csv
a_csv_file = open("h_days.csv", "r")
dict_reader = csv.DictReader(a_csv_file)
ordered_dict_from_csv = list(dict_reader)[0]
holidays_dict = dict(ordered_dict_from_csv)    

#function forvcalculating remaining times until holidays
def time_until_holidays(now, start):
    return int((date.fromisoformat(start) - now).days)

#create dict holidays and days remaining as integers
time_to_holidays = {}
for key, value in holidays_dict.items():
    time_to_holidays[key]= int(time_until_holidays(now, value))

# find the min time 
min = 90000
for key, value in time_to_holidays.items():
    if value < min and value > 0:
        min = value
        min_name = key

#calculate length of school variation
school_start = date.fromisoformat('2020-02-03')
school_fa = date.fromisoformat('2022-07-25')
school_fa_len = school_fa - school_start
school_a = date.fromisoformat("2023-07-24")
school_a_len = school_a - school_start

#school length until now
school_now = now - school_start

#calculate percentage
school_fa_percent = round((school_now/school_fa_len)*100, 2)
school_a_percent = round((school_now/school_a_len)*100, 2)


print("Fachabitur: "+str(school_fa_percent)+"%")
print("Abitur: "+str(school_a_percent)+"%")
print("Next holidays: "+min_name.capitalize()+" holidays in "+ str(min)+" days = "+str(round((min /7), 2))+" weeks = "+str(round((min/30.417), 2))+" months.")
input("Press any button to continue...")