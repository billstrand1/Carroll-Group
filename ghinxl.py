# Updated for Excel utilization

from tabulate import tabulate  # must use MENLO font in email
from datetime import datetime

# from openpyxl import load_workbook
# from pprint import pprint
import os
from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell

import pandas as pd

# contains the name dictionary and Player class, course handicap information, player status
from players import *

# cd documents/github/Carroll-Group

# --------------------Functions -Excel HI's-----------------------------
def get_indexes_from_xl_using_pandas():
    df = pd.read_excel(
        "Handicap Index Course Handicap Report.xlsx", sheet_name="Sheet1"
    )
    print("Sheet Loaded")

    i = 21
    report_date = df["Golfer Name"][i]

    for ind in range(19):
        golfer_name = df["Golfer Name"][ind]
        h_i = float(df["H.I."][ind])
        # print(f"Golfer Name: {golfer_name}, \nHI: {h_i}")

        # Update handicap info in Player Class, set playing to no.
        for player in player_list:
            # print(f"Entering player list with GN: {golfer_name}, PN: {player.ghin_name}")
            if golfer_name == player.ghin_name:
                # print(f"Processing: {golfer_name}")
                player.h_i = h_i
                player.class_tpc_white_70()
                player.class_tpc_white_72()
                player.class_cwv_white_71()
                player.class_road_tees()
                player.playing = False

    return report_date


def update_player_status(day_of_play):
    TOKEN = "0b2269ovtwyvi1bmbqm15c2kg9"
    smartsheet = Smartsheet(TOKEN)
    # id=1798700143011716	'Jack Sign-Up'
    sheet = smartsheet.sheets.get(id=1798700143011716)

    # create list of players for specific date
    monday_list = []
    tuesday_list = []
    wednesday_list = []
    thursday_list = []
    friday_list = []
    road_trip_list = []

    for row in sheet.rows:
        player = row.get_cell("Player").value

        monday_play = row.get_cell("Mon?").value
        if monday_play:
            monday_list.append(player)

        tuesday_play = row.get_cell("Tues?").value
        if tuesday_play:
            tuesday_list.append(player)

        wednesday_play = row.get_cell("Wed?").value
        if wednesday_play:
            wednesday_list.append(player)

        thursday_play = row.get_cell("Thurs?").value
        if thursday_play:
            thursday_list.append(player)

        friday_play = row.get_cell("Fri?").value
        if friday_play:
            friday_list.append(player)

        road_trip_play = row.get_cell("Road Trip?").value
        if road_trip_play:
            road_trip_list.append(player)

    if day_of_play == "M" or day_of_play == "m":
        display_day = "Monday Players"
        for player in player_list:
            if player.signup_name in monday_list:
                player.playing = True

    if day_of_play == "T" or day_of_play == "t":
        display_day = "Tuesday Players"
        for player in player_list:
            if player.signup_name in tuesday_list:
                player.playing = True

    elif day_of_play == "W" or day_of_play == "w":
        display_day = "Wednesday Players"
        for player in player_list:
            if player.signup_name in wednesday_list:
                player.playing = True

    elif day_of_play == "H" or day_of_play == "h":
        display_day = "Thursday Players"
        for player in player_list:
            if player.signup_name in thursday_list:
                player.playing = True

    elif day_of_play == "F" or day_of_play == "f":
        display_day = "Friday Players"
        for player in player_list:
            if player.signup_name in friday_list:
                player.playing = True

    elif day_of_play == "R" or day_of_play == "r":
        for player in player_list:
            if player.signup_name in road_trip_list:
                player.playing = True

    else:
        print("Bad choice of Day")

    return display_day


