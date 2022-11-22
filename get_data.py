import os
import time
import json
import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from csv import writer
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
NUMBER_OF_THREADS = 10
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
start_year = int(sys.argv[1])
end_year = int(sys.argv[2])
def get_data(year, results, start, end):
    query_string = "year:" + str(year)
    for i in range(start, end, 50):
        first_result = sp.search(q=query_string, type='track', limit=50, offset=i)['tracks']['items']
        for j in range(0, 50):
            second_result = first_result[j]['id']
            results.append(second_result)
results = []
for i in range(start_year, end_year):
    get_data(i, results, 0, 500)
    time.sleep(2) # Avoid rate limiting
    get_data(i, results, 500, 1000)
# Save the results into a csv file
with open('song_id.csv', 'w') as f:
    csv_writer = writer(f)
    csv_writer.writerow(results)
    f.close()
print(len(results))
# print(json.dumps(results, indent=4))
# print(json.dumps(playlist_id, indent=4))
# result = sp.search(q='year:2010', type='track', limit=2, offset=1)['tracks']['items']
# print(json.dumps(result, indent=4))
# print(get_data(2019, results, 1000, 1500))