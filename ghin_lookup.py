#ghin_lookup.py
#uploaded to Git, test comment update.

# import calculate_handicaps
import requests
from bs4 import BeautifulSoup
import re
import pprint
import time
from collections import namedtuple

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
	return ({'Bob Heard': '6.2', 'Larry Traub': '8.4', 'Jim Sido': '8.2', 
	'Curt Fitzgerald': '17.5', 'Jimmy Wickham': '13.9', 'Dr. Richard Humphrey': '16.9', 'Kent Fannon': '12.5', 
	'Bill Barnard': '15.6', 'Mr. Doug Williams': '19.1', 'Rocky Duron': '16.1', 'Will Davis': '12.7', 
	'Reid Baker': '11.2', 'Mr. Jack Carroll': '10.1', 'Al Vela': '14.5', 'Dan Stewart': '13.0', 'Bill Strand': '11.3',})



#--------------------START LIST, DICT DEFINITINS-----------------------------
index_list = []
player_dict = {} # list of players : h_i from either prefilled or ghin
tpc_slope_white = 128
cwv_slope_white= 130 

name_dict = {'Mr. Jack Carroll': 'Jack', 'Bob Heard': 'Bob', 'Larry Traub': 'Larry', 'Jim Sido': 'Jim S.', 
'Curt Fitzgerald': 'Curt', 'Jimmy Wickham': 'Jimmy', 'Dr. Richard Humphrey': 'Hump', 'Kent Fannon': 'Kent', 
'Bill Barnard': 'Bill B.', 'Mr. Doug Williams': 'Doug', 'Rocky Duron': 'Rocky', 'Will Davis': 'Will', 
'Reid Baker': 'Reid', 'Bill Strand': 'Bill S.', 'Rick Baumgarth': 'Trick', 'Rick Besse': 'Besse', 'Dan Stewart': 'Dan', 
'Al Vela': 'Al'} #missing Frank, Bob V.

ghin = ['3660603','4548474','4787165','2379581','3661053','3660992','3660486','5910694','3661061','3720105',
'1815996','3660253','3660366', '3660265', '3660283', '7701708', '3661029', '0053161']
# ghin = ['add Franks', 'add Bobs'] # for Testing New people and obtain their 'formal names' from GHIN to add to name_dict.  Missing Frank, Bob V.

#--------------------START CODE EXECUTION-----------------------------

print('Program starts')
get_index_from_ghin() #for production, player_dict is populated with a new ghin download
# player_dict = get_index_from_prefilled_dict() #for testing only, player_dict is predefined from a previous ghin download

tpc_list = []  #accumulate list of handicaps for sorting purposes
cwv_list = []  #accumulate list of handicaps for sorting purposes

print ('computing handicaps')
for player in player_dict:
	h_i = float(player_dict[player])
	name = player
	# print (h_i)
	handicap_tpc = round (h_i * tpc_slope_white / 113)
	tpc_list.append(handicap_tpc)
	handicap_cwv = round (h_i * cwv_slope_white / 113)
	cwv_list.append(handicap_cwv)
	# print(f"Name: {name} Index: {h_i}, TPC: {handicap_tpc}, CWV: {handicap_cwv}")


tpc_list.sort()
# print(tpc_list)
tpc_min = tpc_list[0]
cwv_list.sort()
cwv_min = cwv_list[0]

for player in player_dict:
	tpc_handicap = compute_handicap_tpc_white(float(player_dict[player]))
	cwv_handicap = compute_handicap_cwv_white(float(player_dict[player]))
	print(f" {name_dict[player]} : {player_dict[player]}, TPC: {tpc_handicap} ({tpc_handicap-tpc_min}), CWV: {cwv_handicap} ({cwv_handicap-cwv_min})")
	

# Bob : 6.2, TPC: 7 (0), CWV: 7 (0)
#  Larry : 8.4, TPC: 10 (3), CWV: 10 (3)
#  Jim S. : 8.2, TPC: 9 (2), CWV: 9 (2)
#  Curt : 17.5, TPC: 20 (13), CWV: 20 (13)
#  Jimmy : 13.9, TPC: 16 (9), CWV: 16 (9)
#  Hump : 16.9, TPC: 19 (12), CWV: 19 (12)
#  Kent : 12.5, TPC: 14 (7), CWV: 14 (7)
#  Bill B. : 15.6, TPC: 18 (11), CWV: 18 (11)
#  Doug : 19.1, TPC: 22 (15), CWV: 22 (15)
#  Rocky : 16.1, TPC: 18 (11), CWV: 19 (12)
#  Will : 12.7, TPC: 14 (7), CWV: 15 (8)
#  Reid : 11.2, TPC: 13 (6), CWV: 13 (6)
#  Jack : 10.1, TPC: 11 (4), CWV: 12 (5)
#  Al : 14.5, TPC: 16 (9), CWV: 17 (10)
#  Dan : 13.0, TPC: 15 (8), CWV: 15 (8)
#  Bill S. : 11.3, TPC: 13 (6), CWV: 13 (6)
# https://widgets.ghin.com/HandicapLookupResults.aspx?entry=1&dynamic=&small=1&css=CGA03&ghinno=0053161&hidename=0&showmsg=0&showheader=1&showtabheader=0&combinehieff=0&showheadertext=1&showfootertext=1&tab=0'
