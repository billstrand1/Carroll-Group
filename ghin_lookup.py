#ghin_lookup.py
#uploaded to Git, test comment update.
# CALCS ARE FOR TPC WHITE PAR 72...

from tabulate import tabulate
import re
from datetime import datetime
from bs4 import BeautifulSoup
import pprint

#------------------------file start-------------------------------
def get_index_from_text_file_OLD(file_name):
	print('enter get_index_from_text_file')
	player_dict = {}
	pg = open(file_name)
	page = str(pg.read())

	name = re.findall('name">(.*?)<', str(page)) 

	# find handicap index from string, will only pull out leading '>'
	index = re.findall('>[0-9]+.[0-9]', str(page)) #index_text

	index_2 = []	# remove leading '>'
	for item in index:
		item = item[1:] #slice from position 1 on...
		index_2.append(item)

	zipObj = zip(name, index_2) #create a dict from 2 lists
	player_dict = dict(zipObj)
	bill_index = input ("Bill's Index? ")
	player_dict['Bill Strand'] = bill_index
	# print (f'player_dict: \n {player_dict}')
	return (player_dict)
#------------------------file end-------------------------------
def get_index_from_prefilled_dict():  #pre-defined for testing only
	return ({'Al Vela': '15.7',
		'Rick Besse': '15.7',
		'Bill Barnard': '16.0',
		'Bill Strand': '11.3',
		'Bob Heard': '6.2',

		'Curt Fitzgerald': '17.0',
		'Dan Stewart': '13.1',
		'Doug Williams': '18.9',
		'Frank Broyles': '14.8',
		'Richard Humphrey': '16.6',
		'Jack Carroll': '10.1',
		'Jim Sido': '8.8',
		'Jimmy Wickham': '14.0',
		'Kent Fannon': '12.9',
		'Larry Traub': '8.3',
		'Reid Baker': '11.3',
		'Rocky Duron': '16.2', 
		'Rick Baumgarth': '9.2',
	    'Will Davis': '12.3' })

# Under the new WHS, however, course handicaps reflect the strokes you get in relation to par with a subtle but significant change to the formula.
# Course Handicap = Handicap Index x (Slope Rating/113) + (Course Rating - par)

def compute_handicap_tpc(h_i, slope, rating, handicap): 
	return (round ((h_i * slope / 113) + (rating - handicap))) 

def compute_handicap_cwv(h_i, slope, rating, handicap):
	return (round ((h_i * slope / 113) + (rating - handicap)))  

#--------------------START LIST, DICT DEFINITIONS-----------------------------
tpc_hcp_70 = 70
tpc_hcp_72 = 72

tpc_slope_white_70 = 128
tpc_rating_white_70 = 69.4

tpc_slope_white_72 = 127
tpc_rating_white_72 = 70.1

tpc_slope_gold_70 = 132
tpc_rating_gold_70 = 70.2

tpc_slope_gold_72 = 133
tpc_rating_gold_72 = 70.8

tpc_slope_blue_70 = 136
tpc_rating_blue_70 = 72.0

tpc_slope_blue_72 = 137
tpc_rating_blue_72 = 72.4


cwv_hcp_71 = 71

cwv_slope_white_71 = 130
cwv_rating_white_71 = 69.3

cwv_slope_gold_71 = 132
cwv_rating_gold_71 = 70.3

cwv_slope_blue_71 = 134
cwv_rating_blue_71 = 71.2

name_dict = {'Jack Carroll': 'Jack', 
	'Bob Heard': 'Bob H.', 
	'Larry Traub': 'Larry', 
	'Jim Sido': 'Jim S.', 
	'Curt Fitzgerald': 'Curt', 
	'Jimmy Wickham': 'Jimmy', 
	'Richard Humphrey': 'Hump', 
	'Kent Fannon': 'Kent', 
	'Bill Barnard': 'Bill B.', 
	'Doug Williams': 'Doug', 
	'Rocky Duron': 'Rocky', 
	'Will Davis': 'Will', 
	'Reid Baker': 'Reid', 
	'Bill Strand': 'Bill S.', 
	'Rick Baumgarth': 'Trick', 
	'Rick Besse': 'Besse', 
	'Dan Stewart': 'Dan', 
	'Al Vela': 'Al', 
	'Frank Broyles': 'Frank'}

