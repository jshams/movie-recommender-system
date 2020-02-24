class Movies:
    def __init__(self):
        '''initialize a movies class with a dict to store the movies by id'''
        self.movies = {}

    def get_title(self, movie_id):
        '''given a movie_id return the title associated with it'''
        if movie_id not in self.movies:
            return None
        return self.movies[movie_id]

    def add_movie(self, movie_id, title):
        '''add a movie to movies dictionary. key=movie_id, val=title'''
        if movie_id not in self.movies:
            self.movies[movie_id] = title
