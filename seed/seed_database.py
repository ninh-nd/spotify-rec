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

# Remove any element in results with no audio features
results = [x for x in results if x is not None]

print("Getting genre for each song from API...")
for i in range(0, len(results), 50):
    # Get the artists in a batch of 50
    first_50_results = results[i:i+50]
    song_ids = [result['id'] for result in first_50_results]
    # Get the first artist for 50 songs
    tracks_info = sp.tracks(song_ids)['tracks']
    artists = [track['artists'][0]['id'] for track in tracks_info]
    artists = sp.artists(artists)['artists']
    for j in range(0, len(artists)):
        results[i+j]['genres'] = artists[j]['genres']

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