# Belong Assignment

## Part 1: Scraping IMDB to 250 movie data
The top 250 movie data is fetched using IMDBPY library. The fetched data is saved in "imdb-top250.csv"
## Part 2: Builing movie recommandation for a given movie
If we want to recommend movies for "batman begins", then we will check which movies are similar to this movie using a similarity function. I am going to use cosine function to calculate similarity.
Now the question is : What is the feature vector which we are going to use to calculate similarity? We can use IMDbRating and Metascore but what else we can use? I have used movie's genre to create a vector of binary variable. I have created a binary variable for each genre and then assigned it 0 or 1 respectively. If movie's genre are "Sci-Fi, Action, War" then assign 1 to columns representing these genre and 0 to all other respective columns. 
