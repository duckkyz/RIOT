import pickle
import time
import json
import os
import RiotAPI
from RiotAPI import RiotAPICall
from RiotAPI import GameData
from RiotAPI import ChampIDName

def getPlayerName(player_name):
    #player_name = raw_input("Summoner Name: ")
    storageLoc = str(os.getcwd()) + "/" + player_name
    if not os.path.exists(storageLoc):
        os.makedirs(storageLoc)
    return player_name

def getData(player_name):
    api2 = RiotAPICall()
    api2.api_key = 'aa7ee812-3a61-47c1-8ddf-357cd4eef032'
    api2.region = 'na'

    storageLoc = str(os.getcwd()) + "/" + player_name + "/"

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

    fileExt = str(storageLoc + "games.txt")

    myfile = open(fileExt,"w")
    json.dump((games),myfile)

def insertRGD(player_name):

    storageLoc = str(os.getcwd()) + "/" + player_name + "/"

    fileExt = str(storageLoc + "RGD.txt")
    otherFE = str(storageLoc + "games.txt")

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
    fileExt = str(storageLoc + "RGD.txt")
    myfile = open(fileExt,"w")
    pickle.dump((gameFile),myfile)
    myfile.close()

def spitDataOut(summoner_name):
#Prints out what is in the file
    #player_name = raw_input("Summoner Name: ")
    player_name = getPlayerName(summoner_name)
    storageLoc = str(os.getcwd()) + "/" + player_name + "/"
    fileExt = str(storageLoc + "RGD.txt")
    myfile = open(fileExt,"r")
    data = pickle.load(myfile)
    wins = 0

    ChampData = ChampIDName
    ChampData = RiotAPI.ChampIndex()

    #myThing = pickle.load(myfile)
    #data = myThing['games']
    count1 = 0
    for otherthing in data:
        count1 = count1 + 1
    print(str(count1) + "games")
    role_0 = []
    role_1 = []
    role_2 = []
    role_3 = []
    role_4 = []
    for j in range(0,count1):
        if (str(data[j].gameMode) == 'CLASSIC'):
            if (str(data[j].playerRole) == '0'):
                role_0.append(data[j].championId)
            elif (str(data[j].playerRole) == '1'):
                role_1.append(data[j].championId)
            elif (str(data[j].playerRole) == '2'):
                role_2.append(data[j].championId)
            elif (str(data[j].playerRole) == '3'):
                role_3.append(data[j].championId)
            elif (str(data[j].playerRole) == '4'):
                role_4.append(data[j].championId)
            else:
                print("Player role in game " + str(j) + " is wrong...")
        else:
            print("Game " + str(j) + " is not a classic game")

    for i in range(0,count1):
        # Created an object called GameData that has all the possible paramaters in a game json
        # These are all set to 0 to avoid invalid calling, the following function should just
        # scan in the values and place them into the corresonding one if it exists
        # SHOULD BE SUPER RAD
        print("Game #" + str(i+1))
        print("Game ID                      : " + str(data[i].gameId))
        print("Create Date                  : " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((data[i].createDate)/1000))))
        j = 0
        champFound = 0
        for ids in ChampData:
            if (ids == data[i].championId):
                champFound = 1
                print("Champion ID                  : " + str(data[i].championId))
                try:
                    print("Champion Name                : " + str(ChampData[ids]))
                except:
                    print("Champion Name does not exist in database")
            j += 1
        if (champFound == 0):
            print("Champion ID                  : " + str(data[i].championId))
            print("Champion Name does not exist in database")

        print("Game Mode                    : " + str(data[i].gameMode))
        print("Game Type                    : " + str(data[i].subType))
        print("Summoner Level               : " + str(data[i].sumlevel))
        print("IP Earned                    : " + str(data[i].ipEarned))
        print("Summoner Spell 1             : " + str(data[i].spell1))
        print("Summoner Spell 2             : " + str(data[i].spell2))
        print("Champions Killed             : " + str(data[i].championsKilled))
        print("Victory                      : " + str(data[i].win))
        if (str(data[i].win) == 'True'):
            wins += 1
        print("Wards Placed                 : " + str(data[i].wardPlaced))
        print("Total Damage Dealt           : " + str(data[i].totalDamageDealt))
        print("Magic Damage Dealt To Champs : " + str(data[i].magicDamageDealtToChampions))
        # Player position desc:
        #   0: Mid
        #   1: Top
        #   2: Support
        #   3: Jungle
        #   4: ADC
        #
        if (data[i].gameMode == 'ARAM'):
            player_role = '0'
        else:
            player_role = str(data[i].playerPosition)
        print("Player Position              : " + str(roleCases(player_role)))
        print("Largest MultiKill            : " + str(data[i].largestMultiKill))
        print("Largest Killing Spree        : " + str(data[i].largestKillingSpree))
        print("Magic Damage Taken           : " + str(data[i].magicDamageTaken))
        print("Total Time CC Dealt          : " + str(data[i].totalTimeCrowdControlDealt))
        print("Wards Killed                 : " + str(data[i].wardKilled))
        print("Item 0                       : " + str(data[i].item0))
        print("Item 1                       : " + str(data[i].item1))
        print("Item 2                       : " + str(data[i].item2))
        print("Item 3                       : " + str(data[i].item3))
        print("Item 4                       : " + str(data[i].item4))
        print("Item 5                       : " + str(data[i].item5))
        print("Item 6                       : " + str(data[i].item6))
        print("Minions Killed               : " + str(data[i].minionsKilled))
        print("Vision Wards Bought          : " + str(data[i].visionWardsBought))
        print("Time Played                  : " + str(data[i].timePlayed))
        print("Assists                      : " + str(data[i].assists))
        print("Player Role                  : " + str(data[i].playerRole))
        print("Phys Damage Dealt To Champs  : " + str(data[i].physicalDamageDealtToChampions))
        print("Gold Spent                   : " + str(data[i].goldSpent))
        print("Champ Level                  : " + str(data[i].champlevel))
        print("Phys Damage Dealt to Player  : " + str(data[i].physicalDamageDealtPlayer))
        print("Total Healing                : " + str(data[i].totalHeal))
        print("Gold Earned                  : " + str(data[i].goldEarned))
        print("Total Damage Dealt to Champs : " + str(data[i].totalDamageDealtToChampions))
        print("Total Units Healed           : " + str(data[i].totalUnitsHealed))
        print("Num Deaths                   : " + str(data[i].numDeaths))
        print("Total Damage Taken           : " + str(data[i].totalDamageTaken))
        print("Killing Sprees               : " + str(data[i].killingSprees))
        print("Magic Damage Dealt to Player : " + str(data[i].magicDamageDealtPlayer))
        print("Physical Damage Taken        : " + str(data[i].physicalDamageTaken))
        print(" ")
        print(" ")
    fWins = float(wins)
    fGames = float(count1)
    pWins = (fWins/fGames) * 100
    print("Win rate: {0:.2f}%").format(pWins)

