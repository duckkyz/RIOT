import pickle
import json
import time
import os
import RGDProtocol
from RiotAPI import RiotAPI
from RiotAPI import GameData


def main(task):
    if task == 1:
    #Testing file creation and getting local file.
        print(os.getcwd())

    elif task == 2:
    #undo that JSON and put it in a new file then print out that info
        player_name = str(input("Summoner Name: "))
        fileExt = str("/Users/Ben/Documents/"+player_name+"_games.txt")
        myfile = open(fileExt,"r")
        myThing = json.load(myfile)
        data = myThing['games']
        count1 = 0
        for otherthing in data:
            count1 = count1 + 1
        print(count1)
        games = []
        for i in range(0,count1):
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

            print("Game #" + str(i+1))
            print("Game ID                      : " + str(gamecall.gameId))
            print("Create Date                  : " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((gamecall.createDate)/1000))))
            print("Champion ID                  : " + str(gamecall.championId))
            print("Game Mode                    : " + str(gamecall.gameMode))
            print("Game Type                    : " + str(gamecall.subType))
            print("Summoner Level               : " + str(gamecall.sumlevel))
            print("IP Earned                    : " + str(gamecall.ipEarned))
            print("Summoner Spell 1             : " + str(gamecall.spell1))
            print("Summoner Spell 2             : " + str(gamecall.spell2))
            print("Champions Killed             : " + str(gamecall.championsKilled))
            print("Victory                      : " + str(gamecall.win))
            print("Wards Placed                 : " + str(gamecall.wardPlaced))
            print("Total Damage Dealt           : " + str(gamecall.totalDamageDealt))
            print("Magic Damage Dealt To Champs : " + str(gamecall.magicDamageDealtToChampions))
            print("Player Position              : " + str(gamecall.playerPosition))
            print("Largest MultiKill            : " + str(gamecall.largestMultiKill))
            print("Largest Killing Spree        : " + str(gamecall.largestKillingSpree))
            print("Magic Damage Taken           : " + str(gamecall.magicDamageTaken))
            print("Total Time CC Dealt          : " + str(gamecall.totalTimeCrowdControlDealt))
            print("Wards Killed                 : " + str(gamecall.wardKilled))
            print("Item 0                       : " + str(gamecall.item0))
            print("Item 1                       : " + str(gamecall.item1))
            print("Item 2                       : " + str(gamecall.item2))
            print("Item 3                       : " + str(gamecall.item3))
            print("Item 4                       : " + str(gamecall.item4))
            print("Item 5                       : " + str(gamecall.item5))
            print("Item 6                       : " + str(gamecall.item6))
            print("Minions Killed               : " + str(gamecall.minionsKilled))
            print("Vision Wards Bought          : " + str(gamecall.visionWardsBought))
            print("Time Playe                   : " + str(gamecall.timePlayed))
            print("Assists                      : " + str(gamecall.assists))
            print("Player Role                  : " + str(gamecall.playerRole))
            print("Phys Damage Dealt To Champs  : " + str(gamecall.physicalDamageDealtToChampions))
            print("Gold Spent                   : " + str(gamecall.goldSpent))
            print("Champ Level                  : " + str(gamecall.champlevel))
            print("Phys Damage Dealt to Player  : " + str(gamecall.physicalDamageDealtPlayer))
            print("Total Healing                : " + str(gamecall.totalHeal))
            print("Gold Earned                  : " + str(gamecall.goldEarned))
            print("Total Damage Dealt to Champs : " + str(gamecall.totalDamageDealtToChampions))
            print("Total Units Healed           : " + str(gamecall.totalUnitsHealed))
            print("Num Deaths                   : " + str(gamecall.numDeaths))
            print("Total Damage Taken           : " + str(gamecall.totalDamageTaken))
            print("Killing Sprees               : " + str(gamecall.killingSprees))
            print("Magic Damage Dealt to Player : " + str(gamecall.magicDamageDealtPlayer))
            print("Physical Damage Taken        : " + str(gamecall.physicalDamageTaken))
            print(" ")
            print(" ")
            games.append(gamecall)
        fileExt = str("/Users/Ben/Documents/"+player_name+"_Test.txt")
        myfile = open(fileExt,"w")
        pickle.dump((games),myfile)
        myfile.close()
        myfile = open((fileExt),'r')
        test = pickle.load(myfile)


        #Not working below this


    elif task == 3:
    #Like task 2 but better because it checks to see if games are already in there and only puts games that arent there.
    #saves to a new file
        player_name = str(input("Summoner Name: "))

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

    elif task == 4:
        print("Getting and putting data in rolling game file")
        player_name = RGDProtocol.getPlayerName()
        RGDProtocol.getData(player_name)
        RGDProtocol.insertRGD(player_name)

    else:
    #Prints out what is in the file
        player_name = str(input("Summoner Name: "))
        fileExt = str("/Users/Ben/Documents/"+player_name+"_RGD.txt")
        myfile = open(fileExt,"r")
        data = pickle.load(myfile)
        #myThing = pickle.load(myfile)
        #data = myThing['games']
        count1 = 0
        for otherthing in data:
            count1 = count1 + 1
        print(count1)
        games = []
        for i in range(0,count1):
            # Created an object called GameData that has all the possible paramaters in a game json
            # These are all set to 0 to avoid invalid calling, the following function should just
            # scan in the values and place them into the corresonding one if it exists
            # SHOULD BE SUPER RAD
            print("Game #" + str(i+1))
            print("Game ID                      : " + str(data[i].gameId))
            print("Create Date                  : " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((data[i].createDate)/1000))))
            print("Champion ID                  : " + str(data[i].championId))
            print("Game Mode                    : " + str(data[i].gameMode))
            print("Game Type                    : " + str(data[i].subType))
            print("Summoner Level               : " + str(data[i].sumlevel))
            print("IP Earned                    : " + str(data[i].ipEarned))
            print("Summoner Spell 1             : " + str(data[i].spell1))
            print("Summoner Spell 2             : " + str(data[i].spell2))
            print("Champions Killed             : " + str(data[i].championsKilled))
            print("Victory                      : " + str(data[i].win))
            print("Wards Placed                 : " + str(data[i].wardPlaced))
            print("Total Damage Dealt           : " + str(data[i].totalDamageDealt))
            print("Magic Damage Dealt To Champs : " + str(data[i].magicDamageDealtToChampions))
            print("Player Position              : " + str(data[i].playerPosition))
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
            print("Time Playe                   : " + str(data[i].timePlayed))
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


if __name__ == "__main__":
    print("Just type 4)")
    task = int(input("Task: "))
    main(task)

