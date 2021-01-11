from boxsdk import OAuth2
from boxsdk import Client
from boxsdk import DevelopmentClient
from boxsdk import JWTAuth
# ebb: Try setting this up for JWT auth to use the Developer token https://github.com/box/box-python-sdk#server-to-server-auth-with-jwt
import requests
# import tarfile

from requests.models import Response

oauth = OAuth2(
    client_id='37zh1wo00w7h8qphpviwjkia7ng8g1j4',
    client_secret='YKatTFXOH1icNc9uxD3K2TMLCiulQJ0M',
    access_token='EJpt0KSFVZdNe1WHfIFirVRgcyn4OnPH'
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
