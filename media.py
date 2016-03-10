import webbrowser
class Movie():
    """This class provides a way to create different instances of movies to display using the title, storyline, release date, image and trailer url as inputs"""
    def __init__(self, movie_title, movie_storyline, release_date, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.release = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
