import pickle
import json
import time
from RiotAPI import RiotAPI
from RiotAPI import GameData

def getPlayerName():
    print("Format player name \"Name\" ")
    player_name = str(input("Summoner Name: "))
    return player_name

def getData(player_name):
    api2 = RiotAPI()
    api2.api_key = 'aa7ee812-3a61-47c1-8ddf-357cd4eef032'
    api2.region = 'na'

    response = api2.get_summoner_by_name(player_name)

    try:
        for key in response.keys():
            try:
                account_name = key
            except:
                print("ERROR ACCOUNT NAME DOES NOT EXIST, EXITING")
                print("ERROR 2")
                exit()
    except:
        print("ERROR SUMMONER DOES NOT EXIST, EXITING")
        print("ERROR 1")
        exit()

    summonerId = response[account_name]["id"]
    games = api2.games_by_summoner(summonerId)

    fileExt = str("/Users/Ben/Documents/"+player_name+"_games.txt")

    myfile = open(fileExt,"w")
    json.dump((games),myfile)

def insertRGD(player_name):

    fileExt = str("/Users/Ben/Documents/"+player_name+"_RGD.txt")
    otherFE = str("/Users/Ben/Documents/"+player_name+"_games.txt")

    ids = []
    oldGameCount = 0

    try:
        myfile = open((fileExt),'r')
        gameFile = pickle.load(myfile)
        myfile.close()

        for numGames in gameFile:
            oldGameCount = oldGameCount + 1

        for i in range(0, oldGameCount):
            gameId = gameFile[i].gameId
            ids.append(gameId)
    except:
        myfile = open((fileExt), 'w')
        myfile.close()
        myfile = open((fileExt), 'r')
        gameFile = []


    try:
        myOF = open((otherFE),'r')
        myThing = json.load(myOF)
        data = myThing['games']
        myOF.close()
    except:
        print("Game file does not exist, please run function 1")
        exit()

    newGameCount = 0
    for newGames in data:
        newGameCount = newGameCount + 1

    games = []

    for i in range(0,newGameCount):
        # Created an object called GameData that has all the possible paramaters in a game json
        # These are all set to 0 to avoid invalid calling, the following function should just
        # scan in the values and place them into the corresonding one if it exists
        # SHOULD BE SUPER RAD
        gamecall = GameData()
        for keys3 in data[i]:
            if (str(keys3) == 'stats' ):
                for subkeys in data[i]['stats']:
                    if (str(subkeys) == 'level'):
                        setattr(gamecall,'champlevel',data[i]['stats'][str(subkeys)])
                    else:
                        try:
                            setattr(gamecall, subkeys, data[i]['stats'][str(subkeys)])
                        except KeyError:
                            #print(str(subkeys) + " does not exist in this game")
                            setattr(gamecall, subkeys, '0')
            else:
                if (str(keys3) == 'level'):
                    setattr(gamecall,'sumlevel',data[i][str(keys3)])
                else:
                    try:
                        setattr(gamecall, keys3, data[i][str(keys3)])
                    except KeyError:
                        #print(str(keys3) + " does not exist in this game")
                        setattr(gamecall, keys3, '0')
            if keys3 == 'gameId':
                for p in range(0, oldGameCount):
                    if data[i]['gameId'] == ids[p]:
                        setattr(gamecall, 'append', 0)
                        print("Game "+str(i+1)+" ID matches old game #"+str(p+1))
                        break

        if gamecall.append == 1:
            print("Game " + str(i+1) + " appended")
            gameFile.append(gamecall)

    gameFile = sorted(gameFile, key=lambda GameData: GameData.gameId)
    fileExt = str("/Users/Ben/Documents/"+player_name+"_RGD.txt")
    myfile = open(fileExt,"w")
    pickle.dump((gameFile),myfile)
    myfile.close()