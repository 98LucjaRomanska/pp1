class Playlist():
 def __init__(self, artist, track_title, album, year):
    self.artist = artist
    self.track_title = track_title
    self.album = album
    self.year= year
 def __str__(self):
    return f'Performer:\t{self.artist}\nSong:\t\t{self.track_title}\nAlbum: \t\t{self.album}\nYear: \t\t{self.year}'


song = Playlist('Lana Del Rey','Trauma is offended','Steal this album','1997')
print(song)