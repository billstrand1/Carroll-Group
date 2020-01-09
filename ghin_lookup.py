#ghin_lookup.py
#uploaded to Git, test comment update.
# CALCS ARE FOR TPC WHITE PAR 72...

from tabulate import tabulate
import re
from datetime import datetime

#------------------------file start-------------------------------
def get_index_from_text_file():
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

def compute_handicap_tpc_white(h_i): #for PAR 72 ONLY
	return (round ((h_i * tpc_slope_white_72 / 113) + (tpc_rating_white_72 - tpc_hcp_72))) # Need to add in Par - Rating

def compute_handicap_cwv_white(h_i):
	return (round ((h_i * cwv_slope_white / 113) + (cwv_rating_white - 71))) # Need to add in Par - Rating

#--------------------START LIST, DICT DEFINITINS-----------------------------
tpc_slope_white_70 = 128
tpc_rating_white_70 = 69.4
tpc_hcp_70 = 70

cwv_slope_white = 130
cwv_rating_white = 69.3

tpc_slope_white_72 = 127
tpc_rating_white_72 = 70
tpc_hcp_72 = 72

tpc_slope_gold = 132
cwv_slope_gold = 132
tpc_rating_gold = 70.2
cwv_rating_gold = 70.3


name_dict = {'Jack Carroll': 'Jack', 'Bob Heard': 'Bob H.', 'Larry Traub': 'Larry', 'Jim Sido': 'Jim S.', 
'Curt Fitzgerald': 'Curt', 'Jimmy Wickham': 'Jimmy', 'Richard Humphrey': 'Hump', 'Kent Fannon': 'Kent', 
'Bill Barnard': 'Bill B.', 'Doug Williams': 'Doug', 'Rocky Duron': 'Rocky', 'Will Davis': 'Will', 
'Reid Baker': 'Reid', 'Bill Strand': 'Bill S.', 'Rick Baumgarth': 'Trick', 'Rick Besse': 'Besse', 'Dan Stewart': 'Dan', 
'Al Vela': 'Al', 'Frank Broyles': 'Frank'} #missing Bob V.

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

# print('Program starts')
file_name = input ("What is the input filename? > ")
# print('calling get_index_from_text_file')
player_dict = get_index_from_text_file() #take copy/pasted html and save to file named: 2020-01-05.txt


tpc_list = []  #accumulate list of handicaps for sorting purposes
cwv_list = []  #accumulate list of handicaps for sorting purposes

# print ('computing handicaps')
for player in player_dict:
	h_i = float(player_dict[player])
	name = player

	handicap_tpc = compute_handicap_tpc_white(h_i)
	tpc_list.append(handicap_tpc)
	handicap_cwv = compute_handicap_cwv_white(h_i)
	cwv_list.append(handicap_cwv)
	# print(f"Name: {name} Index: {h_i}, TPC: {handicap_tpc}, CWV: {handicap_cwv}")


#determine lowest handicap
tpc_list.sort()
tpc_min = tpc_list[0]
cwv_list.sort()
cwv_min = cwv_list[0]

#for printing purposes only, redundant from above

# results_list = [["   ", "   ",  "TPC", "TPC", "CWV", "CWV"], ["Name", "Index","HCP", "Strokes", "HCP", "Strokes"]]#, ["-------","-----",  "---",  "-------",  "---",  "-------"]]
results_list = []
for player in player_dict:
	tpc_handicap = compute_handicap_tpc_white(float(player_dict[player]))
	cwv_handicap = compute_handicap_cwv_white(float(player_dict[player]))
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
print (f"TPC: {tpc_rating_white_72} / {tpc_slope_white_72} / Par {tpc_hcp_72} \nCWV: {cwv_rating_white} / {cwv_slope_white} / Par 71")
print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
print ('  (Course Rating - Par)')
print('--------------------------------------------------------')