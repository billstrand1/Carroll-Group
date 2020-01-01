# Consolidate the handicap calculating functions here

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

	