import os
import sys
import random
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

# NUMBER_OF_SAMPLE_GENRE = int(sys.argv[1])
# Global variable to store the results
results = []
list_of_genres = sp.recommendation_genre_seeds()['genres']

def get_data(start, end, genres_array):
    for selected_genre in genres_array:
        for i in range(start, end, 50):
            query_string = "genre: " + selected_genre
            first_result = sp.search(q=query_string, type='track', limit=50, offset=i)['tracks']['items']
            for j in range(0, len(first_result)):
                song_id = first_result[j]['id']
                list = [song_id, selected_genre]
                results.append(list)
        print("Finish getting data for genre: " + selected_genre)

def seed():
    genres_array = ["a-cappella", "afrobeat", "blues", "classical", "disco",  
                    "electronic", "eurobeat", "folk", "funk", "hip-hop", 
                    "idol", "jazz", "latin", "opera", "poetry", 
                    "pop", "rock", "soul", "soundtrack", "tango"]
    get_data(0, 500, genres_array)
    get_data(500, 1000, genres_array)
    # Save the results into a csv file
    with open('song_id.csv', 'w') as f:
        csv_writer = writer(f)
        csv_writer.writerow(['id', 'genres'])
        for i in range(0, len(results)):
            csv_writer.writerow(results[i])
        f.close()
    print("Number of songs obtained: " + str(len(results)))

seed()
