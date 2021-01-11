from typing import List, Any, Tuple

from boxsdk import OAuth2
from boxsdk import Client
import pathtools
import os
# from boxsdk import DevelopmentClient
# from boxsdk import JWTAuth
# ebb: Try setting this up for JWT auth to use the Developer token https://github.com/box/box-python-sdk#server-to-server-auth-with-jwt
import requests
# import tarfile

from requests.models import Response

oauth = OAuth2(
    client_id='37zh1wo00w7h8qphpviwjkia7ng8g1j4',
    client_secret='YKatTFXOH1icNc9uxD3K2TMLCiulQJ0M',
    access_token='maRpVL9nUfUIAP6WZTmGQYoaYyK2XykO'
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
lettersOuterFolder = client.folder(folder_id='907769116').get()
# YearFolders = lettersOuterFolder/folders
for i in lettersOuterFolder.get_items():
    substring = "Folder"
    if substring in str(i):
        yearFid = i.id.split()
        for y in yearFid:
            yearFolder = client.folder(folder_id=y).get()
            if yearFolder.description:
                print(yearFolder.description)
            for a in yearFolder.get_items():
                substring = "Folder"
                if substring in str(a):
                    archiveFid = a.id.split()
                    for r in archiveFid:
                        archiveFolder = client.folder(folder_id=r).get()
                        if archiveFolder.description:
                            print(archiveFolder.description)
                        for letters in archiveFolder.get_items():
                            substring = "Folder"
                            if substring in str(letters):
                                lettersFid = letters.id.split()
                                for l in lettersFid:
                                    letterFolder = client.folder(folder_id=l).get()
                                    if letterFolder.description:
                                        print(letterFolder.description)






