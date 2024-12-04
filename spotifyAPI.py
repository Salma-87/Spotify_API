 first, we import all the libraries that will be utilized 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import time 
import warnings

# authenticate and connect to spotify's API 
#these ids can be found when checking the setting of the application created in spotify developer
client_id = '***********' 
client_secret_id = '*************'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret_id)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# creating function to get playlist 
def TrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

#ids = TrackIDs('oluprecious1', '4MRgvByeNtyl2LcUjDpbE1')

#The track_id can be found in the url of the playlist after the / and before ?
#For the username, we can get it accessing the URL by clicking on your profile same part as track_id

ids = TrackIDs('31m56q64ugposrnkqbtsta6gdz3a', '4MRgvByeNtyl2LcUjDpbE1')
#ids = TrackIDs('oluprecious1', '5HzAzXZzIlzFpgBG9q0y11')

#now want to check the length of the playlist. My playlist has 37 tracks. 
print(len(ids))
print(ids)


def TrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    # metadata
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # specific feartures 
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track
# loop over each track Ids 
tracks = []
for i in range(len(ids)):
    time.sleep(.5)
    track = TrackFeatures(ids[i])
    tracks.append(track)

# wrap dataset in dataframe
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("spotifyafrotest8.csv", sep = ',')

# convert dataframe to csv named spotifyafro and export to desktop 
df.to_csv('/Users/alexparsee/Desktop/LEAD BRG Nov 22nd 2024/spotifyafrotest8.csv', sep = ',' )    

#read extracted data
#################################
# afrobeats_data = pd.read_csv("spotifyafroSaliTest.csv")



# afrobeats_data.head(5)



# #Outliers Check

# afrobeats_data.describe()



# #DROP UNANMED COLUMN

# afrobeats_data.drop('Unnamed: 0', axis=1, inplace=True)



# #MOST DANCEABLE SONG IN THE Playlist

# afrobeats_data[afrobeats_data.danceability == np.max(afrobeats_data.danceability)]



# #TOP 5 danceable songs



# afrobeats_data.nlargest(5, ['danceability']) 


# #MOST ENERGETIC SONG

# afrobeats_data[afrobeats_data.energy == np.max(afrobeats_data.energy)]

# #TOP 5 ENERGETIC SONGS

# afrobeats_data.nlargest(5, ['energy']) 

    

# # with most danceable songs

# top_danceability = afrobeats_data[['name','danceability']].sort_values('danceability', ascending=False)[0:10]





# plt.figure(figsize=(10,5))

# chart = sns.barplot('name','danceability', data=top_danceability,palette ='rocket')

# chart.set_xticklabels(chart.get_xticklabels(), rotation = 45)

# chart.set(xlabel = 'track', ylabel = 'danceablility')

# chart.set_title('Top 10 danceable songs')

    

# # CORRELATION BETWEEN LOUDNESS AND DANCEABILITY

# sns.jointplot(x='loudness',y='danceability', data=afrobeats_data[['loudness', 'danceability']],kind = 'hex').set_axis_labels("loudness","danceability")



# #Most Energetic Artist

# energetic_artist = afrobeats_data[['artist','energy']].sort_values('energy', ascending=False)[0:20]

# plt.figure(figsize=(10,5))

# chart = sns.countplot(y='artist', data=energetic_artist)

# chart.set_title('ENERGY')
