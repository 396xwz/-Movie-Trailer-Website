import media
import fresh_tomatoes
# Create favorite movie instances
# movie title, box art URL,  YouTube link to the movie trailer
toy_story = media.Movie("Toy Story",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
jurassic_world = media.Movie("Jurassic World",
			"http://upload.wikimedia.org/wikipedia/commons/2/2c/Jurassic_Park_Entrance_in_Lost_World_20130209a.jpg",
			"https://www.youtube.com/watch?v=RFinNxS5KN4")


school_of_rock = media.Movie("School of Rock",
			"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
			"http://www.youtube.com/watch?v=XCwy6lW5Ixc")
star_wars = media.Movie("Star Wars",
			"http://upload.wikimedia.org/wikipedia/commons/f/ff/Empireslogo.png",
			"https://www.youtube.com/watch?v=JNwNXF9Y6kY")
# Create list of favorite movies
movies = [toy_story, jurassic_world, school_of_rock, star_wars]
# Generate HTML file movies.html
fresh_tomatoes.open_movies_page(movies)