def roleCases(player_role):
    roles = {
        '0': 'Middle',
        '1': 'Top',
        '2': 'ADC',
        '3': 'Jungle',
        '4': 'Support'
    }
    return (roles[str(player_role)])

def testingFunct(summoner_name):
# 12/31/15: Testing for sorting function
#   [Number of Games] [Wins] [Average K/D/A] [Average CS] [% Top] [% Mid] [% Jungle] [% ADC] [% Support]
    player_name = getPlayerName(summoner_name)
    storageLoc = str(os.getcwd()) + "/" + player_name + "/"
    fileExt = str(storageLoc + "RGD.txt")
    myfile = open(fileExt,"r")
    data = pickle.load(myfile)
    aData = []
    killAvg = 0
    deathAvg = 0
    assistAvg = 0
    csAvg = 0
    wins = 0
    #Additional Info:
    wardPlaceAvg = 0
    wardKillAvg = 0
    wardPinkBought = 0
    gameTimeAvg = 0
    ipEarnedAvg = 0

    ChampData = ChampIDName
    ChampData = RiotAPI.ChampIndex()

    #myThing = pickle.load(myfile)
    #data = myThing['games']
    totGames = 0
    for otherthing in data:
        totGames = totGames + 1

#####sorting function:###############################
    gClassic = []                                   #
    gAram = []                                      #
    gRanked = []                                    #
    gOther = []                                     #
    for j in range(0,totGames):                     #
        if(str(data[j].gameMode) == 'CLASSIC'):     #
            gClassic.append(data[j])                #
        elif(str(data[j].gameMode) == 'ARAM'):      #
            gAram.append(data[j])                   #
        elif(str(data[j].gameMode) == 'RANKED'):    #
            gRanked.append(data[j])                 #
        else:                                       #
            gOther.append(data[j])                  #
