premier_league_2017_2018 = [
                                ["Manchester City",(32,4,2)],
                                ["Manchester United",(25,6,7)],
                                ["Tottenham",(23,8,7)],
                                ["Liverpool",(21,12,5)],
                                ["Chelsea",(21,7,10)],
                                ["Arsenal",(19,6,13)],
                                ["Burnley",(14,12,12)],
                                ["Everton",(13,10,15)],
                                ["Leicester",(12,11,15)],
                                ["Newcastle",(12,8,18)],
                                ["Crystal Palace",(11,11,16)],
                                ["Bournemouth",(11,11,16)],
                                ["West Ham",(10,12,16)],
                                ["Watford",(11,8,19)],
                                ["Brighton",(9,13,16)],
                                ["Huddersfield",(9,10,19)],
                                ["Southampton",(7,15,16)],
                                ["Swansea",(8,9,21)],
                                ["Stoke",(7,12,19)],
                                ["West Bromwich",(6,13,19)]
                            ]

def show_final_result(premier_league_2017_2018):
    for i,j in enumerate(premier_league_2017_2018):

        score = (j[1][0]*3)+(j[1][1])
        print("{}\t {:15}\t {:15}".format(i+1,j[0],score))

        if i == 3:
            print("-"*100)

        elif i == len(premier_league_2017_2018)-4:
            print("-" * 100)

def lost_morethan_draw(premier_league_2017_2018):
    for i,j in enumerate(premier_league_2017_2018):
        score = (j[1][2]) - (j[1][1])
        if j[1][2] > j[1][1]:
            print("{:20}\t {:15}".format(j[0], score))


show_final_result(premier_league_2017_2018)
print("-"*100)
lost_morethan_draw(premier_league_2017_2018)