#ghin_lookup.py
#uploaded to Git, test comment update.

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

def compute_handicap_tpc_white(h_i): #for slope rating of 128 TPC whites
	if h_i >= 0.5 and h_i <= 1.3 : return 1
	elif h_i >= 1.4 and h_i <= 2.2 : return 2
	elif h_i >= 2.3 and h_i <= 3.0: return 3
	elif h_i >= 3.1 and h_i <= 3.9: return 4
	elif h_i >= 4.0 and h_i <= 4.8 : return 5
	elif h_i >= 4.9 and h_i <= 5.7 : return 6
	elif h_i >= 5.8 and h_i <= 6.6 : return 7
	elif h_i >= 6.7 and h_i <= 7.5 : return 8
	elif h_i >= 7.6 and h_i <= 8.3 : return 9
	elif h_i >= 8.4 and h_i <= 9.2 : return 10
	elif h_i >= 9.3 and h_i <= 10.1 : return 11
	elif h_i >= 10.2 and h_i <= 11.0 : return 12
	elif h_i >= 11.1 and h_i <= 11.9 : return 13
	elif h_i >= 12.0 and h_i <= 12.8 : return 14
	elif h_i >= 12.9 and h_i <= 13.6 : return 15
	elif h_i >= 13.7 and h_i <= 14.5 : return 16
	elif h_i >= 14.6 and h_i <= 15.4 : return 17
	elif h_i >= 15.5 and h_i <= 16.3 : return 18
	elif h_i >= 16.4 and h_i <= 17.2 : return 19
	elif h_i >= 17.3 and h_i <= 18.0 : return 20
	elif h_i >= 18.1 and h_i <= 18.9 : return 21
	elif h_i >= 19.0 and h_i <= 19.8 : return 22
	elif h_i >= 19.9 and h_i <= 20.7 : return 23
	elif h_i >= 20.8 and h_i <= 21.6 : return 24
	elif h_i >= 21.7 and h_i <= 22.5 : return 25
	elif h_i >= 22.6 and h_i <= 23.3 : return 26
	elif h_i >= 23.4 and h_i <= 24.2 : return 27
	elif h_i >= 24.3 and h_i <= 25.1 : return 28
	elif h_i >= 25.2 and h_i <= 26.0 : return 29
	elif h_i >= 26.1 and h_i <= 26.9 : return 30
	else: return 0

def compute_handicap_cwv_white(h_i): #for slope rating of 130 CWV whites
	if h_i >= 0.5 and h_i <= 1.3 : return 1
	elif h_i >= 1.4 and h_i <= 2.1 : return 2
	elif h_i >= 2.2 and h_i <= 3.0: return 3
	elif h_i >= 3.1 and h_i <= 3.9: return 4
	elif h_i >= 4.0 and h_i <= 4.7 : return 5
	elif h_i >= 4.8 and h_i <= 5.6 : return 6
	elif h_i >= 5.7 and h_i <= 6.5 : return 7
	elif h_i >= 6.6 and h_i <= 7.3 : return 8
	elif h_i >= 7.4 and h_i <= 8.2 : return 9
	elif h_i >= 8.3 and h_i <= 9.1 : return 10
	elif h_i >= 9.2 and h_i <= 9.9 : return 11
	elif h_i >= 10.0 and h_i <= 10.8 : return 12
	elif h_i >= 10.9 and h_i <= 11.7 : return 13
	elif h_i >= 11.8 and h_i <= 12.6 : return 14
	elif h_i >= 12.7 and h_i <= 13.4 : return 15
	elif h_i >= 13.5 and h_i <= 14.3 : return 16
	elif h_i >= 14.4 and h_i <= 15.2 : return 17
	elif h_i >= 15.3 and h_i <= 16.0 : return 18
	elif h_i >= 16.1 and h_i <= 16.9 : return 19
	elif h_i >= 17.0 and h_i <= 17.8 : return 20
	elif h_i >= 17.9 and h_i <= 18.6 : return 21
	elif h_i >= 18.7 and h_i <= 19.5 : return 22
	elif h_i >= 19.6 and h_i <= 20.4 : return 23
	elif h_i >= 20.5 and h_i <= 21.2 : return 24
	elif h_i >= 21.3 and h_i <= 22.1 : return 25
	elif h_i >= 22.2 and h_i <= 23.0 : return 26
	elif h_i >= 23.1 and h_i <= 23.9 : return 27
	elif h_i >= 24.0 and h_i <= 24.7 : return 28
	elif h_i >= 24.8 and h_i <= 25.6 : return 29
	elif h_i >= 25.7 and h_i <= 26.5 : return 30
	else: return 0

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



#--------------------START CODE EXECUTION-----------------------------
index_list = []
player_dict = {}

name_dict = {'Mr. Jack Carroll': 'Jack', 'Bob Heard': 'Bob', 'Larry Traub': 'Larry', 'Jim Sido': 'Jim S.', 
'Curt Fitzgerald': 'Curt', 'Jimmy Wickham': 'Jimmy', 'Dr. Richard Humphrey': 'Hump', 'Kent Fannon': 'Kent', 
'Bill Barnard': 'Bill B.', 'Mr. Doug Williams': 'Doug', 'Rocky Duron': 'Rocky', 'Will Davis': 'Will', 
'Reid Baker': 'Reid', 'Bill Strand': 'Bill S.', 'Rick Baumgarth': 'Trick', 'Rick Besse': 'Besse', 'Dan Stewart': 'Dan', 
'Al Vela': 'Al'} #missing Frank, Bob V.

ghin = ['3660603','4548474','4787165','2379581','3661053','3660992','3660486','5910694','3661061','3720105',
'1815996','3660253','3660366', '3660265', '3660283', '7701708', '3661029', '0053161']
# ghin = ['add Franks', 'add Bobs'] # for Testing New people and obtain their 'formal names' from GHIN to add to name_dict.  Missing Frank, Bob V.


print('Program starts')
# get_index_from_ghin() #for production, player_dict is populated with a new ghin download
player_dict = get_index_from_prefilled_dict() #for testing only, player_dict is predefined from a previous ghin download

tpc_list = []  #accumulate list of handicaps for sorting purposes
cwv_list = []  #accumulate list of handicaps for sorting purposes

print ('computing handicaps')
for player in player_dict:
	h_i = float(player_dict[player])
	name = player
	# print (h_i)
	handicap_tpc = compute_handicap_tpc_white(h_i)
	tpc_list.append(handicap_tpc)
	handicap_cwv = compute_handicap_cwv_white(h_i)
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
	
	