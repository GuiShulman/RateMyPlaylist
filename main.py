from unittest import result
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st

st.title('Rate My Playlist')
st.text("Gur Shulman | Jan 2020")

scope = 'user-library-read'
client_id = 'b12376dca6fb46fba8e1dbc9c9099f91'
client_secret = '34caa83bbc17441595140b2f35467e08'
redirect_uri = 'http://localhost:8000'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

playlists = sp.current_user_playlists()
saved = sp.current_user_saved_tracks()

source_optioins = []

saved_title = 'Your Liked Songs      |      ' + str(saved['total']) + ' tracks'
source_optioins.append(saved_title)

for playlist in playlists['items']:
    playlist_title = str(playlist['name']) + '    |     ' + str(playlist['tracks']['total']) + ' tracks'
    source_optioins.append(playlist_title)
    
selected_source = st.selectbox('Choose a playlist:', source_optioins, )

if st.button("Let's Go!"):
    if selected_source == source_optioins[0]:
        tracks = saved['items']
        st.text(tracks)
    else:
        tracks = playlists['items'][source_optioins.index(selected_source) - 1]
        st.text(tracks)


