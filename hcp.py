# uses ghinxl.py and players.py
from players import *
from ghinxl import *
import operator


def get_pairings_info(choice):
    results = ()
    results_list = []

    if choice == "T" or choice == "t":
        for player in player_list:
            if player.playing:
                results = [
                    player.signup_name,
                    player.handicap_tpc_70,
                ]
                results_list.append(results)

    elif choice == "C" or choice == "c":
        for player in player_list:
            if player.playing:
                results = [
                    player.signup_name,
                    player.handicap_cwv_71,
                ]
                results_list.append(results)

    else:
        print("Bad Choice for Pairings info")

    results_dict = dict(results_list)
    # sorted(results_dict.items(), key=operator.itemgetter(1))
    # print(results_dict)

    sorted_list = sorted(results_dict.items(), key=lambda x: x[1])
    # print(sorted_list)

    print("----For Jack----")
    # for item in sorted_list:
    #     print(f"{item[0]}: {item[1]}")
    headers = [
        "Name",
        "HCP"]
    column_print_alignment = list(("right", "right"))
    print(
        tabulate(
            sorted_list,
            tablefmt="simple",
            colalign=column_print_alignment,
            headers=headers,
            floatfmt=".1f",
        )
    )


# -------------------- main code:
course_choice = ghinxl_main()

get_pairings_info(course_choice)


# -------------------- main code ends
