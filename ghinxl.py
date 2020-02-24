# Updated for Excel utilization


from tabulate import tabulate
from datetime import datetime
from openpyxl import load_workbook
from pprint import pprint
import os

# contains the name dictionary and Player class
# contains the course handicap information
from players import *

# "Under the new WHS, however, course handicaps reflect the strokes you get in relation to par with a subtle but significant change to the formula.""
# Course Handicap = Handicap Index x (Slope Rating/113) + (Course Rating - par)

# TODO: Remove one of these and make it a generic compute handicap
def compute_handicap_tpc(h_i, slope, rating, handicap): 
	return (round ((h_i * slope / 113) + (rating - handicap))) 

def compute_handicap_cwv(h_i, slope, rating, handicap):
	return (round ((h_i * slope / 113) + (rating - handicap)))  


#--------------------START CODE EXECUTION -Excel HI's-----------------------------
#------------------------file start-------------------------------

#When using the File from Brechin
def get_index_from_xl_file():
	wb = load_workbook(filename = 'Handicap Index Course Handicap Report.xlsx')
	# pprint ('load_workbook worked into wb')

	ws = wb['Sheet1']
	# pprint ('sheet loaded into ws')

	#Retrieve the player's indexes
	player_dict = {}
	#WORKS, print range of cells
	for i in range(2, 21):
		golfer_name = (ws.cell(row=i, column=3).value)
		h_i = (float(ws.cell(row=i, column=4).value))
		for guy in player_list:
			if golfer_name == guy.ghin_name:
				guy.h_i = h_i
				guy.class_tpc_white_70()
				guy.class_cwv_white_71()

	# for guy in player_list:
		# print(f"{guy.signup_name} HI = {guy.h_i}")



		# returning all players
		player_dict[str(golfer_name)] = str(h_i)
		
		# returning only players that are playing
		#To confirm if golfer is playing
		# status = input(f'Is {golfer_name} playing?')
		# if status == 'y':
			# player_dict[str(golfer_name)] = str(h_i)

	# pprint(player_dict)

	return(player_dict) 

#------------------------file end-------------------------------
def main():
	# print('-------------------------------------------------------')
	today = datetime.now()

	player_dict = get_index_from_xl_file()

	tpc_list = []  #accumulate list of handicaps for sorting purposes
	cwv_list = []  #accumulate list of handicaps for sorting purposes

#----------------Try using Players Class -------------	LATER
	#print player names in player class list
	#TODO:  Complete the Smartsheet sign-up list and
	# add a 'signed-up' variable to the Player class.
	#Once updated, limit the player_dict to those signed-up and print
	#out their email addresses below the table... then only email to 
	#those signed up.

	for player in player_dict:
		h_i = float(player_dict[player])
		name = player
		for player_in_class in player_list:
			if name == player_in_class.ghin_name:
				player_in_class.h_i = h_i
				# player_in_class.handicap_tpc = player_in_class.class_tpc_white_72()
				# player_in_class.handicap_cwv = player_in_class.class_cwv_white_71()
				player_in_class.class_tpc_white_70()
				player_in_class.class_cwv_white_71()

	for guy in player_list:
		print (f'{guy.signup_name} = {guy.h_i}, TPC = {guy.handicap_tpc}, CWV = {guy.handicap_cwv}')
		tpc_list.append(guy.handicap_tpc)
		cwv_list.append(guy.handicap_cwv)

			# if name == person.signup_name:
				# print (f' {name} matches {person.signup_name}')


		# handicap_tpc = compute_handicap_tpc(h_i, tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72) 
		# tpc_list.append(handicap_tpc)
		# handicap_cwv = compute_handicap_cwv(h_i, cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
		# cwv_list.append(handicap_cwv)
		# print(f"Name: {name} Index: {h_i}, TPC: {handicap_tpc}, CWV: {handicap_cwv}")
