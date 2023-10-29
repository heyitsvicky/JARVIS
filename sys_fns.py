import os
import subprocess as sp

paths = {
    'notes': "/System/Applications/Notes.app/Contents/MacOS/Notes",
    'discord': "/Applications/Discord.app/Contents/MacOS/Discord",
    'spotify': "/Applications/Spotify.app/Contents/MacOS/Spotify",
    'minecraft': "/Applications/Lunar Client.app/Contents/MacOS/Lunar Client"
}

def open_notes():
    os.system(paths['notes'])

def open_discord():
    os.system(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_spotify():
    os.system(paths['spotify'])

def open_minecraft():
    os.system(paths['minecraft'])