# Create new GHIN list alphabetically:

ghin = ['3660253', #	Reid
	'5910694', #	Bill B
	'3660265', #	Trick
	'3660283', #	Besse
	'2379621', #	Frank
	'3660366', #	Jack
	'1815996', #	Will
	'3720105', #	Rocky
	'3660486', #	Kent
	'2379581', #	Curt
	'3660603', #	Bob H.
	'3660992', #	Hump
	'4787165', #	Jim S.
	'7701708', #	Dan
	'0053161', #	Bill S.
	'4548474', #	Larry
	'3661029', #	Al
	'3661053', #	Jimmy W.
	'3661061'] #	Doug

#--------------------START CODE EXECUTION-----------------------------
def main_OLD():
	# print('Program starts')
	file_name = input ("What is the input filename? > ")
	# print('calling get_index_from_text_file')
	player_dict = get_index_from_text_file_OLD(file_name) #take copy/pasted html and save to file named: 2020-01-05.txt


	tpc_list = []  #accumulate list of handicaps for sorting purposes
	cwv_list = []  #accumulate list of handicaps for sorting purposes

	# print ('computing handicaps')
	for player in player_dict:
		h_i = float(player_dict[player])
		name = player

		handicap_tpc = compute_handicap_tpc(h_i, tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72) 
		tpc_list.append(handicap_tpc)
		handicap_cwv = compute_handicap_cwv(h_i, cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
		cwv_list.append(handicap_cwv)
		# print(f"Name: {name} Index: {h_i}, TPC: {handicap_tpc}, CWV: {handicap_cwv}")


	#determine lowest handicap
	tpc_list.sort()
	tpc_min = tpc_list[0] #lowest TPC handicap
	cwv_list.sort()
	cwv_min = cwv_list[0] #lowest CWV handicap


	#for printing purposes only, REDUNDANT from above
	# results_list = [["   ", "   ",  "TPC", "TPC", "CWV", "CWV"], ["Name", "Index","HCP", "Strokes", "HCP", "Strokes"]]#, ["-------","-----",  "---",  "-------",  "---",  "-------"]]
	results_list = []
	for player in player_dict:
		tpc_handicap = compute_handicap_tpc(float(player_dict[player]), tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72)
		cwv_handicap = compute_handicap_cwv(float(player_dict[player]), cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
		# print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
		results = [name_dict[player], player_dict[player], tpc_handicap, tpc_handicap-tpc_min, cwv_handicap, cwv_handicap-cwv_min]
		results_list.append(results)

	results_list.sort()
	results_list.insert(0,["   ", "   ",  "TPC", "TPC", "CWV", "CWV"])
	results_list.insert(1,["Name", "Index","(72)", "Strks", "(71)", "Strks"])
	today = datetime.now()
	today = today.strftime("%B %d, %Y %H:%M")

	# print('-------------------------------------------------------')
	print("\n \n Today's date:", today)

	print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
	print (f"TPC: {tpc_rating_white_72} / {tpc_slope_white_72} / Par {tpc_hcp_72} \nCWV: {cwv_rating_white_71} / {cwv_slope_white_71} / Par {cwv_hcp_71}")
	print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
	print ('  (Course Rating - Par)')
	print('--------------------------------------------------------')

#--------------------START CODE EXECUTION - TRY BEAUTIFUL SOUP-----------------------------
#------------------------file start-------------------------------
def get_index_from_text_file2(file_name):
	# print('enter get_index_from_text_file')
	player_dict = {}
	pg = open(file_name)
	soup = BeautifulSoup(pg, 'lxml')
	# print(soup)
	index = 0
	# no good: players = soup.find('div', class_='panel')

#-----TRY MULTI PLAYER WITH FINDALL--
	players = soup.find_all('span', class_='item')
	# print(type(players))

	for item in players: #soup.find_all('span', class_='item'):
		# print (item)
		# print()
		player = item.a.span.text #works for full name
		# print(player)

		soup2 = BeautifulSoup(str(item), 'lxml')
		index = soup2.find('a', class_='item index') #works
		# index = players.a.text
		# print(index.text)
		# print()
		player_dict[str(player)] = str(index.text)
	
	bill_index = input ("Bill's Index? ")
	player_dict['Bill Strand'] = bill_index
	return(player_dict)

	# player = players.a.span.text #works for full name
	# print(player)

	# index = soup.find('a', class_='item index') #works
	# # index = players.a.text
	# print(index.text)

# #-----WORKS FOR FIRST PLAYER-------------
# 	players = soup.find('span', class_='item')
# 	# print (players)

# 	player = players.a.span.text #works for full name
# 	print(player)

# 	index = soup.find('a', class_='item index') #works
# 	# index = players.a.text
# 	print(index.text)
# -----WORKS FOR FIRST PLAYER-------------

# OLD CODE
	# page = str(pg.read())
	# name = re.findall('name">(.*?)<', str(page)) 

	# # find handicap index from string, will only pull out leading '>'
	# index = re.findall('>[0-9]+.[0-9]', str(page)) #index_text

	# index_2 = []	# remove leading '>'
	# for item in index:
	# 	item = item[1:] #slice from position 1 on...
	# 	index_2.append(item)

	# zipObj = zip(name, index_2) #create a dict from 2 lists
	# player_dict = dict(zipObj)
	# bill_index = input ("Bill's Index? ")
	# player_dict['Bill Strand'] = bill_index
	# print (f'player_dict: \n {player_dict}')



#------------------------file end-------------------------------
def main2():
	print('MAIN2, TESTING FOR BEAUTIFUL SOUP')
	print('-------------------------------------------------------')
	file_name = input ("What is the input filename? > ")
	# print('calling get_index_from_text_file')
	# player_dict = get_index_from_text_file2(file_name) #take copy/pasted html and save to file named: 2020-01-05.txt
	player_dict = get_index_from_text_file2(file_name) #player_dict = 

	tpc_list = []  #accumulate list of handicaps for sorting purposes
	cwv_list = []  #accumulate list of handicaps for sorting purposes

	# print ('computing handicaps')
	for player in player_dict:
		h_i = float(player_dict[player])
		name = player

		handicap_tpc = compute_handicap_tpc(h_i, tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72) 
		tpc_list.append(handicap_tpc)
		handicap_cwv = compute_handicap_cwv(h_i, cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
		cwv_list.append(handicap_cwv)
		# print(f"Name: {name} Index: {h_i}, TPC: {handicap_tpc}, CWV: {handicap_cwv}")


	#determine lowest handicap
	tpc_list.sort()
	tpc_min = tpc_list[0] #lowest TPC handicap
	cwv_list.sort()
	cwv_min = cwv_list[0] #lowest CWV handicap


	#for printing purposes only, REDUNDANT from above
	# results_list = [["   ", "   ",  "TPC", "TPC", "CWV", "CWV"], ["Name", "Index","HCP", "Strokes", "HCP", "Strokes"]]#, ["-------","-----",  "---",  "-------",  "---",  "-------"]]
	results_list = []
	for player in player_dict:
		tpc_handicap = compute_handicap_tpc(float(player_dict[player]), tpc_slope_white_72, tpc_rating_white_72, tpc_hcp_72)
		cwv_handicap = compute_handicap_cwv(float(player_dict[player]), cwv_slope_white_71, cwv_rating_white_71, cwv_hcp_71)
		# print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
		results = [name_dict[player], player_dict[player], tpc_handicap, tpc_handicap-tpc_min, cwv_handicap, cwv_handicap-cwv_min]
		results_list.append(results)

	results_list.sort()
	results_list.insert(0,["   ", "   ",  "TPC", "TPC", "CWV", "CWV"])
	results_list.insert(1,["Name", "Index","(72)", "Strks", "(71)", "Strks"])
	today = datetime.now()
	today = today.strftime("%B %d, %Y %H:%M")

	# print('-------------------------------------------------------')
	print("\n \n Today's date:", today)

	print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
	print (f"TPC: {tpc_rating_white_72} / {tpc_slope_white_72} / Par {tpc_hcp_72} \nCWV: {cwv_rating_white_71} / {cwv_slope_white_71} / Par {cwv_hcp_71}")
	print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
	print ('  (Course Rating - Par)')
	print('--------------------------------------------------------')

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
# main()
# main2()
# AllHandicaps('0')