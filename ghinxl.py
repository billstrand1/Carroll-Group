# Updated for Excel utilization

from tabulate import tabulate
from datetime import datetime
from openpyxl import load_workbook
from pprint import pprint
import os

# contains the name dictionary and Player class, course handicap information
from players import *

# cd documents/github/Carroll-Group

#--------------------Functions -Excel HI's-----------------------------

#When using the File from Brechin
def get_indexes_from_xl_file():
	wb = load_workbook(filename = 'Handicap Index Course Handicap Report.xlsx')
	ws = wb['Sheet1']

	#Retrieve the player's indexes, compute handicaps
	for i in range(2, 21):
		golfer_name = (ws.cell(row=i, column=3).value)
		h_i = (float(ws.cell(row=i, column=4).value))


		for guy in player_list:
			if golfer_name == guy.ghin_name:
				guy.h_i = h_i
				guy.class_tpc_white_70()
				guy.class_cwv_white_71()
				# print (f" {golfer_name}, hi: {guy.h_i}, tpc: {guy.handicap_tpc_70} cwv: {guy.handicap_cwv_71}")


#----------------------Functions end-------------------------------
def main():
	# print('-------------------------------------------------------')
	today = datetime.now()

	get_indexes_from_xl_file()

	tpc_list = []  #accumulate list of handicaps for sorting purposes
	cwv_list = []  #accumulate list of handicaps for sorting purposes

	#TODO:  Complete the Smartsheet sign-up list to update player.playing

	for guy in player_list:
		if guy.playing:
			tpc_list.append(guy.handicap_tpc_70)
			cwv_list.append(guy.handicap_cwv_71)
 #---------------------------------------------------

	#determine lowest handicap
	tpc_list.sort()
	tpc_min = tpc_list[0] #lowest TPC handicap
	cwv_list.sort()
	cwv_min = cwv_list[0] #lowest CWV handicap

	choice = input ("[T]PC, [C]WV, or [B]oth? > ")

	if choice == 'B' or choice == 'b':
		results_list = []
		for player in player_list:
			if player.playing:
				results = [player.signup_name, player.h_i, player.handicap_tpc_70, player.handicap_tpc_70-tpc_min, player.handicap_cwv_71, player.handicap_cwv_71-cwv_min]
				results_list.append(results)

		results_list.sort()
		results_list.insert(0,["   ", "   ",  "TPC", "TPC", "CWV", "CWV"])
		results_list.insert(1,["Name", "Index","(70)", "Strks", "(71)", "Strks"])
		today = datetime.now()
		today = today.strftime("%B %d, %Y")

		print('-------------------------------------------------------')
		print("\n \n Today's date:", today)
		print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		print (f"TPC: CR = {tpc_rating_white_70} | SR = {tpc_slope_white_70} | Par = {tpc_hcp_70} \nCWV: CR = {cwv_rating_white_71} | SR = {cwv_slope_white_71} | Par = {cwv_hcp_71}")
		# print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		# print ('  (Course Rating - Par)')
		print ('Course Handicap = (H.I. x SR / 113) + (CR - Par)')
		print('--------------------------------------------------------')

	elif choice == 'T' or choice == 't':
		results_list = []
		for player in player_list:
			if player.playing:
				results = [player.signup_name, player.h_i, player.handicap_tpc_70, player.handicap_tpc_70-tpc_min] #, player.handicap_cwv, player.handicap_cwv-cwv_min]
				results_list.append(results)

		results_list.sort()
		results_list.insert(0,["   ", "   ",  "TPC HCP", "TPC"])
		results_list.insert(1,["Name", "Index","Par 70", "Strokes"])
		today = datetime.now()
		today = today.strftime("%B %d, %Y")

		print('-------------------------------------------------------')
		print("\n \n Today's date:", today)
		print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		# print (f"TPC: {tpc_rating_white_70} / {tpc_slope_white_70} / Par {tpc_hcp_70}")
		# print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		# print ('  (Course Rating - Par)')

		print (f"TPC: CR = {tpc_rating_white_70} | SR = {tpc_slope_white_70} | Par = {tpc_hcp_70}")
		print ('Course Handicap = (H.I. x SR / 113) + (CR - Par)')
		# print ('  (Course Rating - Par)')

		print('--------------------------------------------------------')

	elif choice == 'C' or choice == 'c':
		results_list = []
		for player in player_list:
			if player.playing:
				results = [player.signup_name, player.h_i, player.handicap_cwv_71, player.handicap_cwv_71-cwv_min]
				results_list.append(results)

		results_list.sort()
		results_list.insert(0,["   ", "   ", "CWV HCP", "CWV"])
		results_list.insert(1,["Name", "Index","Par 71", "Strokes"])
		today = datetime.now()
		today = today.strftime("%B %d, %Y")

		print('-------------------------------------------------------')
		print("\n \n Today's date:", today)

		print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		print (f"CWV: CR = {cwv_rating_white_71} | SR = {cwv_slope_white_71} | Par = {cwv_hcp_71}")
		# print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		# print ('  (Course Rating - Par)')
		print ('Course Handicap = (H.I. x SR / 113) + (CR - Par)')
		print('--------------------------------------------------------')

	for player in player_list:
		if player.playing:
			print (player.email)
	print("\n\n")
