import os
import time
import spotipy
import spotipy.util as util
from pynput.keyboard import Key, Controller

keyboard = Controller()

def closeSpotify():
    os.system("taskkill /f /im .exe")
    time.sleep(0.25)


def openSpotify():
    os.system('spotify.exe')
    time.sleep(0.25)


def playSpotify():
    time.sleep(1.5)
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
    time.sleep(2.0)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)


def restartSpotify():
    closeSpotify()
    openSpotify()
    playSpotify()


spotifyUsername = <spotify username>
spotifyClientID = <spotify clientID>
spotifyClientSecret = <spotify Client Secret>
spotifyAccessScope = "user-read-currently-playing user-modify-playback-state"
spotifyRedirectURI = "https://google.com/"

def setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI):
    token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
    return spotipy.Spotify(auth=token)

def run():
    global spotifyObject

    try:
        trackInfo = spotifyObject.current_user_playing_track()

    except:
        print("Token Expired")
        spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret,
spotifyRedirectURI)
        trackInfo = spotifyObject.current_user_playing_track()

    try:
        if trackInfo['currently_playing_type'] == 'ad':
            restartSpotify()
    except TypeError:
        pass

    #print(trackInfo)

spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret,spotifyRedirectURI)

if __name__ == "__main__":
    while (True):
        run()  
        time.sleep(1)
