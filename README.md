# Project: Spotify Recommendation System

## Pre-requisites
1. Python 3
2. (Optional) Virtualenv
## Installation
1. Clone the repository
2. (Optional) Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Create an .env file followed the example in .env_example (Login to https://developer.spotify.com/ to get the information needed)
## Usage
### To seed the database
1. Run `python seed/get_data.py`. This will generate a list of songs ids with its genre to `song_id.csv`
2. Run `python seed/seed_database.py`. This will seed `song_features.csv` with the songs and their features
