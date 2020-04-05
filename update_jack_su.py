#! /usr/bin/env python3
# Sheet ID: 4864657262438276

#Enter a new comment at 11:53am
#After revert from 11:56, re-comment at 11:57

from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell

from datetime import date
from datetime import datetime
import schedule
import time
import smtplib

TOKEN = '0b2269ovtwyvi1bmbqm15c2kg9'
smartsheet = Smartsheet(TOKEN)

# getting the sheet by name



# getting columns details by column title (case-sensitive)
# player_column = sheet.get_column("Player")
# pprint(player_column.__dict__)
# friday_play_column = sheet.get_column("Fri?")
# pprint(friday_play_column.__dict__)



#---------------------
# getting a specific cell and updating it:
#TODO - REVISE PROGRAM TO RUN WITH SMARTSHEET ONLY, NOT SIMPLE_SMARTSHEET


    # print ('Done, now sending email')

    # sender = "tcmensgolf@gmail.com"
    # password = "tcmensgolf2020" # Your SMTP password for Gmail
    # recipient = "billstrand1@yahoo.com"
    # subject = "Deleted Sign-Up Rows"
    # text = "Hello from Python\nThis is line 2\nAnd line 3\n Sent from Schedule at 14:00"

    # smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # smtp_server.login(sender, password)
    # message = "From: Friday & Saturday Mens Golf \nSubject: {}\n\n{}".format(subject, text)
    # smtp_server.sendmail(sender, recipient, message)
    # smtp_server.close()

def delete_Jack_Signup_rows():
    sheet = smartsheet.sheets.get('Jack Sign-Up')
    row_id_to_update = []
    for row in sheet.rows:
        row_id_to_update.append(row.id)
        player = row.get_cell("Player").value
        mon = row.get_cell("Mon?").value
        wed = row.get_cell("Wed?").value
        fri = row.get_cell("Fri?").value
        test = row.get_cell("Test").display_value
        print(f"{player} in row {row.id} to be updated, M:{mon}, W:{wed}, F:{fri} T:{test}")

        # mon.displayValue = 'None'
        # wed.displayValue = 'None'
        # fri.displayValue = 'None'

        test.value = 'NEW'
        sheet.update_row(row_id_to_update)

        # smartsheet.sheets.update_rows('Jack Sign-Up', row_id_to_update)
        

    # print ('Done, now sending email')
  


# schedule.every().saturday.at('14:00').do(delete_all_rows)

delete_Jack_Signup_rows()

# print('Scheduling Delete Rows at 14:00 on Saturday')
# while 1:
#     schedule.run_pending()
#     time.sleep(1)


#----------------------
# getting a specific cell and updating it:
# row_id_to_delete = None
# rows_to_update = []
# friday_only = [] 
# saturday_only = [] 
# both_days = []

# for row in sheet.rows:
#     player = row.get_cell("Player").value
#     friday_play = row.get_cell("Fri?").value
#     saturday_play = row.get_cell("Sat?").value

#     if friday_play and saturday_play:
#         both_days.append(player)
#         # print(f"{player} is playing Both Days.")
#     elif friday_play:
#         friday_only.append(player)
#         # print(f"{player} is playing Friday Only.")
#     elif saturday_play:
#         saturday_only.append(player)
#         # print(f"{player} is playing Saturday Only.")  

# s_both_days = sorted(both_days)
# pprint("Both Days:")
# pprint (s_both_days)
# pprint ('')

# s_friday_only = sorted(friday_only)
# pprint("Friday Only:")
# pprint(s_friday_only)

# s_saturday_only = sorted(saturday_only)
# pprint("Saturday Only:")
# pprint(s_saturday_only)



