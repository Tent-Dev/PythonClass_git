def stat_point_goald(set_val):
    for i, val in enumerate(set_val):
        point = (set_val[i]["W"] * 3) + (set_val[i]["D"] * 1)
        gd = set_val[i]["GF"] - set_val[i]["GA"]
        print("{}\t {:30} Pts: {:3}\t GD: {:3}".format(set_val[i]["Pos"], set_val[i]["Team"], point, gd))


def stat_percentages(set_val):
    set_val = sorted(set_val, key=lambda k: k['Team'])
    for i, val in enumerate(set_val):
        sum_score = (set_val[i]["W"] + set_val[i]["D"] + set_val[i]["L"])
        win = (set_val[i]["W"] / sum_score) * 100
        draw = (set_val[i]["D"] / sum_score) * 100
        lost = (set_val[i]["L"] / sum_score) * 100
        print("{}\t {:30} Win[{:3,.2f}%]\t Draw[{:3,.2f}%] Lost[{:3,.2f}%]".format(set_val[i]["Pos"], set_val[i]["Team"],win, draw, lost))


def stat_percentages_adv(set_val):
    set_val = sorted(set_val, key=lambda k: k['Team'])
    for i, val in enumerate(set_val):
        sum_score = (set_val[i]["W"] + set_val[i]["D"] + set_val[i]["L"])
        win = (set_val[i]["W"] / sum_score) * 100
        draw = (set_val[i]["D"] / sum_score) * 100
        lost = (set_val[i]["L"] / sum_score) * 100

        if win > lost:
            print("{}\t {:30} Win[{:3,.2f}%]".format(set_val[i]["Pos"], set_val[i]["Team"], win))
        else:
            print("{}\t {:30} \t\t\t  Lost[{:3,.2f}%]".format(set_val[i]["Pos"], set_val[i]["Team"], lost))


premier_league_2017_2018 = premier_league_2017_2018 = [
    {
        "Pos": 1, "Team": "Manchester City (C)", "W": 32, "D": 4, "L": 2, "GF": 106, "GA": 27
    },
    {
        "Pos": 2, "Team": "Manchester United", "W": 25, "D": 6, "L": 7, "GF": 68, "GA": 28
    },
    {
        "Pos": 3, "Team": "Tottenham Hotspur", "W": 23, "D": 8, "L": 7, "GF": 74, "GA": 36
    },
    {
        "Pos": 4, "Team": "Liverpool", "W": 21, "D": 12, "L": 5, "GF": 84, "GA": 38
    },
    {
        "Pos": 5, "Team": "Chelsea", "W": 21, "D": 7, "L": 10, "GF": 62, "GA": 38
    },
    {
        "Pos": 6, "Team": "Arsenal", "W": 19, "D": 6, "L": 13, "GF": 74, "GA": 51
    },
    {
        "Pos": 7, "Team": "Burnley", "W": 14, "D": 12, "L": 12, "GF": 36, "GA": 39
    },
    {
        "Pos": 8, "Team": "Everton", "W": 13, "D": 10, "L": 15, "GF": 44, "GA": 58
    },
    {
        "Pos": 9, "Team": "Leicester City", "W": 12, "D": 11, "L": 15, "GF": 56, "GA": 60
    },
    {
        "Pos": 10, "Team": "Newcastle United", "W": 12, "D": 8, "L": 18, "GF": 39, "GA": 47
    },
    {
        "Pos": 11, "Team": "Crystal Palace", "W": 11, "D": 11, "L": 16, "GF": 45, "GA": 55
    },
    {
        "Pos": 12, "Team": "Bournemouth", "W": 11, "D": 11, "L": 16, "GF": 45, "GA": 61
    },
    {
        "Pos": 13, "Team": "West Ham United", "W": 10, "D": 12, "L": 16, "GF": 48, "GA": 68
    },
    {
        "Pos": 14, "Team": "Watford", "W": 11, "D": 8, "L": 19, "GF": 44, "GA": 64
    },
    {
        "Pos": 15, "Team": "Brighton & Hove Albion", "W": 9, "D": 13, "L": 16, "GF": 34, "GA": 54
    },
    {
        "Pos": 16, "Team": "Huddersfield Town", "W": 9, "D": 10, "L": 19, "GF": 28, "GA": 58
    },
    {
        "Pos": 17, "Team": "Southampton", "W": 7, "D": 15, "L": 16, "GF": 37, "GA": 56
    },
    {
        "Pos": 18, "Team": "Swansea City (R)", "W": 8, "D": 9, "L": 21, "GF": 28, "GA": 56
    },
    {
        "Pos": 19, "Team": "Stoke City (R)", "W": 7, "D": 12, "L": 19, "GF": 35, "GA": 68
    },
    {
        "Pos": 20, "Team": "West Bromwich Albion (R)", "W": 6, "D": 13, "L": 19, "GF": 31, "GA": 56
    }
]

stat_point_goald(premier_league_2017_2018)
print("-" * 100)
stat_percentages(premier_league_2017_2018)
print("-" * 100)
stat_percentages_adv(premier_league_2017_2018)
