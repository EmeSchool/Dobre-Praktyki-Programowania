class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = int(movieId)
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = int(userId)
        self.movieId = int(movieId)
        self.rating = float(rating)
        self.timestamp = int(timestamp)

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = int(userId)
        self.movieId = int(movieId)
        self.tag = tag
        self.timestamp = int(timestamp)