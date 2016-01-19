import requests
import RiotConsts as Consts


class ChampIDName(object):
    id = 0
    name = "Empty"


def ChampIndex():
    Champ = {103:'Ahri',
             84:'Akali',
             12:'Alistar',
             32:'Amumu',
             34:'Anivia',
             1:'Annie',
             22:'Ashe',
             53:'Blitzcrank',
             63:'Brand',
             51:'Caitlyn',
             69:'Cassiopeia',
             31:'Cho\'Gath',
             42:'Corki',
             36:'Dr. Mundo',
             28:'Evelynn',
             81:'Ezreal',
             9:'Fiddlesticks',
             105:'Fizz',
             3:'Galio',
             41:'Gangplank',
             86:'Garen',
             79:'Gragas',
             104:'Graves',
             74:'Heimerdinger',
             39:'Irelia',
             40:'Janna',
             59:'Jarvan IV',
             24:'Jax',
             43:'Karma',
             30:'Karthus',
             38:'Kassadin',
             55:'Katarina',
             10:'Kayle',
             85:'Kennen',
             96:'Kog\'Maw',
             7:'LeBlanc',
             64:'Lee Sin',
             89:'Leona',
             99:'Lux',
             54:'Malphite',
             90:'Malzahar',
             57:'Maokai',
             11:'Master Yi',
             21:'Miss Fortune',
             82:'Mordekaiser',
             25:'Morgana',
             75:'Nasus',
             76:'Nidalee',
             56:'Nocturne',
             20:'Nunu',
             2:'Olaf',
             61:'Orianna',
             80:'Pantheon',
             78:'Poppy',
             33:'Rammus',
             58:'Renekton',
             92:'Riven',
             68:'Rumble',
             13:'Ryze',
             113:'Sejuani',
             35:'Shaco',
             98:'Shen',
             102:'Shyvana',
             27:'Singed',
             14:'Sion',
             15:'Sivir',
             72:'Skarner',
             37:'Sona',
             16:'Soraka',
             50:'Swain',
             91:'Talon',
             44:'Taric',
             17:'Teemo',
             18:'Tristana',
             48:'Trundle',
             23:'Tryndamere',
             4:'Twisted Fate',
             29:'Twitch',
             77:'Udyr',
             6:'Urgot',
             67:'Vayne',
             45:'Veigar',
             112:'Viktor',
             8:'Vladimir',
             106:'Volibear',
             19:'Warwick',
             62:'Wukong',
             101:'Xerath',
             5:'Xin Zhao',
             83:'Yorick',
             26:'Zilean',
             266 :'Aatrox',
             412 :'Thresh',
             111 :'Nautilus',
             127 :'Lissandra',
             238 :'Zed',
             117 :'Lulu',
             122 :'Darius',
             110 :'Varus',
             126 :'Jayce',
             134 :'Syndra',
             121 :'Kha\'Zix',
             268 :'Azir',
             432 :'Bard',
             150 :'Gnar',
             104 :'Graves',
             254 :'Vi',
             60 :'Elise',
             420 :'Illaoi',
             429 :'Kalista',
             223 :'Tahm Kench',
             131 :'Diana',
             154 :'Zac',
             421 :'Rek\'Sai',
             133 :'Quinn',
             120 :'Hecarim',
             236 :'Lucian',
             107 :'Rengar',
             157 :'Yasuo',
             119 :'Draven',
             115 :'Ziggs',
             245 :'Ekko',
             222 :'Jinx',
             203 :'Kindred',
             201 :'Braum',
             161 :'Vel\'Koz',
             267 :'Nami',
             143 :'Zyra',
             114 :'Fiora',

             }

    return Champ

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


class RiotAPICall(object):
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
