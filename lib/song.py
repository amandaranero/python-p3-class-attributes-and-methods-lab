class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_artists(artist)
        self.add_genres(genre)
        self.count_genres(genre)
        self.count_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_artists(cls, artist):
        cls.artists.append(artist)

    def add_genres(cls,genre):
        cls.genres.append(genre)

    @classmethod
    def count_genres(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def count_artists(cls,artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else: 
            cls.artist_count[artist] = 1
    



    

        
    