#####################################################
    aData = gClassic

    numGames = 0
    for q in aData:
        numGames = numGames + 1
    role_0 = 0 #Top
    role_1 = 0 #Middle
    role_2 = 0 #Jungle
    role_3 = 0 #ADC
    role_4 = 0 #Support

    for i in range(0,numGames):
        killAvg = killAvg + float(aData[i].championsKilled)
        deathAvg = deathAvg + float(aData[i].numDeaths)
        assistAvg = assistAvg + float(aData[i].assists)
        csAvg = csAvg + float(aData[i].minionsKilled)
        if (str(data[i].win) == 'True'):
            wins += 1
        if (str(aData[i].playerPosition) == '1'): #top
            role_0 = role_0 + 1
        elif (str(aData[i].playerPosition) == '2'): #middle
            role_1 = role_1 + 1
        elif (str(aData[i].playerPosition) == '3'): #Jungle
            role_2 = role_2 + 1
        elif (str(aData[i].playerPosition) == '4'): #bot
            if (str(aData[i].playerRole) == '2'): #support
                role_4 = role_4 + 1
            else: #ADC
                role_3 = role_3 + 1
        else:
            print("Player role in game " + str(j) + " is wrong...")
        wardPlaceAvg = wardPlaceAvg + float(aData[i].wardPlaced)
        wardKillAvg = wardKillAvg + float(aData[i].wardKilled)
        wardPinkBought = wardPinkBought + float(aData[i].visionWardsBought)
        gameTimeAvg = gameTimeAvg + float(aData[i].timePlayed)
        ipEarnedAvg = ipEarnedAvg + float(aData[i].ipEarned)

    fWins = float(wins)
    fGames = float(numGames)
    pWins = (fWins/fGames) * 100
    pRole_0 = ((float(role_0))/fGames) * 100
    pRole_1 = ((float(role_1))/fGames) * 100
    pRole_2 = ((float(role_2))/fGames) * 100
    pRole_3 = ((float(role_3))/fGames) * 100
    pRole_4 = ((float(role_4))/fGames) * 100
    killAvg = (killAvg/fGames)
    deathAvg = (deathAvg/fGames)
    assistAvg = (assistAvg/fGames)
    csAvg = (csAvg/fGames)
    #Additional Info:
    wardPlaceAvg = (wardPlaceAvg/fGames)
    wardKillAvg = (wardKillAvg/fGames)
    wardPinkBought = (wardPinkBought/fGames)
    gameTimeAvg = ((gameTimeAvg/60)/fGames)
    ipEarnedAvg = ipEarnedAvg

    print("[Games]      : " + str(numGames))
    print("[Wins]       : " + ("{0:.2f}%").format(pWins))
    print("[K/D/A]      : " + ("{0:.0f}").format(killAvg) + '/' + ("{0:.0f}").format(deathAvg)
          + '/' + ("{0:.0f}").format(assistAvg))
    print("[Avg CS]     : " + ("{0:.0f}").format(csAvg))
    print("[% Top]      : " + ("{0:.2f}%").format(pRole_0))
    print("[% Mid]      : " + ("{0:.2f}%").format(pRole_2))
    print("[% Jungle]   : " + ("{0:.2f}%").format(pRole_1))
    print("[% ADC]      : " + ("{0:.2f}%").format(pRole_3))
    print("[% Support]  : " + ("{0:.2f}%").format(pRole_4))

    print("[Avg Wards]  : " + ("{0:.0f}").format(wardPlaceAvg))
    print("[Ward Kills] : " + ("{0:.0f}").format(wardKillAvg))
    print("[Avg Pinks]  : " + ("{0:.0f}").format(wardPinkBought))
    print("[Avg GTime]  : " + ("{0:.0f}").format(gameTimeAvg))
    print("[IP earned]  : " + ("{0:.0f}").format(ipEarnedAvg))
