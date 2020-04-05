printout.py
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

		#works:
		column_print_alignment = list(("right","right","right","right"))
		print(column_print_alignment)

		print (tabulate(results_list, tablefmt='fancy_grid', colalign=column_print_alignment))#("right","right","right","right"))) #, headers=["Name","Index", "TPC HCP", "TPC Strokes", "CWV HCP", "CWV Strokes"]))
		print (f"CWV: CR = {cwv_rating_white_71} | SR = {cwv_slope_white_71} | Par = {cwv_hcp_71}")
		# print ('Course Handicap = Handicap Index x (Slope Rating/113) +')
		# print ('  (Course Rating - Par)')
		print ('Course Handicap = (H.I. x SR / 113) + (CR - Par)')
		print('--------------------------------------------------------')
