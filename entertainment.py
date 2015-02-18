import media
import fresh_tomatoes
# Create favorite movie instances
# read list.txt file with movie title, box art URL,  YouTube link to the movie trailer
trailers = []
list = open('./list.txt', 'r')

# Create list of favorite movies

for line in list:
	trailers.append(media.Movie(*line.split(',')))
list.close()
# Generate HTML file movies.html
fresh_tomatoes.open_movies_page(trailers)
