#!/usr/bin/python
import plistlib
import urllib2
import os

# Man, I don't want to hardcode these, but getting them programmatically is terrible
def musicLibraryLocation():
	return '/Users/reilly/Music/iTunes/'
def musicLocation():
	return '/Users/reilly/Music/iTunes/iTunes Media/Music/'

l = plistlib.readPlist(musicLibraryLocation() + 'iTunes Music Library.xml')
tracks = l['Tracks']
locations = []
for trackid in tracks:
	if 'Location' in tracks[trackid]:
		location = urllib2.unquote(tracks[trackid]['Location']).replace('file://localhost', '')
		locations.append(location)

files = []
for root, dirnames, filenames in os.walk(musicLocation()):
	for f in filenames:
		if f.endswith('.mp3'):
			files.append(os.path.join(root, f))

for f in files:
	if f not in locations:
		os.remove(f)
