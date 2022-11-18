import os
import threading
import json
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
def get_data(year, results):
    query_string = "year:" + str(year)
    for i in range(0, 500, 50):
        first_result = sp.search(q=query_string, type='track', limit=50, offset=i)['tracks']['items']
        for j in range(0, 50):
            second_result = first_result[j]['id']
            results.append(second_result)
threads = [None] * NUMBER_OF_THREADS
results = []
for i in range(len(threads)):
    threads[i] = threading.Thread(target=get_data, args=(2000 + i, results))
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()
# Save the results into a csv file
with open('song_id.csv', 'a') as f:
    csv_writer = writer(f)
    csv_writer.writerow(results)
    f.close()
print(len(results))
# print(json.dumps(results, indent=4))
# print(json.dumps(playlist_id, indent=4))
# result = sp.search(q='year:2010', type='track', limit=2, offset=1)['tracks']['items']
# print(json.dumps(result, indent=4))