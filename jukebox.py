import requests
import json
import sys
import test106 as test


print ""

class Music:
	def __init__(self, Artist, Song, Album, Number, Cost):
		self.Artist = Artist
		self.Song = Song
		self.Album = Album
		self.Number = Number
		self.Cost = Cost

	def getArtist(self):
		return self.Artist

	def getSong(self):
		return self.Song

	def getAlbum(self):
		return self.Album

	def getNumber(self):
		return self.Number

	def getCost(self):
		return self.Cost

example = Music('Drake', 'Jumpman', 'What a Time To Be Alive', '9', '9.99')
test.testEqual(example.getArtist(), 'Drake')
test.testEqual(example.getSong(), 'Jumpman')
test.testEqual(example.getAlbum(), 'What a Time To Be Alive')
test.testEqual(example.getNumber(), '9')
test.testEqual(example.getCost(), '9.99')


stars = "**********"
star_list = []
for char in stars:
	star_list.append(char)
star_line = reduce(lambda first, second: first + "*" + second, star_list)

print ""
print ""
print star_line
print " Top Music Artists"
print star_line
print ""

top_artists = {'Kanye West':'5K4W6rqBFWDnAN6FQUkS6x', 'Rihanna':'5pKCCKE2ajJHZ9KAiaK11H', 'Justin Bieber':'1uNFoZAHBGtllmzznpCI3s','Coldplay':'4gzpq5DPGxSnKTe4SA8HAU',
				'Adele':'4dpARuHxo51G3z768sgnrY','Drake':'3TVXtAsR1Inumwj472S9r4','The Beatles':'3WrFJ7ztbogyGnTHbHJFl2','Skrillex':'5he5w2lnU9x7JFhnwcekXX',
				'Elvis Presley':'43ZHCT0cAZBISjO8DG9PnE','The Weeknd':'1Xyo4u8uXC1ZmMpatF05PJ','Luke Bryan':'0BvkDsjIUla7X0k6CSWh1I','Rascal Flatts':'0a1gHP0HAqALbEyxaD5Ngn',
				'Avicii':'1vCWHaC5f2uS3yhpwWbIA6','Beyonce':'6vWDO969PvNqNYHIOW5v0m','Eminem':'7dGJo4pcD2V6oG8kP0tJRR','The Chainsmokers':'69GGBxA162lTqCwzJG5jLp',
				'Kendrick Lamar':'2YZyLoL8N0Wb9xBt1NhZWg','Tim McGraw':'6roFdX1y5BYSbp60OTJWMd','Katy Perry':'6jJ0s89eD6GaHleKKya26X','Elton John':'3PhoLpVuITZKcymswpck5b',
				'Nicki Minaj':'0hCNtLu0JehylgoiP8L4Gh','Bob Dylan':'74ASZWbe4lXaubB36ztrGX','Billy Joel':'6zFYqv1mOsgBRQbae3JJ9e', 'Bruce Springsteen':'3eqjTLE0HfPfh78zjh6TqT',
				'JAY Z':'3nFkdlSjzX9mRTtwJOzDYB'}

artist_names = top_artists.keys()
artist_names = sorted(artist_names, key = lambda x: x.upper())
for name in artist_names:
	print name

print ""
print star_line
print ""
print ""


def get_artist_name():
	user_choice = str(raw_input("Enter your favorite music artist from the list above (case sensitive),\nor type \"Quit\" to end program: "))
	print ""
	if user_choice == 'Quit':
		print "Not now? That's okay."
		print ""
		print ""
		sys.exit()
	else:
		while user_choice not in artist_names:
			print "The artist entered is not listed above. Please enter an artist from the above list."
			print "-----------------------------------------------------------------------------------"
			print ""
			print ""
			user_choice = str(raw_input("Enter your favorite music artist from the list above (case sensitive),\nor type \"Quit\" to end program: "))
			print ""
			if user_choice == 'Quit':
				print "Not now? That's okay."
				print ""
				print ""
				sys.exit()
	artist = top_artists[user_choice]
	return artist 

artist = get_artist_name()


client_id = 'ece1895218b04651a297e032ae75c0b5'
client_secret = 'adca10d5804444d7a3532245587b2325'

def get_top_song(baseurl = 'https://api.spotify.com/v1/artists/' + artist + '/top-tracks?country=US',
	api_key = client_id,
	secret_key = client_secret,
	format = 'json'):
	key = requests.get(baseurl)
	return key

find_song = get_top_song()
locate = json.loads(find_song.text)
top_track = locate['tracks'][0]['name']
link = str(locate['tracks'][0]['external_urls'])
link = link[15:-2]

print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print ""
print top_artists.keys()[top_artists.values().index(artist)] + "'s most popular song on Spotify is: " '"' + top_track + '"'
print "You can listen to " '"' + top_track + '"' " on Spotify at: " + link


def get_album_name(baseurl = 'https://itunes.apple.com/search?term=' + top_track + '&limit=100', params = {'format':'json'}):
	key2 = requests.get(baseurl)
	return key2

find_album = get_album_name()
locate2 = json.loads(find_album.text)
album = locate2['results'][0]['collectionName']


def get_track_number(baseurl = 'https://itunes.apple.com/search?term=' + top_track + '&limit=100', params = {'format':'json'}):
	key2 = requests.get(baseurl)
	return key2

find_track_number = get_track_number()
locate3 = json.loads(find_track_number.text)
track_number = locate3['results'][0]['trackNumber']


def get_price(baseurl = 'https://itunes.apple.com/search?term=' + top_track + '&limit=100', params = {'format':'json'}):
	key2 = requests.get(baseurl)
	return key2

find_price = get_price()
locate4 = json.loads(find_price.text)
price = locate4['results'][0]['collectionPrice']


print ""
print '"' + top_track + '"' + " is track number " + str(track_number) + " on the album: " + album
print "You can buy " + album + " on iTunes for $" + str(price)
print ""
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print ""
print ""