import requests
import RiotConsts as Consts

class GameData(object):
    append = 1
    gameId = "0"
    championId = "0"
    sumlevel = "0"
    createDate = "0"
    gameMode = "0"
    mapId = "0"
    gameType = "0"
    subType = "0"
    teamId = "0"
    invalid = "0"
    ipEarned = "0"
    fellowPlayers = "0"
    spell1 = "0"
    spell2 = "0"
    championsKilled = "0"
    win = "0"
    wardPlaced = "0"
    totalDamageDealt = "0"
    magicDamageDealtToChampions = "0"
    playerPosition = "0"
    largestMultiKill = "0"
    largestKillingSpree = "0"
    magicDamageTaken = "0"
    totalTimeCrowdControlDealt = "0"
    wardKilled = "0"
    item2 = "0"
    item3 = "0"
    item0 = "0"
    item1 = "0"
    item5 = "0"
    item6 = "0"
    item4 = "0"
    minionsKilled = "0"
    visionWardsBought = "0"
    timePlayed = "0"
    assists = "0"
    playerRole = "0"
    physicalDamageDealtToChampions = "0"
    goldSpent = "0"
    champlevel = "0"
    physicalDamageDealtPlayer = "0"
    totalHeal = "0"
    goldEarned = "0"
    totalDamageDealtToChampions = "0"
    totalUnitsHealed = "0"
    team = "0"
    numDeaths = "0"
    totalDamageTaken = "0"
    killingSprees = "0"
    magicDamageDealtPlayer = "0"
    physicalDamageTaken = "0"
    def __int__(self):
        self.append = 1
        self.gameId = "0"
        self.championId = "0"
        self.sumlevel = "0"
        self.createDate = "0"
        self.gameMode = "0"
        self.mapId = "0"
        self.gameType = "0"
        self.subType = "0"
        self.teamId = "0"
        self.invalid = "0"
        self.ipEarned = "0"
        self.fellowPlayers = "0"
        self.spell1 = "0"
        self.spell2 = "0"
        self.championsKilled = "0"
        self.win = "0"
        self.wardPlaced = "0"
        self.totalDamageDealt = "0"
        self.magicDamageDealtToChampions = "0"
        self.playerPosition = "0"
        self.largestMultiKill = "0"
        self.largestKillingSpree = "0"
        self.magicDamageTaken = "0"
        self.totalTimeCrowdControlDealt = "0"
        self.wardKilled = "0"
        self.item2 = "0"
        self.item3 = "0"
        self.item0 = "0"
        self.item1 = "0"
        self.item5 = "0"
        self.item6 = "0"
        self.item4 = "0"
        self.minionsKilled = "0"
        self.visionWardsBought = "0"
        self.timePlayed = "0"
        self.assists = "0"
        self.playerRole = "0"
        self.physicalDamageDealtToChampions = "0"
        self.goldSpent = "0"
        self.champlevel = "0"
        self.physicalDamageDealtPlayer = "0"
        self.totalHeal = "0"
        self.goldEarned = "0"
        self.totalDamageDealtToChampions = "0"
        self.totalUnitsHealed = "0"
        self.team = "0"
        self.numDeaths = "0"
        self.totalDamageTaken = "0"
        self.killingSprees = "0"
        self.magicDamageDealtPlayer = "0"
        self.physicalDamageTaken = "0"

class RiotAPI(object):
    api_key = ""
    region = ""

    def __int__(self, api_key, region='na'):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
            ),
            params=args
        )
        print (response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)


    def games_by_summoner(self, id):
        api_url = Consts.URL['game'].format(
            version=Consts.API_VERSIONS['game'],
            summonerId=id
        )
        return self._request(api_url)