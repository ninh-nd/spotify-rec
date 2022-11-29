import os
import json
import spotipy
import pandas as pd
import csv
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
# Initialize the Spotify API
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load data from csv file
df = pd.read_csv("song_id.csv")
# Create a list of song ids
song_ids = df['id'].tolist()
results = []

print("Getting audio features from API...")
for i in range(0, len(song_ids), 100):
    # Get the audio features in a batch of 100
    audio_features = sp.audio_features(song_ids[i:i+100])
    results += audio_features

print("Saving audio features to csv file...")
# Save the results into a csv file
with open('song_features.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['id', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence'])
    
    for i in range(0, len(results)):
        if (results[i] is not None): # Some songs may not have audio features
            csv_writer.writerow([results[i]['id'], results[i]['acousticness'], results[i]['danceability'], results[i]['energy'], results[i]['instrumentalness'], results[i]['key'], results[i]['liveness'], results[i]['loudness'], results[i]['mode'], results[i]['speechiness'], results[i]['tempo'], results[i]['time_signature'], results[i]['valence']])
    
    f.close()

print("Finish saving audio features to csv file.")