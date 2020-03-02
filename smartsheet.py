#! /usr/bin/env python3
# Sheet ID: 4864657262438276


# import smartsheet
# import logging

from datetime import date
from datetime import datetime
from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell

# importing for scheduling an email
# import schedule
# import time
# import smtplib

import pprint

#-------------Simple Smartsheet-------------------

TOKEN = '0b2269ovtwyvi1bmbqm15c2kg9'
smartsheet = Smartsheet(TOKEN)
# getting the sheet by name
# JackSignUp = 1798700143011716

sheet = smartsheet.sheets.get('Jack Sign-Up')

# getting columns details by column title (case-sensitive)
# player_name = sheet.get_column("Player")
# pprint(player_name.__dict__)
# friday_data = sheet.get_column("Fri?")
# pprint(friday_play_column.__dict__)


#-------------Simple Smartsheet-------------------



#---------------------
# getting a specific cell and updating it:
#TODO - REVISE PROGRAM TO RUN WITH SMARTSHEET ONLY, NOT SIMPLE_SMARTSHEET


# def delete_all_rows():
#     today = datetime.now()
#     today = today.strftime("%B %d, %Y %H:%M")
#     print("Today's date: ", today)
#     print("Delete the Sign-ups")

#     row_id_to_delete = []
#     for row in sheet.rows:
#         row_id_to_delete = row.id
#         player = row.get_cell("Player").value
#         print(f"{player} in row {row_id_to_delete} deleted")
#         # sheet.delete_row(row_id_to_delete)
#     print ('Done, now sending email')

#     sender = "tcmensgolf@gmail.com"
#     password = "tcmensgolf2020" # Your SMTP password for Gmail
#     recipient = "billstrand1@yahoo.com"
#     subject = "Signed Up"
#     text = "Hello from Python\nThis is line 2\nAnd line 3\n Sent from Schedule at 14:00"

#     smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     smtp_server.login(sender, password)
#     message = "From: Friday & Saturday Mens Golf \nSubject: {}\n\n{}".format(subject, text)
#     smtp_server.sendmail(sender, recipient, message)
#     smtp_server.close()


# schedule.every().saturday.at('14:00').do(delete_all_rows)

# delete_all_rows()

# print('Scheduling Delete Rows at 14:00 on Saturday')
# while 1:
#     schedule.run_pending()
#     time.sleep(1)


#----------------------


#Creat a list of players on each day:
monday_list = [] 
wednesday_list = []
friday_list = [] 

for row in sheet.rows:
    player = row.get_cell("Player").value
    monday_play = row.get_cell("Mon?").value
    if monday_play: monday_list.append(player)

    wednesday_play = row.get_cell("Wed?").value
    if wednesday_play: wednesday_list.append(player)

    friday_play = row.get_cell("Fri?").value
    if friday_play: friday_list.append(player)
    print(f"{player}, Mon:{monday_play}, Wed:{wednesday_play}, Fri: {friday_play}")


# s_monday_list = sorted(monday_list)
print("Monday:")
pprint(monday_list
print ('')

# s_wednesday_list = sorted(wednesday_list)
print("Wednesday")
pprint (wednesday_list)
print ('')

# s_friday_list = sorted(friday_list)
print("Friday :")
pprint(friday_list)

#-----------------------Tried Smartsheet directly-----
# smart = smartsheet.Smartsheet(TOKEN)
# smart.errors_as_exceptions(True)

# jack_sheet = 1798700143011716
# sheet = smart.Sheets.get_sheet(sheet_id=jack_sheet)

# def map_the_columns():
#     # Build column map for later reference - translates column names to column id.  column_map is a dict defined above
#     for column in sheet.columns:
#         column_map[column.title] = column.id


# column_map = {}
# def get_cell_by_column_name(row, column_name):
#     column_id = column_map[column_name]
#     return row.get_column(column_id)



