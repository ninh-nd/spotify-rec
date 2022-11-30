# Project: Spotify Recommendation System

## Pre-requisites
1. Python 3
2. (Optional) Virtualenv
## Installation
1. Clone the repository
2. (Optional) Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
## Usage
### To seed the database
1. Run `python seed/get_data.py <start-year> <end-year>`. This will generate a list of songs ids to `song_id.csv` with each year has 1000 songs
2. Run `python seed/seed_database.py`. This will seed `song_features.csv` with the songs and their features
