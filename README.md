# Belong Assignment

## Part 1: Create IMDB Top 250 Movie Dataset
The top 250 movie data is fetched using IMDBPY library. The fetched data is saved in "imdb-top250.csv". 

The script used for the data fetching is "imdb-scraper.py"

## Part 2: Recommand Similar Movies for a Given Movie
If we want to recommend movies for "The Godfather", then we need to check which movies are similar to this movie using a similarity function. Here, I am using cosine function to calculate similarity.

Now the question is: What is the feature vector which we are going to use to calculate similarity? We can use simply use IMDb Rating but what else we can use? I have used movie's genre to create a vector of binary variable. I have created a binary variable for each genre and then assigned it 0 or 1 respectively. If movie's genre are "Sci-Fi, Action, War" then assign 1 to columns representing these genre and 0 to all other respective columns. Using the rating combined with the genre I created the feature vector for the similarity calculation. 

Similarity function is compute intensive. For each queried movie if we apply similarity function to all movies, it will be very compute intensive and it will take very long time. So we will apply similarity function to subset of movies which we think are important. So how do we decide which movies are important? I have selected movies which have actors, directors, writers or production companies in common with queried movie.

Finally I am showing the movies with top similarity scores.

The movie recommandation is code is written is the jupyter notebook "imdb-movie-recommandation.ipynb".  
