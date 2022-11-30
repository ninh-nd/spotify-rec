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

# Bring back genres from the csv file to the results
for i in range(0, len(results)):
    results[i]['genres'] = df['genres'][i]


# Remove any element in results with no audio features
results = [x for x in results if x is not None]

print("Saving audio features to csv file...")
# Save the results into a csv file
with open('song_features.csv', 'w') as f:
    csv_writer = csv.writer(f)
    features = ['id', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence', 'genres']
    csv_writer.writerow(features)
    for i in range(0, len(results)):
        csv_writer.writerow([results[i][feature] for feature in features])
    f.close()

print("Finish saving audio features to csv file.")