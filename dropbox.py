'''
The script to upload files and directories to dropbox
Author: Jinhua Wang
'''

import requests
import json

'''
Access token for dropbox
'''
token=raw_input("Please enter your access token for dropbox: \n")


dropboxarg={'path':'/Asset/execute.py',"mode":"add", "autorename":True, "mute":False}
print json.dumps(dropboxarg)
auth_headers={'Authorization':'Bearer '+token, "Dropbox-API-Arg":json.dumps(dropboxarg), "Content-Type":"application/octet-stream"}
data=open('./execute.py','rb').read()
res=requests.post(url='https://content.dropboxapi.com/2/files/upload', data=data, headers=auth_headers)
print res.text
