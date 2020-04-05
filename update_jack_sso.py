#! /usr/bin/env python3
# Sheet ID: 4864657262438276

import smartsheet
import logging
# import os.path
# import pprint

# from datetime import date
# from datetime import datetime
# import schedule
# import time
# import smtplib

'''
4/3/20:  Can read all info and print out.  
Need to figure out updating the date cells to 'None'

'''
TOKEN = '0b2269ovtwyvi1bmbqm15c2kg9'
access_token = TOKEN

jack_signup_sheet = 1798700143011716


# Helper function to find cell in a row
column_map = {}
def get_cell_by_column_name(row, column_name):
    column_id = column_map[column_name]
    return row.get_column(column_id)


def review_Jack_Signup_rows(source_row):
        player_cell = get_cell_by_column_name(source_row, "Player")
        player = player_cell.display_value

        mon_cell = get_cell_by_column_name(source_row, "Mon?")
        mon = mon_cell.value

        wed_cell = get_cell_by_column_name(source_row, "Wed?")
        wed = wed_cell.value

        fri_cell = get_cell_by_column_name(source_row, "Fri?")
        fri = fri_cell.value

        test_cell = get_cell_by_column_name(source_row, "Test")
        test = test_cell.display_value

        print(f"{player} in row {row.id} to be updated, M:{mon}, W:{wed}, F:{fri} T:{test}")

        # mon.value = 'None'
        # wed.value = 'None'
        # fri.value = 'None'

        test_cell.display_value = 'NEW'
        # sheet.update_row(source_row.id)



#-------------------------Code Starts---------------------------
# Load entire sheet
smart = smartsheet.Smartsheet(access_token)

sheet = smart.Sheets.get_sheet(sheet_id=jack_signup_sheet)
print("Loaded " + str(len(sheet.rows)) + " rows from sheet: " + sheet.name)
print()

column_map = {}
for column in sheet.columns:
    column_map[column.title] = column.id
    
# Works, all column titles / id's mapped
# for k, v in column_map.items():
#     print(f"K: {k}, V: {v}")



rowsToUpdate = []

for row in sheet.rows:
    rowToUpdate = review_Jack_Signup_rows(row)
    if rowToUpdate: # is not None:
        rowsToUpdate.append(rowToUpdate)

# review_Jack_Signup_rows()
