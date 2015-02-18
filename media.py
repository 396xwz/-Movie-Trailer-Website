import webbrowser
# Class Movie
class Movie():
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]	
# Movie Title, Poster Image, Trailer URL
	def __init__(self, movie_title, poster_image, trailer_youtube):
		self.title  = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
# Open browser and play video
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
