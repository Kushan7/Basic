# from pynput.mouse import Button,Controller
# mouse= Controller()
# import pyautogui
# import keyboard
# import os
# import json
# import spotipy
# import webbrowser
# def action():
#     mouse.position = (1347, 63)
#     mouse.click(Button.left, 1)
#     pyautogui.sleep(1)
#     keyboard.press_and_release("ctrl + c")
#     pyautogui.sleep(1)
#     keyboard.press_and_release("windows + 6")
#     pyautogui.sleep(1)
#     mouse.position = (917, 786)
#     pyautogui.sleep(1)
#     mouse.click(Button.left, 1)
#     pyautogui.sleep(1)
#     keyboard.press_and_release("ctrl + v")
# def spotify(search):
#
#     username = '5efbgp0j9xe5f4sfsrdt10c58'
#     clientID = '70d38730f709405cb201edc0bb3e0b45'
#     clientSecret = '4d1bd0c83da4406281a5d2c3e5815c28'
#     redirectURI = 'http://google.com/'
#     oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI)
#
#
#
#
#
#     token_dict = oauth_object.get_access_token()
#
#     if token_dict != "":
#         action()
#     token = token_dict['access_token']
#     spotifyObject = spotipy.Spotify(auth=token)
#     user = spotifyObject.current_user()
#     # To print the response in readable format.
#     x=json.dumps(user, sort_keys=True, indent=4)
#
#     searchQuery = search
#     # Search for the Song.
#     searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
#     # Get required data from JSON response.
#     tracks_dict = searchResults['tracks']
#     tracks_items = tracks_dict['items']
#     song = tracks_items[0]['external_urls']['spotify']
#     # Open the Song in Web Browser
#     webbrowser.open(song)
#     print('Song has been opened in your browser.')






