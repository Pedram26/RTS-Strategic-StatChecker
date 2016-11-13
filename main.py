# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:42:21 2016

@author: clayfinney
"""

import dropbox
import sc2script
import lolscript
import time

running = True

dropbox_key = '#####################'
dropbox_secret = '##################'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(dropbox_key, dropbox_secret)
flow.start()
access_token = '#####################################################'
client = dropbox.client.DropboxClient(access_token)

def main():
    lolscript.run()    
    sc2script.run()
    write_time_to_dropbox()

def write_time_to_dropbox():
    client = dropbox.client.DropboxClient(access_token)
    f = str(int(time.time()))
    response = client.put_file('/rtstime.txt', f, overwrite = True)    
    
    
if __name__ == '__main__':
    main()
    