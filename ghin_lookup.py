#ghin_lookup.py
#uploaded to Git, test comment update.

# import calculate_handicaps
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
import re
import pprint
# import time	#not used
# from collections import namedtuple #not used
from datetime import date
from datetime import datetime


def get_index(ghin_no):
	url = 'https://widgets.ghin.com/HandicapLookupResults.aspx?entry=1&dynamic=&small=1&css=CGA03&ghinno=' + ghin_no + '&hidename=0&showmsg=0&showheader=1&showtabheader=0&combinehieff=0&showheadertext=1&showfootertext=1&tab=0'
	page = requests.get(url)
	# print(page) #looking for 200

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page.text, 'html.parser')
	# extract line with index 
	index_text = soup.find_all(class_='ClubGridHandicapIndex')
	# find handicap index from string
	index = re.findall('[0-9]+.[0-9]', str(index_text))
	index_int = index[0] #print(index[0])
	# print(index_int)

	# extract line with name
	name_text = soup.find(id='ctl00_bodyMP_lblName')
	# print(name_text)

	name = re.findall('>(.*?)<', str(name_text))
	name_str = name[0]  #print(name[0])
	# print(name_str)

	# works:
	index_list.append(index_int)
	# print (index_list)
	player_dict[name_str] = index_int

def get_index_from_ghin():
	print('get_index_from_ghin entered')

	# for item in ghin: #index_list:
	for ghin_no in ghin:
		get_index(ghin_no)
		# print(ghin_no)
		time.sleep(3)

	# print('Index List:')
	# print(index_list)
	# print('Player Dict:')
	# print(player_dict)

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


def compute_handicap_tpc_white(h_i):
	return (round ((h_i * tpc_slope_white / 113) + (tpc_rating_white - 70))) # Need to add in Par - Rating


def compute_handicap_cwv_white(h_i):
	return (round ((h_i * cwv_slope_white / 113) + (cwv_rating_white - 71))) # Need to add in Par - Rating

#--------------------START LIST, DICT DEFINITINS-----------------------------
index_list = []
player_dict = {} # list of players : h_i from either prefilled or ghin
tpc_slope_white = 128
cwv_slope_white = 130
tpc_rating_white = 69.4
cwv_rating_white = 69.3

tpc_slope_gold = 132
cwv_slope_gold = 132
tpc_rating_gold = 70.2
cwv_rating_gold = 70.3


name_dict = {'Jack Carroll': 'Jack', 'Bob Heard': 'Bob H.', 'Larry Traub': 'Larry', 'Jim Sido': 'Jim S.', 
'Curt Fitzgerald': 'Curt', 'Jimmy Wickham': 'Jimmy', 'Richard Humphrey': 'Hump', 'Kent Fannon': 'Kent', 
'Bill Barnard': 'Bill B.', 'Doug Williams': 'Doug', 'Rocky Duron': 'Rocky', 'Will Davis': 'Will', 
'Reid Baker': 'Reid', 'Bill Strand': 'Bill S.', 'Rick Baumgarth': 'Trick', 'Rick Besse': 'Besse', 'Dan Stewart': 'Dan', 
'Al Vela': 'Al', 'Frank Broyles': 'Frank'} #missing Bob V.

# ghin = ['3660603','4548474','4787165','2379581','3661053','3660992','3660486','5910694','3661061','3720105',
# '1815996','3660253','3660366', '3660265', '3660283', '7701708', '3661029', '0053161']
# ghin = ['add Franks', 'add Bobs'] # for Testing New people and obtain their 'formal names' from GHIN to add to name_dict.  Missing Frank, Bob V.


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
# get_index_from_ghin() #for production, player_dict is populated with a new ghin download
player_dict = get_index_from_prefilled_dict() #for testing only, player_dict is predefined from a previous ghin download

# print(player_dict)

tpc_list = []  #accumulate list of handicaps for sorting purposes
cwv_list = []  #accumulate list of handicaps for sorting purposes

# print ('computing handicaps')
for player in player_dict:
	h_i = float(player_dict[player])
	name = player
	# print (h_i)
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

results_list = [["   ", "   ",  "TPC", "TPC", "CWV", "CWV"], ["Name", "Index","HCP", "Strokes", "HCP", "Strokes"]]#, ["-------","-----",  "---",  "-------",  "---",  "-------"]]
for player in player_dict:
	tpc_handicap = compute_handicap_tpc_white(float(player_dict[player]))
	cwv_handicap = compute_handicap_cwv_white(float(player_dict[player]))
	# print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
	results = [name_dict[player], player_dict[player], tpc_handicap, tpc_handicap-tpc_min, cwv_handicap, cwv_handicap-cwv_min]
	results_list.append(results)

today = datetime.now()
today = today.strftime("%B %d, %Y %H:%M")

# print('-------------------------------------------------------')
print("Today's date:", today)

print (tabulate(results_list, tablefmt='fancy_grid', colalign=("right","right","right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
print (f"TPC: {tpc_rating_white} / {tpc_slope_white}  CWV: {cwv_rating_white} / {cwv_slope_white} ")
print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
print ('  (Course Rating - Par)')
print('--------------------------------------------------------')