# #---------------------------------------------------

	# print ('computing handicaps')
	# for player in player_dict:
	# 	h_i = float(player_dict[player])
	# 	name = player

	# 	handicap_tpc = compute_handicap_tpc(h_i, tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72) 
	# 	tpc_list.append(handicap_tpc)
	# 	handicap_cwv = compute_handicap_cwv(h_i, cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
	# 	cwv_list.append(handicap_cwv)
	# 	# print(f"Name: {name} Index: {h_i}, TPC: {handicap_tpc}, CWV: {handicap_cwv}")


	#determine lowest handicap
	tpc_list.sort()
	tpc_min = tpc_list[0] #lowest TPC handicap
	cwv_list.sort()
	cwv_min = cwv_list[0] #lowest CWV handicap


	choice = input ("[T]PC, [C]WV, or [B]oth? > ")

	if choice == 'B' or choice == 'b':
		#for printing purposes only, REDUNDANT from above
		results_list = []
		for player in player_dict:
			tpc_handicap = compute_handicap_tpc(float(player_dict[player]), tpc_slope_white_70, tpc_rating_white_70, tpc_hcp_70)
			cwv_handicap = compute_handicap_cwv(float(player_dict[player]), cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
			# print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
			results = [name_dict[player], player_dict[player], tpc_handicap, tpc_handicap-tpc_min, cwv_handicap, cwv_handicap-cwv_min]
			results_list.append(results)

		results_list.sort()
		results_list.insert(0,["   ", "   ",  "TPC", "TPC", "CWV", "CWV"])
		results_list.insert(1,["Name", "Index","(70)", "Strks", "(71)", "Strks"])
		today = datetime.now()
		today = today.strftime("%B %d, %Y")

		print('-------------------------------------------------------')
		print("\n \n Today's date:", today)


		print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		print (f"TPC: {tpc_rating_white_70} / {tpc_slope_white_70} / Par {tpc_hcp_70} \nCWV: {cwv_rating_white_71} / {cwv_slope_white_71} / Par {cwv_hcp_71}")
		print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		print ('  (Course Rating - Par)')
		# print(f"File name: {file_name}")
		print('--------------------------------------------------------')

	elif choice == 'T' or choice == 't':
		results_list = []
		for player in player_dict:
			tpc_handicap = compute_handicap_tpc(float(player_dict[player]), tpc_slope_white_70, tpc_rating_white_70, tpc_hcp_70)
			# tpc_handicap = compute_handicap_tpc(float(player_dict[player]), tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72)
			# cwv_handicap = compute_handicap_cwv(float(player_dict[player]), cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
			# print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
			results = [name_dict[player], player_dict[player], tpc_handicap, tpc_handicap-tpc_min] #, cwv_handicap, cwv_handicap-cwv_min]
			results_list.append(results)

		results_list.sort()
		results_list.insert(0,["   ", "   ",  "TPC HCP", "TPC"])
		results_list.insert(1,["Name", "Index","Par 70", "Strokes"])
		today = datetime.now()
		today = today.strftime("%B %d, %Y")


		print('-------------------------------------------------------')
		print("\n \n Today's date:", today)


		print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		print (f"TPC: {tpc_rating_white_70} / {tpc_slope_white_70} / Par {tpc_hcp_70}")
		print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		print ('  (Course Rating - Par)')
		# print(f"File name: {file_name}")
		print('--------------------------------------------------------')


	elif choice == 'C' or choice == 'c':
		results_list = []
		for player in player_dict:
			# tpc_handicap = compute_handicap_tpc(float(player_dict[player]), tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72)
			cwv_handicap = compute_handicap_cwv(float(player_dict[player]), cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
			# print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
			results = [name_dict[player], player_dict[player], cwv_handicap, cwv_handicap-cwv_min]
			results_list.append(results)

		results_list.sort()
		results_list.insert(0,["   ", "   ", "CWV HCP", "CWV"])
		results_list.insert(1,["Name", "Index","Par 71", "Strokes"])
		today = datetime.now()
		today = today.strftime("%B %d, %Y")

		print('-------------------------------------------------------')
		print("\n \n Today's date:", today)

		print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		print (f"CWV: {cwv_rating_white_71} / {cwv_slope_white_71} / Par {cwv_hcp_71}")
		print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		print ('  (Course Rating - Par)')
		# print(f"File name: {file_name}")
		print('--------------------------------------------------------')


	#------------- OLD-----------
	# print('-------------------------------------------------------')
	# print("\n \n Today's date:", today)

	# print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
	# print (f"TPC: {tpc_rating_white_72} / {tpc_slope_white_72} / Par {tpc_hcp_72} \nCWV: {cwv_rating_white_71} / {cwv_slope_white_71} / Par {cwv_hcp_71}")
	# print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
	# print ('  (Course Rating - Par)')
	# print('--------------------------------------------------------')

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