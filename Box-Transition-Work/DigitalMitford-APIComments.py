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
    foldername = getFolder.name
    foldernamecorr = foldername.replace('?', '')
    folderid = getFolder.id
    for i in getFolder.get_items():
        # print(str(i.type))
        if "file" in str(i.type):
            itemname = i.name
            itemnamecorr = itemname.replace('?', '')
            itemid = i.id
            commentfilename = "comments_F_" + foldernamecorr + "_" + itemnamecorr + "-" + itemid + ".txt"
            pathway = os.path.join(projectPath, commentfilename)
            commentList = []
            for c in i.get_comments():
                    content = 'Comment was left by {0} at {1}: {2}'.format(c.created_by.name, c.created_at, c.message)
                    print(content)
                    commentList.append(content)
            commentListWhole = '\n'.join(commentList)
            if len(commentListWhole) > 0:
                print(str(commentListWhole))
            # if len(str(commentList)) > 0:
            #    separator = '\n'
            #    commentFileContents = separator.join(commentList)
            #    commentfile = open(pathway, 'w', encoding='utf-8')
            #    commentfile.write(commentFileContents)
            #    commentfile.close()
            #    commentfileupload = client.folder(folderid).upload(pathway)
            #   print('File "{0}" uploaded to Box with file ID {1}'.format(commentfileupload.name, commentfileupload.id))
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
    access_token='2w9yInFbPEbA5Vh41qqoNRgrw38Ry5FG'
    # store_tokens=your_store_tokens_callback_method,
)

auth_url, csrf_token = oauth.get_authorization_url('https://psu.app.box.com/folder/0')

# Redirect user to auth_url, where they will enter their Box credentials

response = requests.get("https://account.box.com/api/oauth2/authorize/")
# print(response.status_code)
client = Client(oauth)
# client: object = requests.get("https://api.box.com/2.0/folders/:9dj7qs0aimiaywmxm2mo/").folder.get()
# Mitford_Digital_Archives folder = client.folder(folder_id='907565446').get()
sampleFile = client.file(file_id='33034276995')
comments = sampleFile.get_comments()
type = sampleFile.get().type
print(str(comments))
print(str(type))
for comment in comments:
    print(str(comment))
    print('Comment was left by {0} at {1}: {2}'.format(comment.created_by.name, comment.created_at, comment.message))

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