# ------------------PRINT OUT TABLE OF INDEXES / HANDICAPS / STROKES OFF LOW HANDICAP----------
def print_results_new(
    tpc_min_70,
    tpc_min_72,
    cwv_min,
    road_min,
    report_date,
    display_day,
    display_tee_times,
):
    today = (
        datetime.datetime.now()
    )  # was just datetime.now, but import of datetime in players.py changed that....
    today = today.strftime("%B %d, %Y")

    results_list = []

    choice = input("[T]PC, [C]WV?, or [R]oad > ")

    if choice == "T" or choice == "t":
        for player in player_list:
            if player.playing:
                results = [
                    player.signup_name,
                    player.h_i,
                    player.handicap_tpc_70,
                    player.handicap_tpc_70 - tpc_min_70,
                ]  # , player.handicap_tpc_72, player.handicap_tpc_72 - tpc_min_72]
                results_list.append(results)

        results_list.sort()
        # results_list.insert(0,["   ", "   ",  "TPC HCP", "TPC-70", "TPC HCP", "TPC-72"])
        # results_list.insert(1,["Name", "Index","Par 70", "Strks", "Par 72", "Strks"])
        headers = [
            "\nName",
            "\nIndex",
            "TPC HCP\nWhites",
            "TPC\n Strokes",
        ]  # , "TPC HCP\n Par 72", "TPC-72\nStrokes" ]
        column_print_alignment = list(
            ("right", "right", "right", "right")
        )  # , "right", "right"))
        course_info = f"TPC 70: CR = {tpc_rating_white_70} | SR = {tpc_slope_white_70} | Par = {tpc_hcp_70}"
        # course_info = course_info + f"TPC 72: CR = {tpc_rating_white_72} | SR = {tpc_slope_white_72} | Par = {tpc_hcp_72}"

    elif choice == "C" or choice == "c":
        for player in player_list:
            if player.playing:
                results = [
                    player.signup_name,
                    player.h_i,
                    player.handicap_cwv_71,
                    player.handicap_cwv_71 - cwv_min,
                ]
                results_list.append(results)

        results_list.sort()
        # results_list.insert(0,["   ", "   ", "CWV HCP", "CWV"])
        # results_list.insert(1,["Name", "Index","Par 71", "Strokes"])
        headers = [
            "\nName",
            "\nIndex",
            "CWV HCP\nWhites",
            "CWV\n Strokes",
        ]  # , "TPC HCP\n Par 72", "TPC-72\nStrokes" ]
        column_print_alignment = list(("right", "right", "right", "right"))
        course_info = f"CWV: CR = {cwv_rating_white_71} | SR = {cwv_slope_white_71} | Par = {cwv_hcp_71}"

    # ROAD TRIP - UPDATE DATA IN 'PLAYERS.PY'
    elif choice == "R" or choice == "r":
        for player in player_list:
            if player.playing:
                results = [
                    player.signup_name,
                    player.h_i,
                    player.handicap_road,
                    player.handicap_road - road_min,
                ]
                results_list.append(results)

        results_list.sort()
        # results_list.insert(0,["   ", "   ", "CWV HCP", "CWV"])
        # results_list.insert(1,["Name", "Index","Par 71", "Strokes"])
        headers = [
            "\nName",
            "\nIndex",
            "TXR HCP\nSilver",
            "TXR\n Strokes",
        ]  # , "TPC HCP\n Par 72", "TPC-72\nStrokes" ]
        column_print_alignment = list(("right", "right", "right", "right"))
        course_info = (
            f"TX Rangers: CR = {road_rating} | SR = {road_slope} | Par = {road_hcp}"
        )

    else:
        print("Bad Choice")

    # Finish printout:
    print("")
    print(f"{display_day} ({display_tee_times})")
    print("----------------------------------------")
    print(" \n Today's date:", today)
    print()
    print(
        tabulate(
            results_list,
            tablefmt="simple",
            colalign=column_print_alignment,
            headers=headers,
            floatfmt=".1f",
        )
    )
    print()
    print(course_info)
    print("Course Handicap = (H.I. x SR / 113) + (CR - Par)")
    print(f"GHIN Downloaded: {report_date}")
    print()
    # print('--------------------------------------------------------')
    for player in player_list:
        if player.playing:
            print(player.email)
    print("\n\n")
    # END-----------------PRINT OUT TABLE OF INDEXES / HANDICAPS / STROKES OFF LOW HANDICAP----------


def update_tee_times(display_day):
    """[Open "Tee Times" smartsheet and ]
    Arguments:
        display_day {[string]} -- [Day of Week Playing]
    """
    TOKEN = "0b2269ovtwyvi1bmbqm15c2kg9"
    smartsheet = Smartsheet(TOKEN)
    # id=8164839852926852	'Tee Times'
    sheet = smartsheet.sheets.get(id=8164839852926852)

    for row in sheet.rows:
        day = row.get_cell("Day").value
        tee_times = row.get_cell("Course / Tee Times").value
        # print(f"{display_day} / {day} {tee_times}")
        if (day + " Players") == display_day:
            print(f"Returning {tee_times}")
            return tee_times

        # if display_day == (row.get_cell("Day").value)

        # print(display_day)
        # break


def main():
    # Update the indexes of all players from the excel file
    report_date = get_indexes_from_xl_using_pandas()

    # get_indexes_from_xl_file()
    display_day = ""
    day_of_play = input("[M]on, [T]ues, [W]ed, T[h]urs, [F]ri?, or [R]oad?>")
    display_day = update_player_status(day_of_play)

    display_tee_times = ""
    display_tee_times = update_tee_times(display_day)

    print(f"Return from UPS display_day {display_day} and {display_tee_times}")
    # accumulate list of handicaps for sorting purposes
    tpc_list_70 = []
    tpc_list_72 = []
    cwv_list = []
    road_list = []

    # TODO:  Complete the Smartsheet sign-up list to update player.playing

    for player in player_list:
        if player.playing:
            tpc_list_70.append(player.handicap_tpc_70)
            tpc_list_72.append(player.handicap_tpc_72)
            cwv_list.append(player.handicap_cwv_71)
            road_list.append(player.handicap_road)

    # determine lowest handicaps
    tpc_list_70.sort()
    tpc_min_70 = tpc_list_70[0]  # lowest TPC70 handicap
    # print(f"TPC 70 Min: {tpc_min_70}")

    tpc_list_72.sort()
    tpc_min_72 = tpc_list_72[0]  # lowest TPC72 handicap
    # print(f"TPC 72 Min: {tpc_min_72}")

    cwv_list.sort()
    cwv_min = cwv_list[0]  # lowest CWV handicap
    # print(f"CWV Min: {cwv_min}")

    road_list.sort()
    road_min = road_list[0]  # lowest Road handicap

    print_results_new(
        tpc_min_70,
        tpc_min_72,
        cwv_min,
        road_min,
        report_date,
        display_day,
        display_tee_times,
    )


# --------------------START CODE EXECUTION-----------------------------

# <section class="golfer_lookup_section"> is copied to text file...

main()
