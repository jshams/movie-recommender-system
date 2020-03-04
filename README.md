# Movie Recommender System

## What is a Recommender System?
A recommender system uses data about users to recommend similar products or items to other users that use the same products or items.

## What are some ways to implement Recommender Systems for movies?
### Content based filtering
- Use content about each movie (description, actors, director, year made, etc.) to find similar movies.
- This could require multiple other models to interpret the data:
    - For instance descriptions would have to be vectorized (NLP). Could use TFIDF.
    - You could also have another model that vectorizes actors and actresses based on their movies. Actors in similar movies are closer to each other.
- So if a users likes certain movies you can recommend them movies similar to what they watch.
### Collaborative Filtering
- Collaborative filtering is a technique that uses data collected from users.
- For instance with movies you can have user ratings on movies, and users who rated similar movies probably have similar taste and you can reccomend them the movies their similar users liked.
- 