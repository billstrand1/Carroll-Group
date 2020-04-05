#computes handicaps for both courses / all tees
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
	