# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:05:55 2016

@author: clayfinney
"""

# Script to construct database of SC2 players' total games played
# Called via main.py


# Blizzard URI-specific things
matches = 'matches'

apikey = '#############################'

locale = {'US':'?locale=en_US',
          'KR':'?locale=ko_KR',
          'EU':'?locale=us_EN'}

import csv
import json
import urllib
import dropbox
import time


player_lists = []
error_list = []
previous = []
current = []

dropbox_key = '#####################'
dropbox_secret = '##################'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(dropbox_key, dropbox_secret)
flow.start()
access_token = '#########################################'
client = dropbox.client.DropboxClient(access_token)


def read_from_dropbox():
    
    response = client.get_file('/rtstime.txt')    
    for row in response:
        global start_time
        start_time = int(row)

def get_links():
    with open('sc2db.csv', 'r') as r:
        reader = csv.reader(r)
        next(reader)
        for row in reader:
            player_lists.append(row)
            
  
def make_links(): # join the api key, links, then send them to get data retrieved
    for sublist in player_lists:
        player = sublist[1]
        global region
        region = sublist[2]
        link = sublist[3]
        if 'NA' in region:          
            uri = link + matches + locale['US'] + apikey
            collect_current_scores(player, region, uri)
            previous.append(int(sublist[4]))
        elif 'EU' in region:
            uri = link + matches + locale['EU'] + apikey
            collect_current_scores(player, region, uri)
            previous.append(int(sublist[5]))
        elif 'KR' in region:
            uri = link + matches + locale['KR'] + apikey
            collect_current_scores(player, region, uri)
            previous.append(int(sublist[6]))
        else:
            pass

def collect_current_scores(player_name, account_region, link):       
    try:
        count = 0
        urllib.urlopen(link).read()
        final = json.loads(urllib.urlopen(link).read())
        number_of_games = final['matches']
        for games in number_of_games:
            if games['date'] > start_time and games['type'] == "SOLO":            
                count += 1   
        
        current.append(count)

    except:
        error_list.append([player_name, account_region])
        current.append(0)


def compare():        
    new = [x + y for x, y in zip(current, previous)]
    for i, sublist in enumerate(player_lists):
        if 'NA' in region:
            sublist[4] = new[i]
            sublist[7] = new[i]
        elif 'EU' in region:
            sublist[5] = new[i]
            sublist[7] = new[i]
        elif 'KR' in region:
            sublist[6] = new[i]
            sublist[7] = new[i]

def write_to_csv():
    with open('sc2db.csv', 'wb') as w:
        fieldnames = ['team_id', 'name', 'region', 'link', 'na_server', 'eu_server', 'kr_server', 'total']
        header = csv.DictWriter(w, fieldnames = fieldnames)
        header.writeheader()
        
    with open('sc2db.csv', 'ab') as r:
        writer = csv.writer(r)
        for sublist in player_lists:
            writer.writerow(sublist)
   
def run():
    read_from_dropbox()
    get_links()
    make_links()
    compare()
    write_to_csv()


