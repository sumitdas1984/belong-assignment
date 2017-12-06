# create and instance of the IMDb class
from imdb import IMDb
ia = IMDb()

# get top250 movies
top250 = ia.get_top250_movies()

with open("imdb-top250.csv", "w") as out_file:
	out_file.write("Id#Title#Year#Runtime#Languege#Country#Genre#Director#Writer#Actors#Production#IMDB_Rating\n")
	i = 1
	for movie in top250:
		# Use a try-catch on the loop to prevent temporary connection-related issues from stopping the scrape
		try:
			print('@@count:',i)
			movie_fields = []

			movieID = movie.movieID
			movie_fields.append(str(movieID))

			movie = ia.get_movie(movieID)	

			title = movie.get('title')
			movie_fields.append(str(title))

			year = movie.get('year')
			movie_fields.append(str(year))

			runtime = movie.get('runtime')
			movie_fields.append(str('|'.join(runtime)))

			languages = movie.get('languages')
			movie_fields.append(str('|'.join(languages)))

			country = movie.get('countries')
			movie_fields.append(str('|'.join(country)))

			# mpaa_rating = movie['mpaa']
			# print(mpaa_rating)

			genres = movie.get('genres')
			movie_fields.append(str('|'.join(genres)))

			directors = movie.get('director')
			movie_fields.append(str('|'.join([d.get('name') for d in directors])))

			writer = movie.get('writer')
			movie_fields.append(str('|'.join([d.get('name') for d in writer])))

			actors = movie.get('cast')
			movie_fields.append(str('|'.join([a.get('name') for a in actors])))

			production = movie.get('production companies')
			movie_fields.append(str('|'.join([a.get('name') for a in production])))

			# plot = movie.get('plot')
			# movie_fields.append(str('|'.join([a.get('name') for a in plot])))

			imdb_rating = movie.get('rating')
			movie_fields.append(str(imdb_rating))

			# All entries are comma-delimited
			out_file.write("#".join(movie_fields) + "\n")

			i = i+1
			# if i > 5:
			# 	break
		except Exception as e:
			print("Error with", str(movie))

out_file.close()
