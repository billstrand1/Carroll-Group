import datetime
from players import *
import re
from tabulate import tabulate
from operator import itemgetter

tday = datetime.date.today()
birthday_list = []
for player in player_list:
	# player.class_birthday()

	# birthdate = re.split('/', player.birthday)
	# print(f"{player.signup_name}, {birthdate}")
	# day = int(birthdate[0])
	# month = int(birthdate[1])
	# year = int(birthdate[2])
	# birthdate_formatted = int(year), int(day), int(month)
	# print (birthdate_formatted)
	# print(f"{player.signup_name}, {birthdate_formatted}")
	# player_bdate = datetime.date(2020, day, month)
	player_bday = (player.birthdate).strftime('%b %d')
	player_no_days = ((player.birthdate - tday).days)
	if player.signup_name == 'Rocky': player.age = '??'
	birthday_info = [player.signup_name, player.age, player_bday, player_no_days]
	birthday_list.append(birthday_info)
	# print(f"{player.signup_name} will be {player.age} on {(player.birthdate).strftime('%b %d')} ({(player.birthdate - tday).days} days) ")
	# birthdays.append[player.signup_name] #, player.age, player.birthdate]

b = sorted(birthday_list, key=itemgetter(3))
headers = ["\nName", "Will\nBe", "\nOn", "In #\nDays"]		
column_print_alignment = list(("right","center","center","right"))
# print(headers)
# print(column_print_alignment)
# print(birthday_list)
# print (tabulate(birthday_list, tablefmt='simple', colalign=column_print_alignment, headers=headers))

print(f"As of {tday.strftime('%B %d %Y')}: ")
print (tabulate(b, tablefmt='simple', colalign=column_print_alignment, headers=headers, floatfmt=".1f"))

# print(birthday_list)
# print(f" Bob's Birthday is in 98 days, that makes it on {tday + datetime.timedelta(days=98)}")
# print(f" Bill will be {2020 - 1961}")
#pbday = datetime.date(2020, 8, 12)
#till_bday = pbday - tday
#print (till_bday.days)

# pam_age = (tday - pam)
# print(f"Number of days until Pam's b-day is {pam_bday - tday}")
# pam_age_days = pam_age.days
# leelu_age = (tday - leelu)
# leelu_age_days = 7 * leelu_age.days

#print(f" Pam is {pam_age.days} days old = {pam_age_days}")
#print(f" Leelu is {7 * leelu_age.days} days old in dog-days = {leelu_age_days}")
# print(f" L: {leelu_age_days}, P: {pam_age_days}")

# i = 1
# print
# while leelu_age_days < pam_age_days:
# 	leelu_age_days += 7
# 	pam_age_days += 1
# 	i += 1

# tdelta = datetime.timedelta(days=i)
# date_of_equal = tday + tdelta
		
# print(f" L: {leelu_age_days}, P: {pam_age_days} in {i} days")
# print(f" This occurs on {date_of_equal} or {pam_age_days/365} years old")
# print(f" {.06027 * 365} days old")

#tdelta = datetime.timedelta(days=i)
#leelu_age = leelu_age + (tday + tdelta)
#leelu_age_days = (7 * leelu_age.days)
#pam_age = pam_age + (tday + tdelta)
#pam_age_days = (pam_age.days)
#i += 1

#print (f" # days from now = {i}")	
#date_same_age = tday + tdelta2	
#print(f" Pam and Leelu are {pam_age} days old on {date_same_age}")	
	
#print(tday + tdelta)

