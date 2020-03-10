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

## How do I approach creating a Reccomender Sytem?
The problem: Given a user who has rated some movies, reccomend them 5 movies.

---

## Approach 1: User-User RS using K Nearest Neighbor Search
This method works by finding the 10 most similar users in our data set,
then reccomending movies based on what the similar users have liked.
This approach is an extremely naive approach to RS with movies.

#### Step By Step Explanation
1. Find 10 most similar users to a given user
    - Uses [Euclidian Distance](https://en.wikipedia.org/wiki/Euclidean_distance) to calculate the
    distance between users. Works quickly because you only have to compare movies both users have seen.
    <img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2018/05/2zjgw1x1.png"></img>
    - The 10 most similar users are the ones with the shortest distance from the original user.
2. Collect all the movies other users have watched
3. For each movie predict the score the original user would rate it. To predict the score of a movie:
    - Find all similar users that have rated the movie.
    - Users that are more similar to the original user will weigh stronger (their reccomendations will count more).
    - Note: This method is flawed because if only one user rates a movie a 5, then that movie will get recommended. This can be fixed by adding more metrics.
4. Return a list of the 10 most highly rated movies by similar users.

This method was inspired by The Coding Train's 3 part series [Nearest Neighbor Recommendation Engine](https://www.youtube.com/watch?v=N8Fabn1om2k&t=1343s)

**Does it work?** Yes  
**Is it as accurate as I'd like it to be?** No  
**Flaws:** Does not care about movies being similar, instead only focuses on users. Does not utilize all the data given.


---

## Approach 2:
This method is similar to the first, but uses more traditional metrics and methodologies.
Instead of finding similar users this method predics the score a user would give for each movie.
Then takes the best predicted ratings and returns those.

#### Step By Step Explanation
1. Predict the score the user would rate each movie
    - A movie score is calculated using this formula:  
    <img style="margin-left: 30%; height: 60px;" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2018/05/Screenshot-from-2018-05-29-20-15-31.png"></img>
    - Here:
        - Pu,i is the prediction of an item
        - Rv,i is the rating given by a user v to a movie i
        - Su,v is the similarity between users
    - Uses [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) as a metric to determine similarity between users.
    <img style="margin-left: 30%; height: 60px;" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2018/05/Screenshot-from-2018-05-31-14-28-18-300x80.png">
2. Return the 10 best predicted movie scores.

This method was inspired from this article.
[Comprehensive Guide to build a Recommendation Engine from scratch (in Python)](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/)

**Does it work?** Yes  
**Is it as accurate as I'd like it to be?** It does a pretty good job.  
**Flaws:** Extremely slow. For each movie we have to look at each user.