# for use with ghinxl.py
# contains the name dictionary and Player class
# contains the course handicap information

# print ('PLAYERS.PY HAS BEEN IMPORTED')
#--------------------CONSTANTS-----------------------------
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

cwv_slope_white_71 = 128
cwv_rating_white_71 = 69.3

cwv_slope_gold_71 = 130
cwv_rating_gold_71 = 70.4

cwv_slope_blue_71 = 132
cwv_rating_blue_71 = 71.4
#--------------------END CONSTANTS-----------------------------

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
	'Bill  Strand': 'Bill S.', 
	'Rick Baumgarth': 'Trick', 
	'Rick Besse': 'Besse', 
	'Dan Stewart': 'Dan', 
	'Al Vela': 'Al', 
	'Frank Broyles': 'Frank'}

class Player:
	def __init__ (self, playing, signup_name, ghin_no, email, birthday, cell_phone, ghin_name):
		self.playing = playing
		self.signup_name = signup_name
		self.ghin_no = ghin_no
		self.email = email
		self.birthday = birthday
		self.cell_phone = cell_phone
		self.ghin_name = ghin_name
		self.h_i = 0
		self.handicap_tpc_70 = 0
		self.handicap_tpc_72 = 0
		self.handicap_cwv_71 = 0

	def class_tpc_white_70(self): 
		self.handicap_tpc_70 = (round ((self.h_i * tpc_slope_white_70 / 113) + (tpc_rating_white_70 - tpc_hcp_70))) 

	def class_tpc_white_72(self): 
		self.handicap_tpc_72 = (round ((self.h_i * tpc_slope_white_72 / 113) + (tpc_rating_white_72 - tpc_hcp_72))) 

	def class_cwv_white_71(self):
		self.handicap_cwv_71 = (round ((self.h_i * cwv_slope_white_71 / 113) + (cwv_rating_white_71 - cwv_hcp_71)))  


Al 		= Player(False, 'Al', '3661029', 'txanv3@verizon.net', '12/24/1940', '(214) 405-6475', 'Al Vela')
Besse 	= Player(True, 'Besse', '3660283', 'rick@rickbesse.com', '10/07/1943', '(214) 850-7100', 'Rick Besse')
BillB	= Player(False, 'Bill B.','5910694', 'wbarnard96@aol.com',	'07/15/1953','(817) 800-0659', 'Bill Barnard')
BillS	= Player(True, 'Bill S.','0053161', 'billstrand1@yahoo.com', '10/23/1961', '(469) 774-7607', 'Bill  Strand')
Bob		= Player(True, 'Bob','3660603', 'bheard3321@gmail.com', '06/10/1951', '(214) 995-3050', 'Bob Heard')
Curt	= Player(False, 'Curt','2379581', 'Cmfitzg@gmail.com', '11/19/1948', '(972) 754-6910', 'Curt Fitzgerald')
Dan		= Player(True, 'Dan','7701708', 'danstewart01@icloud.com', '09/23/1947', '(214) 215-4046', 'Dan Stewart')
Doug	= Player(True, 'Doug','3661061', 'dougwilliams9@hotmail.com', '09/06/1946', '(214) 502-3384', 'Doug Williams')
Frank	= Player(True, 'Frank','2379621', 'frank.broyles@utexas.edu', '05/12/1946', '(214) 207-4336', 'Frank Broyles')
Hump	= Player(False, 'Hump','3660992', 'rcraighumphrey@msn.com', '08/27/1950', '(214) 686-2666', 'Richard Humphrey')
Jack	= Player(True, 'Jack','3660366', 'JackLCarroll@Verizon.net', '09/09/1945', '(972) 679-6595', 'Jack Carroll')
JimS	= Player(False, 'Jim S.','4787165', 'jimsido@gmail.com', '10/15/1946', '(214) 215-0122', 'Jim Sido')
Jimmy	= Player(True, 'Jimmy W.', '3661053', 'jimwickham@verizon.net', '11/19/1940', '(214) 908-2370', 'Jimmy Wickham')
Kent	= Player(False, 'Kent','3660486', 'kent.fannon@verizon.net', '07/03/1952', '(214) 850-6980', 'Kent Fannon')
Larry	= Player(False, 'Larry', '4548474', 'larrytraub5@gmail.com', '07/04/1949',	'(214) 850-8128', 'Larry Traub')
Reid	= Player(False, 'Reid', '3660253', 'reid.baker@sbcglobal.net', '12/14/1948', '(214) 683-1799', 'Reid Baker')
Rocky	= Player(False, 'Rocky', '3720105', 'duronrocky@gmail.com', '06/10/1932', '(214) 707-0556', 'Rocky Duron')
Trick	= Player(True, 'Trick', '3660265', 'rbaumgarth@aol.com', '08/17/1947', '(214) 476-7801', 'Rick Baumgarth')
Will	= Player(True, 'Will', '1815996', 'vanhorn_davis@verizon.net', '09/11/1952', '(561) 351-7724', 'Will Davis')
 
player_list = [Al, Besse, BillB, BillS, Bob, Curt,Dan, Doug, Frank, Hump, Jack, JimS, Jimmy, Kent, Larry, Reid, Rocky, Trick, Will]	


# i = 1
# for player in player_list:
# 	print (player.ghin_name, ', ', player.ghin_no)
	# i += 1	