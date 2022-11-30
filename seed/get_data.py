import os
import time
import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from csv import writer
# Initialize the Spotify API
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get commandline input, including start year and end year
start_year = int(sys.argv[1])
end_year = int(sys.argv[2])

# Global variable to store the results
results = []

def get_data(year, results, start, end):
    query_string = "year:" + str(year)
    for i in range(start, end, 50):
        first_result = sp.search(q=query_string, type='track', limit=50, offset=i)['tracks']['items']
        for j in range(0, 50):
            song_id = first_result[j]['id']
            artist_id = first_result[j]['artists'][0]['id']
            list = [song_id, artist_id]
            results.append(list)

def seed(start_year, end_year):
    for i in range(start_year, end_year + 1):
        print("Currently getting 1000 songs from year " + str(i))
        get_data(i, results, 0, 500)
        get_data(i, results, 500, 1000)
        print("Finished getting 1000 songs from year " + str(i))
    # Save the results into a csv file
    with open('song_id.csv', 'w') as f:
        csv_writer = writer(f)
        csv_writer.writerow(['id', 'artist_id'])
        for i in range(0, len(results)):
            csv_writer.writerow(results[i])
        f.close()
    print("Number of songs obtained: " + str(len(results)))

seed(start_year, end_year)
