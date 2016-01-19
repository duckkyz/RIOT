import os
import RGDProtocol

def main(task, summoner_name):
    if task == 1:
        print("Getting and putting data in rolling game file")
        player_name = RGDProtocol.getPlayerName(summoner_name)
        RGDProtocol.getData(player_name)
        RGDProtocol.insertRGD(player_name)

    elif task == 3:
        # 12/31/15: Testing for sorting function
        #   [Number of Games] [Wins] [Average K/D/A] [Average CS] [% Top] [% Mid] [% Jungle] [% ADC] [% Support]
        RGDProtocol.testingFunct(summoner_name)

    else:
        RGDProtocol.spitDataOut(summoner_name)



if __name__ == "__main__":
    loopVar = 1
    loopCount = 0
    timeOut = 10
    summoner_name = raw_input("Summoner Name: ")
    while ((loopVar == 1) and (timeOut > loopCount)):
        print("Task functions: ")
        print("\tCreate/Append Game data : 1")
        print("\tPrint out raw game data : 2")
        print("\tTesting function        : 3")
        print("\tChange User             : 8")
        print("\tQuit                    : 9")
        print("")
        task = int(input("Task: "))

        if ((task == 1) or (task == 2)):
            main(task, summoner_name)
        elif (task == 3):
            main(task, summoner_name)
        elif (task == 8):
            summoner_name = raw_input("Summoner Name: ")
        elif (task == 9):
            loopCount = 10
            loopVar = 0
        elif (loopCount == 9):
            print("Invalid command limit reached, quitting")
            loopVar = 1
            loopCount += 1
        else:
            loopVar = 1
            loopCount += 1
            print loopCount
            print("Invalid input, will time out after " + str(10-loopCount) + " more invalid cycles, Try again")
            print("")
            print("")


