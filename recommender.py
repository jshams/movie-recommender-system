from heapq import heappop, heappush


class Recommender:
    def __init__(self):
        '''initialize a reccomender model with users=None'''
        self.users = None

    def fit(self, users, movies):
        '''fit the reccomender model with a users object, and a movies obj'''
        self.users = users
        self.movies = movies

    def get_nearest_neighbors(self, new_user):
        '''calls users knn method
        returns a list of tuples (similarity, user obj)'''
        if self.users is None:
            return None
        return self.users.k_nearest_neighbors(new_user)

    def get_new_recs(self, new_user, nearest_neighbors):
        '''returns a set of new movie ids that neighbors have seen that
        new user has not'''
        new_recs = set()
        for neighbor in nearest_neighbors:
            for movie_id in neighbor.movie_ratings:
                if movie_id not in new_user.movie_ratings:
                    if movie_id not in new_recs:
                        new_recs.add(movie_id)
        return new_recs

    def predict_movie_score(self, new_user, nearest_neighbors, movie_id):
        '''given a new users, its nearest_neighbors, and a movie, predict
        the score new_user would give it based on its neighbors'''
        # create a score (float) variable = 0
        score = 0
        # create a similarities_sum (float) variable = 0
        sim_sum = 0
        # For each neighbor that has seen that movie
        for neighbor, sim in nearest_neighbors.items():
            if movie_id in neighbor.movie_ratings:
                # add the neighbor's similarity * their score for the movie
                score += sim * neighbor.get_movie_rating(movie_id)
                sim_sum += sim
        # divide the score by similarities_sum and return it
        return score / sim_sum

    def recommend(self, new_user, n=10):
        '''recommend the top 10 movies based on the users nearest neighbors'''
        nearest_neighbors = self.get_nearest_neighbors(new_user)
        # create some list (store) of all movies new_user nearest neighbors
        # have seen that new user has not seen
        new_recs = self.get_new_recs(new_user, nearest_neighbors)
        # use a min heap to store movies with the best scores
        best_recs = []
        # for each of those movies
        for movie_id in new_recs:
            # calculate the predicted score the new user would rate it
            score = self.predict_movie_score(
                new_user, nearest_neighbors, movie_id)
            # put the score and movie in a tuple to store in the min heap
            score_and_movie = (score, movie_id)
            # push to the minheap if its size < n
            if len(best_recs) < n:
                heappush(best_recs, score_and_movie)
            else:
                # if the curr score > min item in minheap (worst best score)
                if score_and_movie > best_recs[0]:
                    # remove the min item and add the new item
                    heappop(best_recs)
                    heappush(best_recs, score_and_movie)
        # return the movies order of best to worst
        results = []
        for _ in range(n):
            next_best_movie_id = heappop(best_recs)[1]  # [1]
            results.append(self.movies.get_title(next_best_movie_id))
        return results[::-1]