# --------------------------------------
def AllHandicaps(f_h_i):
	f_h_i = input ("Your Handicap Index: ")
	f_h_i = float(f_h_i)
	print (f"Your Handicap Index: {f_h_i}")
	print (f"Your Handicaps:  ")

		# TPC 70 White
	handicap_tpc = compute_handicap_tpc(f_h_i, tpc_slope_white_70, tpc_rating_white_70, tpc_hcp_70)
	print (f' TPC White Par 70:  {handicap_tpc}, ({tpc_slope_white_70} / {tpc_rating_white_70}, / {tpc_hcp_70})')

		# TPC 70 Gold
	handicap_tpc = compute_handicap_tpc(f_h_i, tpc_slope_gold_70, tpc_rating_gold_70, tpc_hcp_70)
	print (f' TPC Gold  Par 70:  {handicap_tpc}, ({tpc_slope_gold_70} / {tpc_rating_gold_70}, / {tpc_hcp_70})')

		# TPC 70 Blue
	handicap_tpc = compute_handicap_tpc(f_h_i, tpc_slope_blue_70, tpc_rating_blue_70, tpc_hcp_70)
	print (f' TPC Blue  Par 70:  {handicap_tpc}, ({tpc_slope_blue_70} / {tpc_rating_blue_70}, / {tpc_hcp_70})')

	print("")
		# TPC 72 White
	handicap_tpc = compute_handicap_tpc(f_h_i, tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72)
	print (f' TPC White Par 72:  {handicap_tpc}, ({tpc_slope_white_72} / {tpc_rating_white_72}, / {tpc_hcp_72})')

	# TPC 72 Gold
	handicap_tpc = compute_handicap_tpc(f_h_i, tpc_slope_gold_72, tpc_rating_gold_72, tpc_hcp_72)
	print (f' TPC Gold  Par 72:  {handicap_tpc}, ({tpc_slope_gold_72} / {tpc_rating_gold_72}, / {tpc_hcp_72})')

	# TPC 72 Blue
	handicap_tpc = compute_handicap_tpc(f_h_i, tpc_slope_blue_72, tpc_rating_blue_72, tpc_hcp_72)
	print (f' TPC Blue  Par 72:  {handicap_tpc}, ({tpc_slope_blue_72} / {tpc_rating_blue_72}, / {tpc_hcp_72})')

	print("")
	# CWV 71 White
	handicap_cwv = compute_handicap_cwv(f_h_i, cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
	print (f' CWV White Par 71:  {handicap_cwv}, ({cwv_slope_white_71} / {cwv_rating_white_71}, / {cwv_hcp_71})')		
	# CWV 71 Gold
	handicap_cwv = compute_handicap_cwv(f_h_i, cwv_slope_gold_71, cwv_rating_gold_71, cwv_hcp_71)
	print (f' CWV Gold  Par 71:  {handicap_cwv}, ({cwv_slope_gold_71} / {cwv_rating_gold_71}, / {cwv_hcp_71})')		

	# CWV 71 Blue				
	handicap_cwv = compute_handicap_cwv(f_h_i, cwv_slope_blue_71, cwv_rating_blue_71, cwv_hcp_71)
	print (f' CWV Blue  Par 71:  {handicap_cwv}, ({cwv_slope_blue_71} / {cwv_rating_blue_71}, / {cwv_hcp_71})')		
	
#--------------------START CODE EXECUTION-----------------------------

# <section class="golfer_lookup_section"> is copied to text file...

main()

# AllHandicaps('0')