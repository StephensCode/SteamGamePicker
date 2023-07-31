from steam.webapi import WebAPI
import random
inkey = input("Steam Web API Key: ")
api = WebAPI(key=inkey)

id = input("SteamID: ")
numberofgames = int(input("How many games? "))

allthestuff = api.IPlayerService.GetOwnedGames(steamid = id, include_appinfo=1, include_played_free_games=1, appids_filter=[], include_free_sub=0, language="en", include_extended_appinfo=1)

games_names = [game['name'] for game in allthestuff['response']['games']]
count = allthestuff['response']['game_count']
while numberofgames > 0:
    randomgame = random.randint(0, count-1)
    print(games_names[randomgame])
    numberofgames -= 1
