class Song:
    def __init__(self, trackid, songid, artistnamn, songnamn):
        self.trackid = trackid
        self.songid = songid
        self.artistnamn = artistnamn
        self.songnamn = songnamn

    def __lt__(self, other):
        if self.songnamn < other.songnamn:
            return True
        else:
            return False
def text():
        lista = []
        with open("unique_tracks.txt", "r", encoding="utf-8") as songfil:
            for rad in songfil:
                raden = rad.strip()
                raden = raden.split("<SEP>")
                lista.append(Song(raden[0],raden[1],raden[2],raden[3]))
            return lista

def readfile(filename):
    # En tom lista där all objekt skall samlas i
    songList = []

    # Filen öppnas i läsläge
    file = open(filename, "r", encoding="utf8")

    # Varje rad i filen separeras och sparas som ett objekt i songList
    for row in file:
        row = row.split("<SEP>")
        track = Song(row[0], row[1], row[2], row[3])
        songList.append(track)

    file.close()

    # Listan med alla objekt returneras
    return songList