import pymongo

client = pymongo.MongoClient("mongodb+srv://chutipas:TaTent591220306@cluster0-94rnq.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("Practice")

def practice1():
    print("Show Information of Stadium Order by Country name.")
    readcmd = list(db.Club.find({}).sort('City'))
    j = 1
    for i in readcmd:
        print("{} - {}".format(j, i['Stadium_Name']))
        j+=1
    print("-"*50)

def practice2():
    print("Show Information of Stadium in Liverpool City.")
    readcmd = list(db.Club.find({'City':{'$in':['Liverpool']}}))
    j = 1
    for i in readcmd:
        print("{} - {}".format(j, i['Stadium_Name']))
        j+=1
    print("-"*50)

def practice3():
    print("Show Information of Stadium where name end with 'Stadium'.")
    readcmd = list(db.Club.find({'Stadium_Name':{'$regex':'Stadium$', '$options':'i'}}))
    j = 1
    for i in readcmd:
        print("{} - {}".format(j, i['Stadium_Name']))
        j+=1
    print("-"*50)

def practice4():
    print("Show Information of Stadium where Club name has 'FC'.")
    readcmd = list(db.Club.find({'Stadium_Name':{'$regex':'FC'}}))
    j = 1
    for i in readcmd:
        print("{} - {}".format(j, i['Stadium_Name']))
        j+=1
    print("-"*50)

def practice5():
    print("Show Information of Stadium where capacity more than 20,000 people.")
    readcmd = list(db.Club.find({'Capacity':{'$gt':20000}}))
    j = 1
    for i in readcmd:
        print("{} - {:70} {:,} people".format(j, i['Stadium_Name'], i['Capacity']))
        j+=1
    print("-"*50)

def practice6():
    print("Show Information of Stadium where capacity between 20,000 to 40,000 people. and Order by Capacity")
    readcmd = list(db.Club.find({'$and':[{'Capacity':{'$gt':20000}},{'Capacity':{'$lt':40000}}]}).sort('Capacity'))
    j = 1
    for i in readcmd:
        print("{} - {:70} {:,} people".format(j, i['Stadium_Name'], i['Capacity']))
        j+=1
    print("-"*50)

def practice7():
    print("Show Information of Stadium in London where capacity less than 20,000")
    readcmd = list(db.Club.find({'$and':[{'Capacity':{'$gt':20000}},{'Capacity':{'$lt':40000}}]}).sort('Capacity',-1))
    j = 1
    for i in readcmd:
        print("{} - {:70} {:,} people".format(j, i['Stadium_Name'], i['Capacity']))
        j+=1
    print("-"*50)

def practice8():
    print("Show Information of Stadium Orderby Capacity and Name.")
    readcmd = list(db.Club.find({}).sort([('Capacity',-1),('Stadium_Name',1)]))
    j = 1
    for i in readcmd:
        print("{} - {:70} {:,} people".format(j, i['Stadium_Name'], i['Capacity']))
        j+=1
    print("-"*50)

def practice9():
    print("Show Information of Stadium in Bristol , London , Luton and capacity more than 15,000 .")
    readcmd = list(db.Club.find({'$and':[{'City':{'$in':['Bristol','London','Luton']}},{'Capacity':{'$gt':15000}}]}))
    j = 1
    for i in readcmd:
        print("{} - {:70} {:70} {:,} people".format(j, i['Stadium_Name'],i['City'], i['Capacity']))
        j+=1
    print("-"*50)

def practice10():
    print("Show Information of Stadium where capacity less than 10,000 or have 'FC' in stadium name Order by City .")
    readcmd = list(db.Club.find({'$or':[{'Capacity':{'$lt':10000}},{'Staduim_Name':{'$regex':'FC'}}]}).sort('City',1))
    j = 1
    for i in readcmd:
        print("{} - {:70} {:70} {:,} people".format(j, i['Stadium_Name'],i['City'], i['Capacity']))
        j+=1
    print("-"*50)

def practice11():
    print("Update Capacity where Club name is 'Liverpool FC' to 100,000")
    updatecmd = db.Club.update_many({'Club':'Liverpool FC'},{'$set':{'Capacity':100000}})
    readcmd = list(db.Club.find({'Club':'Liverpool FC'}))

    j = 1
    for i in readcmd:
        print("{} - {:70} {:70} {:,} people".format(j, i['Stadium_Name'],i['City'], i['Capacity']))
        j+=1
    print("-"*50)

def practice12():
    print("Delete data in Manchester Club")
    print("Deleting data. Please wait...")
    deletecmd = db.Club.delete_many({'City':'Manchester'})
    print("Finished.")
    readcmd = list(db.Club.find({'City':'Manchester'}))

    j = 1
    for i in readcmd:
        print("{} - {:70} {:70} {:,} people".format(j, i['Stadium_Name'],i['City'], i['Capacity']))
        j+=1
    print("-"*50)

def setDummyData():
    data = [{"Club": "Tottenham Hotspur FC", "Stadium_Name": "Wembley National Stadium", "Country": "England",
             "City": "London", "Capacity": 90652},
            {"Club": "Manchester United FC", "Stadium_Name": "Old Trafford", "Country": "England", "City": "Manchester",
             "Capacity": 74994},
            {"Club": "West Ham United FC", "Stadium_Name": "London Stadium (Olympic Stadium)", "Country": "England",
             "City": "London", "Capacity": 60000},
            {"Club": "Arsenal FC", "Stadium_Name": "Emirates Stadium (Ashburton Grove)", "Country": "England",
             "City": "London", "Capacity": 59867},
            {"Club": "Manchester City FC", "Stadium_Name": "Etihad Stadium (City of Manchester Stadium / Eastlands)",
             "Country": "England", "City": "Manchester", "Capacity": 55017},
            {"Club": "Liverpool FC", "Stadium_Name": "Anfield", "Country": "England", "City": "Liverpool",
             "Capacity": 53394},
            {"Club": "Newcastle United FC", "Stadium_Name": "St. James’ Park", "Country": "England",
             "City": "Newcastle", "Capacity": 52354},
            {"Club": "Chelsea FC", "Stadium_Name": "Stamford Bridge", "Country": "England", "City": "London",
             "Capacity": 41631},
            {"Club": "Everton FC", "Stadium_Name": "Goodison Park", "Country": "England", "City": "Liverpool",
             "Capacity": 39595}, {"Club": "Southampton FC", "Stadium_Name": "St. Mary’s Stadium", "Country": "England",
                                  "City": "Southampton", "Capacity": 32384},
            {"Club": "Leicester City FC", "Stadium_Name": "King Power Stadium (Filbert Way)", "Country": "England",
             "City": "Leicester", "Capacity": 32273},
            {"Club": "Brighton and Hove Albion", "Stadium_Name": "American Express Community Stadium (Falmer Stadium)",
             "Country": "England", "City": "Brighton & Hove", "Capacity": 30666},
            {"Club": "Stoke City FC", "Stadium_Name": "bet365 Stadium", "Country": "England", "City": "Stoke-on-Trent",
             "Capacity": 30089},
            {"Club": "West Bromwich Albion FC", "Stadium_Name": "The Hawthorns", "Country": "England",
             "City": "West Bromwich", "Capacity": 26688},
            {"Club": "Crystal Palace FC", "Stadium_Name": "Selhurst Park", "Country": "England", "City": "London",
             "Capacity": 25456},
            {"Club": "Huddersfield Town FC", "Stadium_Name": "John Smith’s Stadium (Kirklees Stadium)",
             "Country": "England", "City": "Huddersfield", "Capacity": 24169},
            {"Club": "Burnley FC", "Stadium_Name": "Turf Moor", "Country": "England", "City": "Burnley",
             "Capacity": 21944},
            {"Club": "Watford FC", "Stadium_Name": "Vicarage Road", "Country": "England", "City": "Watford",
             "Capacity": 21000},
            {"Club": "AFC Bournemouth", "Stadium_Name": "Vitality Stadium (Dean Court)", "Country": "England",
             "City": "Bournemouth", "Capacity": 11360},
            {"Club": "Sunderland AFC", "Stadium_Name": "Stadium of Light", "Country": "England", "City": "Sunderland",
             "Capacity": 48707},
            {"Club": "Aston Villa FC", "Stadium_Name": "Villa Park", "Country": "England", "City": "Birmingham",
             "Capacity": 42682},
            {"Club": "Sheffield Wednesday FC", "Stadium_Name": "Hillsborough Stadium", "Country": "England",
             "City": "Sheffield", "Capacity": 39812},
            {"Club": "Leeds United FC", "Stadium_Name": "Elland Road", "Country": "England", "City": "Leeds",
             "Capacity": 39460}, {"Club": "Middlesbrough FC", "Stadium_Name": "Riverside Stadium", "Country": "England",
                                  "City": "Middlesbrough", "Capacity": 33746},
            {"Club": "Derby County FC", "Stadium_Name": "Pride Park Stadium", "Country": "England", "City": "Derby",
             "Capacity": 33597},
            {"Club": "Sheffield United FC", "Stadium_Name": "Bramall Lane", "Country": "England", "City": "Sheffield",
             "Capacity": 32702},
            {"Club": "Wolverhampton Wanderers FC", "Stadium_Name": "Molineux Stadium", "Country": "England",
             "City": "Wolverhampton", "Capacity": 32057},
            {"Club": "Nottingham Forest", "Stadium_Name": "City Ground (Trentside)", "Country": "England",
             "City": "Nottingham", "Capacity": 30445},
            {"Club": "Ipswich Town", "Stadium_Name": "Portman Road", "Country": "England", "City": "Ipswich",
             "Capacity": 30311},
            {"Club": "Birmingham City FC", "Stadium_Name": "St. Andrew’s Stadium", "Country": "England",
             "City": "Birmingham", "Capacity": 30009},
            {"Club": "Bolton Wanderers FC", "Stadium_Name": "Macron Stadium", "Country": "England", "City": "Bolton",
             "Capacity": 28723},
            {"Club": "Bristol City FC", "Stadium_Name": "Ashton Gate", "Country": "England", "City": "Bristol",
             "Capacity": 27699},
            {"Club": "Norwich City FC", "Stadium_Name": "Carrow Road", "Country": "England", "City": "Norwich",
             "Capacity": 27033},
            {"Club": "Fulham FC", "Stadium_Name": "Craven Cottage", "Country": "England", "City": "London",
             "Capacity": 25700},
            {"Club": "Hull City AFC", "Stadium_Name": "KCOM Stadium", "Country": "England", "City": "Hull",
             "Capacity": 24983},
            {"Club": "Reading FC", "Stadium_Name": "Madejski Stadium", "Country": "England", "City": "Reading",
             "Capacity": 24161},
            {"Club": "Preston North End FC", "Stadium_Name": "Deepdale Stadium", "Country": "England",
             "City": "Preston", "Capacity": 23404},
            {"Club": "Barnsley FC", "Stadium_Name": "Oakwell Stadium", "Country": "England", "City": "Barnsley",
             "Capacity": 23009},
            {"Club": "Millwall FC", "Stadium_Name": "The Den", "Country": "England", "City": "London",
             "Capacity": 20146},
            {"Club": "Queens Park Rangers", "Stadium_Name": "Loftus Road", "Country": "England", "City": "London",
             "Capacity": 18000},
            {"Club": "Brentford FC", "Stadium_Name": "Griffin Park", "Country": "England", "City": "London",
             "Capacity": 12300}, {"Club": "Burton Albion FC", "Stadium_Name": "Pirelli Stadium", "Country": "England",
                                  "City": "Burton upon Trent", "Capacity": 6912},
            {"Club": "Blackburn Rovers FC", "Stadium_Name": "Ewood Park", "Country": "England", "City": "Blackburn",
             "Capacity": 31154},
            {"Club": "Milton Keynes Dons FC", "Stadium_Name": "Stadium mk (Denbigh Stadium)", "Country": "England",
             "City": "Milton Keynes", "Capacity": 30700},
            {"Club": "Charlton Athletic FC", "Stadium_Name": "The Valley", "Country": "England", "City": "London",
             "Capacity": 27111},
            {"Club": "Wigan Athletic", "Stadium_Name": "DW Stadium", "Country": "England", "City": "Wigan",
             "Capacity": 25138},
            {"Club": "Bradford City FC", "Stadium_Name": "Valley Parade Stadium", "Country": "England",
             "City": "Bradford", "Capacity": 25100},
            {"Club": "Portsmouth FC", "Stadium_Name": "Fratton Park", "Country": "England", "City": "Portsmouth",
             "Capacity": 20821},
            {"Club": "Notts County", "Stadium_Name": "Meadow Lane", "Country": "England", "City": "Nottingham",
             "Capacity": 20229},
            {"Club": "Plymouth Argyle FC", "Stadium_Name": "Home Park", "Country": "England", "City": "Plymouth",
             "Capacity": 16388},
            {"Club": "Blackpool FC", "Stadium_Name": "Bloomfield Road", "Country": "England", "City": "Blackpool",
             "Capacity": 16220},
            {"Club": "Doncaster Rovers FC", "Stadium_Name": "Keepmoat Stadium (Lakeside Spors Complex)",
             "Country": "England", "City": "Doncaster", "Capacity": 15231},
            {"Club": "Peterborough United", "Stadium_Name": "ABAX Stadium (London Road)", "Country": "England",
             "City": "Peterborough", "Capacity": 14319},
            {"Club": "Oxford United FC", "Stadium_Name": "Kassam Stadium", "Country": "England", "City": "Oxford",
             "Capacity": 12500}, {"Club": "Southend United FC", "Stadium_Name": "Roots Hall", "Country": "England",
                                  "City": "Southend-on-Sea", "Capacity": 12392},
            {"Club": "Rotherham United FC", "Stadium_Name": "New York AESSEAL Stadium", "Country": "England",
             "City": "Rotherham", "Capacity": 12021},
            {"Club": "Bury FC", "Stadium_Name": "Gigg Lane", "Country": "England", "City": "Bury", "Capacity": 11840},
            {"Club": "Gillingham FC", "Stadium_Name": "MEMS Priestfield Stadium", "Country": "England",
             "City": "Gillingham", "Capacity": 11582},
            {"Club": "Walsall FC", "Stadium_Name": "Banks’s Stadium (Bescot Stadium)", "Country": "England",
             "City": "Walsall", "Capacity": 11300},
            {"Club": "Oldham Athletic AFC", "Stadium_Name": "Boundary Park", "Country": "England", "City": "Oldham",
             "Capacity": 10638},
            {"Club": "Rochdale AFC", "Stadium_Name": "Spotland Stadium", "Country": "England", "City": "Rochdale",
             "Capacity": 10249},
            {"Club": "Shrewsbury Town FC", "Stadium_Name": "Montgomery Waters Meadow Stadium (New Meadow, Oteley Road)",
             "Country": "England", "City": "Shrewsbury", "Capacity": 9875},
            {"Club": "Yeovil Town FC", "Stadium_Name": "Huish Park Stadium", "Country": "England", "City": "Yeovil",
             "Capacity": 9665},
            {"Club": "Leyton Orient FC", "Stadium_Name": "Matchroom Stadium (Brisbane Road)", "Country": "England",
             "City": "London", "Capacity": 9271},
            {"Club": "Scunthorpe United FC", "Stadium_Name": "Glanford Park", "Country": "England",
             "City": "Scunthorpe", "Capacity": 9088},
            {"Club": "Fleetwood Town FC", "Stadium_Name": "Highbury Stadium", "Country": "England", "City": "Fleetwood",
             "Capacity": 5094},
            {"Club": "West Ham United FC", "Stadium_Name": "Boleyn Ground (Upton Park)", "Country": "England",
             "City": "London", "Capacity": 35345},
            {"Club": "Coventry City FC", "Stadium_Name": "Ricoh Arena", "Country": "England", "City": "Coventry",
             "Capacity": 32609},
            {"Club": "Tottenham Hotspur FC", "Stadium_Name": "White Hart Lane", "Country": "England", "City": "London",
             "Capacity": 32000},
            {"Club": "Port Vale FC", "Stadium_Name": "Vale Park", "Country": "England", "City": "Stoke-on-Trent",
             "Capacity": 19052},
            {"Club": "St. Helens RFC", "Stadium_Name": "Totally Wicked Stadium (St Helens Stadium)",
             "Country": "England", "City": "St Helens", "Capacity": 17646},
            {"Club": "Carlisle United FC", "Stadium_Name": "Brunton Park", "Country": "England", "City": "Carlisle",
             "Capacity": 16980},
            {"Club": "Tranmere Rovers FC", "Stadium_Name": "Prenton Park", "Country": "England", "City": "Birkenhead",
             "Capacity": 16587},
            {"Club": "Swindon Town FC", "Stadium_Name": "County Ground", "Country": "England", "City": "Swindon",
             "Capacity": 15728},
            {"Club": "Bristol Rovers FC", "Stadium_Name": "Bristol Memorial Stadium", "Country": "England",
             "City": "Bristol", "Capacity": 11917},
            {"Club": "Chesterfield FC", "Stadium_Name": "Proact Stadium", "Country": "England", "City": "Chesterfield",
             "Capacity": 10379},
            {"Club": "Wycombe Wanderers FC", "Stadium_Name": "Adams Park", "Country": "England", "City": "Wycombe",
             "Capacity": 10284},
            {"Club": "Luton Town FC", "Stadium_Name": "Kenilworth Road Stadium", "Country": "England", "City": "Luton",
             "Capacity": 10226},
            {"Club": "Crewe Alexandra FC", "Stadium_Name": "Alexandra Stadium (Gresty Road)", "Country": "England",
             "City": "Crewe", "Capacity": 10153},
            {"Club": "Lincoln City FC", "Stadium_Name": "Sincil Bank Stadium (The Bank)", "Country": "England",
             "City": "Lincoln", "Capacity": 10127}, {"Club": "Colchester United FC",
                                                     "Stadium_Name": "Weston Homes Community Stadium (Colchester Community Stadium)",
                                                     "Country": "England", "City": "Colchester", "Capacity": 10084},
            {"Club": "Cambridge United FC", "Stadium_Name": "Abbey Stadium", "Country": "England", "City": "Cambridge",
             "Capacity": 9617},
            {"Club": "Mansfield Town FC", "Stadium_Name": "One Call Stadium (Field Mill)", "Country": "England",
             "City": "Mansfield", "Capacity": 9186},
            {"Club": "Grimsby Town FC", "Stadium_Name": "Blundell Park", "Country": "England", "City": "Grimsby",
             "Capacity": 9052},
            {"Club": "Exeter City FC", "Stadium_Name": "St James Park, Exeter", "Country": "England", "City": "Exeter",
             "Capacity": 8541}, {"Club": "Hartlepool United FC", "Stadium_Name": "Victoria Park", "Country": "England",
                                 "City": "Hartlepool", "Capacity": 7856},
            {"Club": "Northampton Town FC", "Stadium_Name": "Sixfields Stadium", "Country": "England",
             "City": "Northampton", "Capacity": 7653},
            {"Club": "Grantham Town FC", "Stadium_Name": "South Kesteven Sports Stadium (The Meres)",
             "Country": "England", "City": "Grantham", "Capacity": 7500},
            {"Club": "Chaltenham Town FC, Gloucester City AFC", "Stadium_Name": "Abbey Business Stadium (Whaddon Road)",
             "Country": "England", "City": "Chaltenham", "Capacity": 7066},
            {"Club": "Manchester City FC", "Stadium_Name": "Manchester City Football Academy Stadium",
             "Country": "England", "City": "Manchester", "Capacity": 7000},
            {"Club": "Torquay United FC", "Stadium_Name": "Plainmoor", "Country": "England", "City": "Torquay",
             "Capacity": 6500},
            {"Club": "Morecambe FC", "Stadium_Name": "Globe Arena", "Country": "England", "City": "Morecambe",
             "Capacity": 6476},
            {"Club": "Macclesfield Town FC", "Stadium_Name": "Moss Rose", "Country": "England", "City": "Macclesfield",
             "Capacity": 6355},
            {"Club": "Kidderminster Harriers FC", "Stadium_Name": "Aggborough", "Country": "England",
             "City": "Kidderminster", "Capacity": 6238},
            {"Club": "Barnet FC", "Stadium_Name": "The Hive Stadium", "Country": "England", "City": "London",
             "Capacity": 6205},
            {"Club": "Crawley Town FC", "Stadium_Name": "Checkatrade.com Stadium (Broadfield Stadium)",
             "Country": "England", "City": "Crawley", "Capacity": 6134}, {"Club": "Dagenham & Redbridge FC",
                                                                          "Stadium_Name": "Victoria Road (London Borough of Barking & Dagenham Stadium)",
                                                                          "Country": "England", "City": "London",
                                                                          "Capacity": 6078},
            {"Club": "Southport FC", "Stadium_Name": "Merseyrail Community Stadium (Haig Avenue)", "Country": "England",
             "City": "Southport", "Capacity": 6008},
            {"Club": "AFC Fylde", "Stadium_Name": "Mill Farm", "Country": "England", "City": "Medlar with Wesham",
             "Capacity": 6000},
            {"Club": "Chester FC", "Stadium_Name": "Lookers Vauxhall Stadium", "Country": "England", "City": "Chester",
             "Capacity": 5376}, {"Club": "Accrington Stanley FC", "Stadium_Name": "Wham Stadium", "Country": "England",
                                 "City": "Accrington", "Capacity": 5057},
            {"Club": "Forest Green Rovers FC", "Stadium_Name": "The New Lawn", "Country": "England",
             "City": "Nailsworth", "Capacity": 5032},
            {"Club": "Ebbsfleet United FC", "Stadium_Name": "PHB Stadium (Stonebridge Road)", "Country": "England",
             "City": "Northfleet", "Capacity": 5011},
            {"Club": "Kingstonian FC, AFC Wimbledon", "Stadium_Name": "The Cherry Red Records Stadium (Kingsmeadow)",
             "Country": "England", "City": "London", "Capacity": 4850},
            {"Club": "FC United of Manchester", "Stadium_Name": "Broadhurst Park", "Country": "England",
             "City": "Manchester", "Capacity": 4400},
            {"Club": "Dartford FC", "Stadium_Name": "Princes Park Stadium (Dartford)", "Country": "England",
             "City": "Dartford", "Capacity": 4100},
            {"Club": "Hyde FC", "Stadium_Name": "Ewen Fields", "Country": "England", "City": "Hyde", "Capacity": 4073},
            {"Club": "Curzon Ashton FC", "Stadium_Name": "Tameside Stadium", "Country": "England",
             "City": "Ashton-under-Lyne", "Capacity": 4000},
            {"Club": "Salford City FC", "Stadium_Name": "Moor Lane", "Country": "England", "City": "Salford",
             "Capacity": 3339},
            {"Club": "Lewes FC", "Stadium_Name": "The Dripping Pan", "Country": "England", "City": "Lewes",
             "Capacity": 3000}, {"Club": "Matlock Town FC", "Stadium_Name": "DCJ Group Insurance Arena (Causeway Lane)",
                                 "Country": "England", "City": "Matlock", "Capacity": 2757},
            {"Club": "Hallam FC", "Stadium_Name": "Sandygate Road", "Country": "England", "City": "Sheffield",
             "Capacity": 700},
            {"Club": "Arsenal FC", "Stadium_Name": "Arsenal Stadium (Highbury) – until 2006", "Country": "England",
             "City": "London", "Capacity": 38500},
            {"Club": "Manchester City FC", "Stadium_Name": "Maine Road – until 2003", "Country": "England",
             "City": "Manchester", "Capacity": 35150},
            {"Club": "Stoke City FC", "Stadium_Name": "Victoria Ground – until 1997", "Country": "England",
             "City": "Stoke-on-Trent", "Capacity": 22500},
            {"Club": "Manchester City", "Stadium_Name": "Etihad Stadium", "Country": "England", "City": "Manchester",
             "Capacity": 62170},
            {"Club": "Tottenham", "Stadium_Name": "New Tottenham Stadium", "Country": "England", "City": "London",
             "Capacity": 61559},
            {"Club": "Liverpool FC", "Stadium_Name": "Anfield", "Country": "England", "City": "Liverpool",
             "Capacity": 58800},
            {"Club": "Wanderers", "Stadium_Name": "Molineux Stadium", "Country": "England", "City": "Wolverhampton",
             "Capacity": 37500},
            {"Club": "Brentford FC", "Stadium_Name": "Brentford Community Stadium", "Country": "England",
             "City": "London", "Capacity": 17250},
            {"Club": "Oldham Athletic", "Stadium_Name": "Boundary Park", "Country": "England", "City": "Oldham",
             "Capacity": 13000},
            {"Club": "York City, Knights", "Stadium_Name": "York Community Stadium", "Country": "England",
             "City": "York", "Capacity": 8113},
            {"Club": "Ebbsfleet United", "Stadium_Name": "PHB Stadium", "Country": "England", "City": "Northfleet",
             "Capacity": 6000},
            {"Club": "Salford City", "Stadium_Name": "Moor Lane", "Country": "England", "City": "Salford",
             "Capacity": 5108},
            {"Club": "Chelsea FC", "Stadium_Name": "Stamford Bridge", "Country": "England", "City": "London",
             "Capacity": 60000},
            {"Club": "Sheffield United", "Stadium_Name": "Bramall Lane", "Country": "England", "City": "Sheffield",
             "Capacity": 41300},
            {"Club": "Crystal Palace", "Stadium_Name": "Selhurst Park", "Country": "England", "City": "London",
             "Capacity": 34000},
            {"Club": "Fulham FC", "Stadium_Name": "Craven Cottage", "Country": "England", "City": "London",
             "Capacity": 29600},
            {"Club": "Southend United", "Stadium_Name": "Fossetts Farm Stadium", "Country": "England",
             "City": "Southend-on-Sea", "Capacity": 21001},
            {"Club": "Wimbledon", "Stadium_Name": "Plough Lane", "Country": "England", "City": "London",
             "Capacity": 2000},
            {"Club": "Luton Town", "Stadium_Name": "Power Court Stadium", "Country": "England", "City": "Luton",
             "Capacity": 17500},
            {"Club": "Grimsby Town", "Stadium_Name": "Grimsby Community Stadium", "Country": "England",
             "City": "Grimsby", "Capacity": 14000},
            {"Club": "Cambridge United", "Stadium_Name": "Abbey Stadium", "Country": "England", "City": "Cambridge",
             "Capacity": 11000},
            {"Club": "Forest Green Rovers", "Stadium_Name": "Eco Park (I)", "Country": "England", "City": "Stonehouse",
             "Capacity": 10000},
            {"Club": "Leamington FC", "Stadium_Name": "Leamington Community Stadium", "Country": "England",
             "City": "Leamington Spa", "Capacity": 5000},
            {"Club": "Stanley", "Stadium_Name": "Wham Stadium", "Country": "England", "City": "Accrington",
             "Capacity": 5000},
            {"Club": "Boston United", "Stadium_Name": "Boston Community Stadium", "Country": "England",
             "City": "Boston", "Capacity": 42329},
            {"Club": "Cambridge City", "Stadium_Name": "Sawston Ground", "Country": "England", "City": "Sawston",
             "Capacity": 3000},
            {"Club": "Arsenal Londyn", "Stadium_Name": "Emirates Stadium", "Country": "England", "City": "London",
             "Capacity": 60000},
            {"Club": "West Ham United", "Stadium_Name": "London Olympic Stadium", "Country": "England",
             "City": "London", "Capacity": 60000},
            {"Club": "Coventry City FC", "Stadium_Name": "Ricoh Arena", "Country": "England", "City": "Coventry",
             "Capacity": 32000},
            {"Club": "Bristol City", "Stadium_Name": "Ashton Gate", "Country": "England", "City": "Bristol",
             "Capacity": 27000},
            {"Club": "Brighton & Hove Albion FC", "Stadium_Name": "American Express Community Stadium",
             "Country": "England", "City": "Brighton & Hove", "Capacity": 22347},
            {"Club": "Rotherham United", "Stadium_Name": "Rotherham United Stadium", "Country": "England",
             "City": "Rotherham", "Capacity": 12000},
            {"Club": "Manchester City", "Stadium_Name": "City Football Academy Arena", "Country": "England",
             "City": "Manchester", "Capacity": 7000},
            {"Club": "FC United, Moston Juniors", "Stadium_Name": "Broadhurst Park", "Country": "England",
             "City": "Manchester", "Capacity": 5000},
            {"Club": "Liverpool FC", "Stadium_Name": "Stanley Park (New Anfield)", "Country": "England",
             "City": "Liverpool", "Capacity": 73000},
            {"Club": "Chelsea FC", "Stadium_Name": "Chelsea Battersea Stadium", "Country": "England", "City": "London",
             "Capacity": 60000},
            {"Club": "Liverpool FC", "Stadium_Name": "Stanley Park (New Anfield)", "Country": "England",
             "City": "Liverpool", "Capacity": 60000},
            {"Club": "Tottenham", "Stadium_Name": "New Tottenham Stadium", "Country": "England", "City": "London",
             "Capacity": 56250},
            {"Club": "Everton", "Stadium_Name": "King’s Dock Stadium", "Country": "England", "City": "Liverpool",
             "Capacity": 55000},
            {"Club": "Newcastle United", "Stadium_Name": "Leazes Park Stadium", "Country": "England",
             "City": "Newcastle", "Capacity": 55000},
            {"Club": "Everton FC", "Stadium_Name": "Kirkby Stadium", "Country": "England", "City": "Kirkby",
             "Capacity": 50401}, {"Club": "Southampton FC", "Stadium_Name": "St. Mary’s Stadium", "Country": "England",
                                  "City": "Southampton", "Capacity": 50000},
            {"Club": "Everton", "Stadium_Name": "Walton Hall Park Stadium (I)", "Country": "England",
             "City": "Liverpool", "Capacity": 50000},
            {"Club": "Everton", "Stadium_Name": "Walton Hall Park Stadium (II)", "Country": "England",
             "City": "Liverpool", "Capacity": 50000},
            {"Club": "QPR", "Stadium_Name": "New Queens Park", "Country": "England", "City": "London",
             "Capacity": 40000},
            {"Club": "Portsmouth FC", "Stadium_Name": "Portsmouth Dockland Stadium", "Country": "England",
             "City": "Portsmouth", "Capacity": 36000},
            {"Club": "Bristol City", "Stadium_Name": "Bristol City Stadium", "Country": "England", "City": "Bristol",
             "Capacity": 30000},
            {"Club": "Fulham FC", "Stadium_Name": "Craven Cottage", "Country": "England", "City": "London",
             "Capacity": 30000},
            {"Club": "Coventry City", "Stadium_Name": "Coventry City Stadium", "Country": "England", "City": "Coventry",
             "Capacity": 23000},
            {"Club": "Bristol Rovers", "Stadium_Name": "UWE Stadium", "Country": "England", "City": "Bristol",
             "Capacity": 21700},
            {"Club": "Rovers", "Stadium_Name": "New Memorial Stadium", "Country": "England", "City": "Bristol",
             "Capacity": 18500},
            {"Club": "Oldham Athletic", "Stadium_Name": "Oldham Arena", "Country": "England", "City": "Oldham",
             "Capacity": 16000},
            {"Club": "Scunthorpe United", "Stadium_Name": "Scunthorpe United Stadium", "Country": "England",
             "City": "Scunthorpe", "Capacity": 12000},
            {"Club": "Forest Green Rovers", "Stadium_Name": "Eco Park (II)", "Country": "England", "City": "Stonehouse",
             "Capacity": 10000}, {"Club": "Forest Green Rovers", "Stadium_Name": "Eco Park (III)", "Country": "England",
                                  "City": "Stonehouse", "Capacity": 10000},
            {"Club": "Fulham FC", "Stadium_Name": "Craven Cottage (I)", "Country": "England", "City": "London",
             "Capacity": 39000},
            {"Club": "Tottenham Hotspur", "Stadium_Name": "New Tottenham Stadium", "Country": "England",
             "City": "London", "Capacity": 12345},
            {"Club": "Salford City", "Stadium_Name": "Moor Lane", "Country": "England", "City": "Salford",
             "Capacity": 24564},
            {"Club": "Liverpool FC", "Stadium_Name": "Anfield", "Country": "England", "City": "Liverpool",
             "Capacity": 30978},
            {"Club": "Bristol City FC", "Stadium_Name": "Ashton Gate", "Country": "England", "City": "Bristol",
             "Capacity": 12312},
            {"Club": "Manchester City FC", "Stadium_Name": "Etihad Stadium (City of Manchester Stadium / Eastlands)",
             "Country": "England", "City": "Manchester", "Capacity": 32412},
            {"Club": "FC United of Manchester", "Stadium_Name": "Broadhurst Park (Moston Community Stadium)",
             "Country": "England", "City": "Manchester", "Capacity": 4567},
            {"Club": "Manchester City FC", "Stadium_Name": "City Football Academy Arena", "Country": "England",
             "City": "Manchester", "Capacity": 12312},
            {"Club": "Wolverhampton Wanderers", "Stadium_Name": "Molineux แ", "Country": "England",
             "City": "Wolverhampton", "Capacity": 11111},
            {"Club": "Brighton & Hove Albion FC", "Stadium_Name": "American Express Community Stadium (Falmer Stadium)",
             "Country": "England", "City": "Brighton & Hove", "Capacity": 23212},
            {"Club": "Morecambe FC", "Stadium_Name": "Globe Arena (Morecambe FC New Stadium)", "Country": "England",
             "City": "Morecambe", "Capacity": 5652}]

    db.Club.insert_many(data)
    print("finished")

def text_hello(other):
    try:
        print("-" * 100)
        if other == 0:
            print("*\t\t\t\033[0;34;43mSelect Homework below !!!\033[0;0m\t\t\t*")
        else:
            print("*\t\t\t\033[0;34;43mSelect Other Homework below !!!\033[0;0m\t\t\t*")
        print("-" * 100)
        select_quiz = input("Select No. / Name Of Homework (1-12, [dummyData] or 0 for Autorun) for Check : ")
        print("-" * 100)
        select_to_run(select_quiz)
    except Exception as e:
        print("-" * 100)
        print("\033[0;31;40m ERROR !!!\033[0;0m >>>>>>>>>> {}".format(e))
        text_hello(0)

def select_to_run(select_quiz):
    try:
        if select_quiz == "0":
            practice1()
            practice2()
            practice3()
            practice4()
            practice5()
            practice6()
            practice7()
            practice8()
            practice9()
            practice10()
            practice11()
            practice12()

        elif select_quiz == "1":
            practice1()

        elif select_quiz == "2":
            practice2()

        elif select_quiz == "3":
            practice3()
        elif select_quiz == "4":
            practice4()

        elif select_quiz == "5":
            practice5()

        elif select_quiz == "6":
            practice6()

        elif select_quiz == "7":
            practice7()

        elif select_quiz == "8":
            practice8()

        elif select_quiz == "9":
            practice9()

        elif select_quiz == "10":
            practice10()

        elif select_quiz == "11":
            practice11()

        elif select_quiz == "12":
            practice12()

        elif select_quiz == "dummyData":
            setDummyData()

        text_hello(1)
    except Exception as e:
        print("-"*100)
        print("\033[0;31;40m ERROR !!!\033[0;0m >>>>>>>>>> {}".format(e))
        text_hello(0)

if __name__ == '__main__':
    text_hello(0)

