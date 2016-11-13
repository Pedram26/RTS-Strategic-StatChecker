import requests
import time
import csv
import dropbox

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()

"""def requestRankedData(region, sid, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + sid + "/entry?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()"""

def requestMatchlistData(region, sid, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.2/matchlist/by-summoner/" + sid + "?rankedQueues=" + "RANKED_FLEX_SR" + "&seasons=" + "SEASON2016" + "&api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

APIKey = _____

def read_from_dropbox():
    dropbox_key = _____
    dropbox_secret = _____
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(dropbox_key, dropbox_secret)
    flow.start()
    access_token = _____
    client = dropbox.client.DropboxClient(access_token)
    response = client.get_file('/rtstime.txt')
    for line in response:
        global start_time
        start_time = int(line)

def main():
    team, name, role, region, sid, ign, na_games, eu_games, kr_games, total_games = [], [], [], [], [], [], [], [], [], []
    with open('player_dict.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        next(reader)
        for row in reader:
            team.append(row[0])
            name.append(row[1])
            role.append(row[2])
            region.append(row[3])
            sid.append(row[4])
            ign.append(row[5])
            na_games.append(row[6])
            eu_games.append(row[7])
            kr_games.append(row[8])
            total_games.append(int(row[9]))

    with open('player_dict.csv', 'w', newline='') as csvfile:
        fieldnames = ['team', 'name', 'role', 'region', 'sid', 'ign', 'na_games', 'eu_games', 'kr_games', 'total_games']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for i in range(len(team)):
            responseJSON3 = requestMatchlistData(region[i], sid[i], APIKey)
            try:
                for match in responseJSON3['matches']:
                    if match['timestamp']//1000 > start_time:
                        total_games[i] += 1
                    else:
                        break
            except:
                time.sleep(2)
                print("Error")
            if "NA" is region[i]:
                na_games[i] = total_games[i]
            elif "EUW" is region[i] or "EUNE" is region[i]:
                eu_games[i] = total_games[i]
            elif "KR" is region[i]:
                kr_games[i] = total_games[i]
            print(ign[i], total_games[i])
            writer.writerow({'team': team[i], 'name': name[i], 'role': role[i],
                             'region': region[i], 'sid': sid[i],
                             'ign': ign[i], 'na_games': na_games[i],
                             'eu_games': eu_games[i], 'kr_games': kr_games[i],
                             'total_games': total_games[i]})
            time.sleep(2)

def add_player(team, name, region, ign):
    ign = ign.lower()
    sid = str(requestSummonerData(region, ign, APIKey)[ign]['id'])
    with open('player_dict.csv', 'a', newline='') as csvfile:
        fieldnames = ['team', 'name', 'role', 'region', 'sid', 'ign', 'na_games', 'eu_games', 'kr_games', 'total_games']
        writer = csv.DictWriter(csvfile, fieldnames)
        responseJSON3 = requestMatchlistData(region, sid, APIKey)
        na_games, eu_games, kr_games, total_games = 0, 0, 0, 0
        try:
            for match in responseJSON3['matches']:
                if match['timestamp']//1000 > 1470000000:
                    total_games += 1
                else:
                    break
        except:
            time.sleep(5)
            print(ign, responseJSON3, total_games)
        if "NA" is region:
            na_games = total_games
        elif "EUW" is region or "EUNE" is region:
            eu_games = total_games
        elif "KR" is region:
            kr_games = total_games
        writer.writerow({'team': team, 'name': name, 'role': role,
                         'region': region, 'sid': sid,
                         'ign': ign, 'na_games': na_games,
                         'eu_games': eu_games, 'kr_games': kr_games,
                         'total_games': total_games})
read_from_dropbox()

#if __name__ == "__main__":
#    main()
