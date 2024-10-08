# from typing import List, Any, Tuple
# import tarfile
from typing import Any

from boxsdk import OAuth2
from boxsdk import Client
from pathlib import Path
import os
from os import mkdir
# Not using the libraries below. Authenticate using the developer token which needs to be updated hourly.
# from boxsdk import DevelopmentClient
# from boxsdk import JWTAuth
# ebb: Try setting this up for JWT auth to use the Developer token https://github.com/box/box-python-sdk#server-to-server-auth-with-jwt
import requests

projectPath = Path('E:/Users/Lisa Documents/Documents/GitHub/Digital-Mitford-Organization/DM_documentation/Box-Transition-Work')

def recurfolders(getFolder):
    # ebb: What if instead we filed the description files inside the actual downloaded Box directories that share the same name as the folder.name?
    # Would we need os.walk for this?
    # Maybe easiest to post the descriptions as files to Box, and let them sync locally.
    # See https://github.com/box/box-python-sdk/blob/master/docs/usage/files.md#upload-a-file
    if getFolder.description:
        foldername = getFolder.name
        foldernamecorr = foldername.replace('?', '')
        folderid = getFolder.id
        labelcontents = getFolder.description
        labelfilename = foldernamecorr + '----' + folderid + ".txt"
        newPath = os.path.join(projectPath, labelfilename)
        labelFile = open(newPath, 'w', encoding='utf-8')
        labelFile.write(labelcontents)
        labelFile.close()
        labelfileupload = client.folder(folderid).upload(newPath)
        print('File "{0}" uploaded to Box with file ID {1}'.format(labelfileupload.name, labelfileupload.id))
    for i in getFolder.get_items():
        substring = "Folder"
        if substring in str(i):
            innerids = i.id.split()
            for n in innerids:
                innerFolder = client.folder(folder_id=n).get()
                # print(innerFolder.id)
                # print(innerFolder.description)
                # if innerFolder.item_collection["total_count"] > 1:
                recurfolders(innerFolder)


oauth = OAuth2(
    client_id='37zh1wo00w7h8qphpviwjkia7ng8g1j4',
    client_secret='YKatTFXOH1icNc9uxD3K2TMLCiulQJ0M',
    access_token='AzoJ2PXouN7iOS3Sk0kkIf6GuovPtXn0'
    # store_tokens=your_store_tokens_callback_method,
)

auth_url, csrf_token = oauth.get_authorization_url('https://psu.app.box.com/folder/0')

# Redirect user to auth_url, where they will enter their Box credentials

response = requests.get("https://account.box.com/api/oauth2/authorize/")
# print(response.status_code)
client = Client(oauth)
# client: object = requests.get("https://api.box.com/2.0/folders/:9dj7qs0aimiaywmxm2mo/").folder.get()
# Mitford_Digital_Archives folder = client.folder(folder_id='907565446').get()
sampleFolder = client.folder(folder_id='907771552')
folder = sampleFolder.get()
print('Folder "{0}" with id {1} has {2} items in it'.format(
    folder.name,
    folder.id,
    folder.item_collection['total_count'],
))
folder_metadata = sampleFolder.get_all_metadata()
print('Folder "{0}" has this metadata: "{1}" and this description: "{2}".'.format(
    folder.name,
    folder.metadata,
    folder.description
))
MitfordDigitalArchives = client.folder(folder_id='907565446').get()
lettersOuterFolder = client.folder(folder_id='907769116').get()
testingOuterFolder = client.folder(folder_id='132569588068').get()
recurfolders(MitfordDigitalArchives)